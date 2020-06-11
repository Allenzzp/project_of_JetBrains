import random

rate = 0

def cheater(user_option, rate, option_list):
    cp_option = random.choice(option_list)
    index = option_list.index(cp_option)
    length = len(option_list) // 2
    # create win situation
    if index >= length:
        win_situ = (option_list[(index - length):index])
    else:
        ft = option_list[:index]
        bk = option_list[-(length - len(ft)):]
        win_situ = ft + bk
    # determine win or lose
    if user_option == cp_option:
        print(f"There is a draw ({user_option})")
        rate += 50
    elif user_option in win_situ:
        print(f"Sorry, but computer chose {cp_option}")
    else:
        print(f"Well done. Computer chose {cp_option} and failed")
        rate += 100
    return rate

def play_game():
    global rate
    name = input("Enter your name: ")
    print("Hello", name)
    with open("rating.txt") as f:
        rate_list = f.readlines()
        for item in rate_list:
            if name in item:
                rate = int(name.split(" ")[1])
    option_list = input().split()
    if not option_list:
        option_list = ["rock", "paper", "scissors"]
    print("Okay, let's start")
    while True:
        user_option = input()
        if user_option not in [*option_list, "!exit", "!rating"]:
            print("Invalid input")
        elif user_option == "!exit":
            print("Bye!")
            break
        elif user_option == "!rating":
            print(f"Your rating: {rate}")
        else:
            rate = cheater(user_option, rate, option_list)

play_game()