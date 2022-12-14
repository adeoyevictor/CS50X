-- Keep a log of any SQL queries you execute as you solve the mystery.
--
SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND year = 2021 AND street = "Humphrey Street";
--
-- 10:15 am
-- bakery
-- interviews
-- 3 witnesses

--
SELECT name, transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;
-- ruth thief left bakery parking lot around 10 :15 to 10:25
SELECT activity, license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute<=25;
--
SELECT name, phone_number , passport_number FROM people WHERE license_plate IN(
    SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute<=25 AND activity = "exit"
);
-- Vanessa, Barry, Iman, Sofia, Luca, Diana, Kelsey, Bruce (possible drivers/thiefs)

--
-- eugene before getting to emma's bakery saw thief at atm on leggett street withdrawing
SELECT account_number, amount  FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type="withdraw";
SELECT account_number  FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type="withdraw";

SELECT name FROM people WHERE id IN(
SELECT person_id FROM bank_accounts WHERE account_number IN(SELECT account_number  FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type="withdraw"
));
-- Kenny ,Iman, Benista, Taylor, Brooke, Luca,Diana, Bruce (possible withdrawers)

-- raymond thief called someone for less than a minute (planning to take earliest flight out of fiftyville tomoro) accomplice asked to purchase ticket

SELECT caller, receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60);
SELECT name FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60);

-- callers Kenny, Sofia, Benista, Taylor, Diana, Kelsey, Bruce, Carina
-- receivers James, Larry, Anna, Jack, Melissa, Jacqueline, Philip, Robin, Doris

-- thiefs narrowed down to DIANA and BRUCE
-- accomplices PHILIP and ROBIN based on phone call
SELECT passport_number FROM people WHERE name = "Diana" OR name = "Bruce";

SELECT flight_id FROM passengers WHERE passport_number=(SELECT passport_number FROM people WHERE name = "Diana");
SELECT flight_id FROM passengers WHERE passport_number=(SELECT passport_number FROM people WHERE name = "Bruce");



SELECT full_name, city, abbreviation FROM airports WHERE id = 8;


SELECT origin_airport_id, destination_airport_id FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND id = 18;

SELECT id FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND hour <10;

SELECT origin_airport_id, destination_airport_id FROM flights WHERE id = 36;

SELECT city FROM airports WHERE id = 4;