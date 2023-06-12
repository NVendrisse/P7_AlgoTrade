from controllers.trade import Trade
import sys

def main():
    try:
        Trade.begin(str(sys.argv[1]))
    except IndexError:
        print("\nVous devez entrer un nom de fichier de données\n")
    except FileNotFoundError:
        print("\nVous devez sélectionner fichier de données existant\n")



if __name__ == '__main__':
    main()