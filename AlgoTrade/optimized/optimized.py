from controllers.trade import Trade
import sys

def main():
    Trade.begin(str(sys.argv[1]))

if __name__ == '__main__':
    main()