import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    stocks = db.execute("SELECT * FROM stocks WHERE user_id=?", session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])
    for stock in stocks:
        currentPrice = lookup(stock["stock"])["price"]
        stock["currentPrice"] = currentPrice
    totalStock = 0
    for stock in stocks:
        currentPrice = lookup(stock["stock"])["price"]
        shares = stock["shares"]
        amount = currentPrice * shares
        totalStock += amount


    return render_template("index.html", stocks=stocks, cash=cash, totalStock=totalStock)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Input Symbol", 403)
        result = lookup(symbol)
        if not result:
             return apology("Invalid Symbol", 403)
        shares = request.form.get("shares")
        if not shares or int(shares) <= 0:
            return apology("Invalid shares", 403)
        cash = db.execute("SELECT cash FROM users WHERE id =?", session["user_id"])
        amount = int(shares) * float(result["price"])
        if cash[0]["cash"] < amount:
            return apology("Not enough cash", 403)
        # track purchase
        curr = db.execute("SELECT shares FROM stocks WHERE stock=?", symbol)

        if not curr:
            db.execute("INSERT INTO stocks (user_id, stock, price, shares) VALUES(?, ?, ?, ?)", session["user_id"], symbol, result["price"], shares)
        else:
            db.execute("UPDATE stocks SET shares =? WHERE stock =?", curr[0]["shares"] + int(shares), symbol)
        # update cash
        db.execute("INSERT INTO transactions (user_id, type, stock, price, shares) VALUES(?,?,?,?,?)", session["user_id"], "buy", symbol, result["price"], shares)
        db.execute("UPDATE users SET cash =? WHERE id=?", cash[0]["cash"] - (amount), session["user_id"])
        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT * FROM transactions WHERE user_id=?", session["user_id"])
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        result = lookup(symbol)
        if result:
            return render_template("quoted.html", result=result)
    return apology("Lookup unsuccessful", 400)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        usernames = db.execute("SELECT username FROM users")

        username_list = []

        for i in range(len(usernames)):
            username_list.append(usernames[i]["username"])

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not username:
            return apology("must provide username", 400)
        elif username in username_list:
            return apology("username already exists", 400)
        elif not password or not confirmation:
            return apology("Please input password and confirmation", 400)
        elif password != confirmation:
            return apology("password and confirmation must be the same")
        else:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password, method='pbkdf2:sha256', salt_length=8))
            user = db.execute("SELECT id FROM users WHERE username=?", username)
            session["user_id"] = user[0]["id"]
            return redirect("/")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        stocks = db.execute("SELECT * FROM stocks WHERE user_id=?", session["user_id"])
        uniqueStocks = set()
        for stock in stocks:
            uniqueStocks.add(stock["stock"])
        return render_template("sell.html", uniqueStocks=uniqueStocks)
    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        stock = db.execute("SELECT * FROM stocks WHERE stock = ? AND user_id=?", symbol, session["user_id"])

        if not symbol or not shares or int(shares) < 1:
            return apology("Please Choose Stock and Shares")

        if len(stock) == 0 or stock[0]["shares"] < int(shares):
             return apology("Stock not available or enough")

        current_price = lookup(symbol)["price"]
        selling_price = current_price * int(shares)

        cash = db.execute("SELECT cash FROM users WHERE id =?", session["user_id"])

        db.execute("UPDATE users SET cash =? WHERE id=?", cash[0]["cash"] + selling_price, session["user_id"])

        share = db.execute("SELECT shares FROM stocks WHERE user_id =? AND stock=?", session["user_id"], symbol)


        db.execute("UPDATE stocks SET shares =? WHERE user_id=? AND stock=?", share[0]["shares"] - int(shares), session["user_id"], symbol)
        db.execute("INSERT INTO transactions (user_id, type, stock, price, shares) VALUES(?,?,?,?,?)", session["user_id"], "sell", symbol, current_price, shares)

        return redirect("/")



