

class Display:

    def draw(trade_data):
        for each_action in trade_data[0]:
            print(each_action[0])
        print("Total cost : {}".format(trade_data[1]))
        print("Total gain : {}".format(trade_data[2]))
        print("For an investment of {} you'll retrieve {}".format(trade_data[1],trade_data[3]))
