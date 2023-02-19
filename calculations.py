
def daily_ratio(prev_adj_close, current_adj_close):
    daily_ratio_value = current_adj_close/prev_adj_close
    return daily_ratio_value


def main():
    count = 0
    prev_adj_close = 0.0
    try:
        file = open(f"Data\SPY.txt", "r")
        data = file.readlines()
    finally:
        file.close()
    for line in data:
        try:
            count+=1
            if count >2:
                values = line.split()
                current_adj_close = float((values[4]))
                if count >3:
                    daily_ratio_value = daily_ratio(prev_adj_close, current_adj_close)
                prev_adj_close = current_adj_close
                print(daily_ratio_value)
        except:
            print("Error")

main()

