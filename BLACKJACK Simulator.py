import random

def blckjck_program():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")
    print("Enter 'x' for bet to exit")

    starting_money = float(input("\nStarting Money:  "))
    program_running = True
    while program_running:
        bet_amount = (input("\nBet Amount:      "))
        if bet_amount == "x":
            break
        number = (random.randint(1,100))
        if number > 95:    
            starting_money = starting_money + (1.5*float(bet_amount))
            print("You Got Blackjack!")
            print("Money:  {}\n".format(starting_money))
        elif number > 58:
            starting_money = starting_money + (float(bet_amount))
            print("You Won!")
            print("Money:  {}\n".format(starting_money))
        elif number > 49:
            starting_money = starting_money
            print("You Pushed.")
            print("Money:  {}\n".format(starting_money))
        else:
            starting_money = starting_money - (float(bet_amount))
            print("You Lost :(")
            print("Money:  {}\n".format(starting_money))
blckjck_program()
print("Bye!")
