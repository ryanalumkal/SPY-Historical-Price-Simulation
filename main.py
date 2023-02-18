import yfinance as yf
from datetime import date, timedelta

Stocks = [
"SPY",
"QQQ",
"VIX",
"XLE",
"SMH",
"TLT"
]

def main():
    #comp = yf.Ticker(page)
    data = yf.download(page, start = start_date, end=end_date)
    print(page, data, file=outfile)

if __name__ == "__main__":
    end_date = date.today()
    start_date = end_date - timedelta(days =1095)
    outfile = open("data.txt", "w")
    for i in range (len(Stocks)):
        page = Stocks[i]
        main()
    outfile.close()





