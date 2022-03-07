# imports
import pickle
from menu import *
from player import *

# list of golfers
golfer_list = []


def handle_inputs():
    """This function handles inputs and calls the necessary function to proceed with the program"""

    player_count = 0
    global golfer_list

    # infinite
    while True:
        menu()  # run menu at the start of the program
        option = int(input("\n> Enter option : "))

        if option == 1:
            print("\n━━━━━━━━━━━━━━━━━━━━ ADD GOLFER ━━━━━━━━━━━━━━━━━━━━")

            try:
                no_of_golfers = int(input("> Enter no of golfers: "))

                for i in range(no_of_golfers):
                    name = input("\n> Enter name of golfer: ")
                    score = int(input("> Enter score golfer: "))

                    if 18 <= score <= 108:
                        add_golfer(name, score)
                    else:
                        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                              + "\n ⚠ ERROR. SCORE SHOULD BE BETWEEN 18 and 108"
                              + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                        continue
            except ValueError:
                print("\n ⚠ ERROR. ENTER VALID INPUT")

        elif option == 2:
            print("\n━━━━━━━━━━━━━━━━━━━━ FIND GOLFER ━━━━━━━━━━━━━━━━━━━━")
            name = input("> Enter name of golfer: ")
            display_golfer(name)

        elif option == 3:
            print("\n\n━━━━━━━━━━━━ GOLFER SCORE TABLE ━━━━━━━━━━━━━━━━━\n")
            display_table()

        elif option == 4:
            save_data(golfer_list)
            print("\n🔔 Saving data...")

        elif option == 5:
            print("\n🔔 Loading data...")
            load_data()

        elif option == 6:
            print("\n🔔 Exiting program...")
            break

        else:
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━" + "\n ⚠ ERROR. ENTER VALID INPUT!" + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━")
            continue


def add_golfer(name, score):
    """This function adds a golfer and their score to the roster"""

    global golfer_list
    found = False

    if name is not None and score is not None:
        if len(golfer_list) > 0:
            for golfer in golfer_list:
                if str(golfer.get_name()) == name:
                    found = True
                    choice = input("Golfer already exists. Do you wish to override (y/n)? ")
                    if choice.lower() == "y":
                        golfer_list.remove(golfer)  # remove existing obj
                        golf_player = GolfPlayer(name, score)  # create new obj
                        golfer_list.append(golf_player)  # add obj to list
                        golf_player.display_payer()  # display obj attributes
                        print("Golfers: ", golfer_list)
                        break
                    else:
                        print("\n\n--------------------------" + "\n\tOVERRIDE CANCELLED \n" +
                              "--------------------------")
                        break
        if found is False:
            golf_player = GolfPlayer(name, score)
            golfer_list.append(golf_player)
            golf_player.display_payer()
            print("Golfers: ", golfer_list)

    else:
        print("\n⚠ Error adding golfer. Enter again")


def display_golfer(golfer_name):
    """This function finds the requested golfer and outputs their details"""

    found = False

    # find golfer by looping through list
    for golfer in golfer_list:
        if golfer.get_name() == golfer_name:
            found = True
            golfer.display_payer()
            break
        else:
            continue

    if not found:
        print("\n--------------------------" + "\n\tGOLFER NOT FOUND \n" + "--------------------------")


def display_table():
    """This function outputs the golfer score table"""

    # table headers
    print("\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("\t      GOLFER   ┃   SCORE   ┃   PLACE              ")
    print("\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    golfer_list.sort(key=lambda x: x.get_score(), reverse=True)  # sort according to score

    # construct table using string formatting
    for i in range(len(golfer_list)):
        print(("\t{}" + str(golfer_list[i].get_name()) + "{}" + str(golfer_list[i].get_score()) + "{}" + str(
            i + 1)).format(
            " " * (12 - len(str(golfer_list[i].get_name()))),
            " " * (12 - len(str(golfer_list[i].get_score()))),
            " " * (12 - len(str(i)))), end="      ")
        print("\n\t-----------------------------------------")
    print("")


def save_data(li):
    """This function saves all the golfer data into a file"""

    output_file = open('data/data.dat', 'wb')
    pickle.dump(li, output_file)
    output_file.close()


def load_data():
    """This function loads all the golfer data from a file"""
    global golfer_list

    if len(golfer_list) > 0:
        choice = input("\nGolfers already exist in roster."
                       "\nDo you wish to load data from file and override existing data (y/n)? ")

        if choice.lower() == "y":
            with (open("data/data.dat", "rb")) as openfile:
                while True:
                    try:
                        golfer_list = pickle.load(openfile)
                    except EOFError:
                        break
                print(golfer_list)
        else:
            print("\n--------------------------" + "\n\tOVERRIDE CANCELLED \n" +
                  "--------------------------")

    else:
        with (open("data/data.dat", "rb")) as openfile:
            while True:
                try:
                    golfer_list = pickle.load(openfile)
                except EOFError:
                    break
            print(golfer_list)
