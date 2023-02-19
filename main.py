import yfinance as yf
from datetime import date, timedelta

Stocks = [
"SPY",
"QQQ",
"^VIX",
"XLE",
"SMH",
"TLT"
]

#data
def main():
    print(page)
    company = yf.Ticker(page)
    company.fast_info   

    data = yf.download(tickers = page,
                       period = "2y",
                       interval = "1d")
    print(data, file = outfile)

#data scraping
if __name__ == "__main__":
    for i in range (len(Stocks)):
        if Stocks[i] == "SPY":
            outfile = open(f"SPY.txt", "w")
        elif Stocks[i] == "QQQ":
            outfile = open(f"QQQ.txt", "w")
        elif Stocks[i] == "^VIX":
            outfile = open(f"VIX.txt", "w")
        elif Stocks[i] == "XLE":
            outfile = open(f"XLE.txt", "w")
        elif Stocks[i] == "SMH":
            outfile = open(f"SMH.txt", "w")
        elif Stocks[i] == "TLT":
            outfile = open(f"TLT.txt", "w")
        page = Stocks[i]
        main()
        outfile.close()





