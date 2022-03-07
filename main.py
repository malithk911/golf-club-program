
# imports
from functions import handle_inputs

# __main__
if __name__ == "__main__":
    try:
        handle_inputs()
    except ValueError:  # if user input is not integers
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + "\n ⚠ ERROR. ENTER VALID INPUT!" + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        handle_inputs()
