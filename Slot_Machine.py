import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}

symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


def check_winings(columns, lines, bet, values):
    winings = 0
    wining_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winings += values[symbol] * bet
            wining_lines.append(line + 1)

    return winings, wining_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("what would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? "
        )
        if lines.isdigit():  # if input is a digit
            lines = int(lines)  # converting it to an integer
            if (
                1 <= lines <= MAX_LINES
            ):  # checking if line is greater tha equal to 1 and is less than equal to maximum lines
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("what would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number")

    return amount


def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"you do not have enough to bet that amount, your current balance is ${balance}"
            )
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}"
    )

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winings, wining_lines = check_winings(slots, lines, bet, symbol_value)
    print(f"You won ${winings}.")
    print(f"You won on lines:", *wining_lines)
    return winings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answere = input("Press enter to spin (q to quit).")
        if answere == "q":
            break
        balance += game(balance)

    print(f"You are left with ${balance}")


main()
