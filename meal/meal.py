def main():
    time = input("What time is it? ")
    time = convert(time)
    print(time)



def convert(time):
    hr, min = time.split(":")
    hr = float(hr)
    min = float(min) / 60
    return hr + min



if __name__ == "__main__":
    main()