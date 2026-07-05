import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

def deposit():
    while True:
        amount = input("deposit amount -$:")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Amount lesser than 0")
        else:
            print("enter valid amount")
    return amount

def get_no_of_lines():
    while True:
        lines = input("enter the amount of lines you wanna bet on (1-"+str(MAX_LINES)+")?")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
               print("enter valid line amount")
        else:
            print("enter a digit")
    return lines

def get_bet():
    while True:
        amount = input("enter an amount to bet on each line $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"enter a valid amount b/w {MIN_BET} - {MAX_BET}. ")
        else: 
            print("enter a digit")
    return amount


def main():
    balance = deposit()
    lines = get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet >balance:
            print(f"insufficient balance | ${balance}left")
        else: 
            break
    print(f"you are betting ${bet} on {lines} lines.\ntotal bet is {total_bet}")
main()
