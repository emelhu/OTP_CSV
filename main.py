import sys
import CSVtoDB


class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def processCommand(command):
    print("Ezt a parancsot kérte: {command}")

def main():
    print()
    print()
    print(str(bcolors.HEADER) + "--- OTP Bank csv forgalmi kivonat feldolgozása --- (c) eMeL" + str(bcolors.ENDC))
    print()
    print()

    if len(sys.argv) > 1:
        command = sys.argv[1]
    else:
        print(str(bcolors.BLUE) + "A végrehajtható parancsok listája:" + str(bcolors.ENDC))
        print("CSV")
        print()

        command = input("Végrehajtandó parancs neve: ")

    processCommand(command)

#--------------------------------------------------------------------------------

if __name__ == "__main__":
    main()