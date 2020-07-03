import random
import sqlite3


conn = sqlite3.connect("card.s3db")
cur = conn.cursor()
cur.execute("drop table card")
cur.execute("CREATE TABLE card(id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);")
conn.commit()


class Credit_card():
    def __init__(self):
        self.bin = "400000"
        self.can = "".join([str(random.choice(range(0, 10))) for lt in range(9)])
        self.bincan = self.bin + self.can
        self.card_num = self.bincan + str(self.luhn())
        self.pin = "".join([str(random.choice(range(0, 10))) for j in range(4)])
        self.balance = 0

    def luhn(self):
        alist = [int(ii) for ii in self.bincan]
        mod1 = [alist[o] * 2 if (o + 1) % 2 == 1 else alist[o] for o in range(len(alist))]
        mod2 = [f - 9 if f > 9 else f for f in mod1]
        total = sum(mod2)
        if total % 10 == 0:
            return 0
        else:
            return 10 - total % 10

    def check_balance(self):
        return self.balance


def check_luhn(card_num):
    alist = [int(ii) for ii in card_num]
    mod1 = [alist[o] * 2 if (o + 1) % 2 == 1 else alist[o] for o in range(len(alist) - 1)]
    mod2 = [f - 9 if f > 9 else f for f in mod1]
    total = sum(mod2)
    return (total + int(card_num[-1])) % 10 == 0


def bank_os():
    global finish, i
    command = input("1. Create an account\n2. Log into account\n0. Exit\n")
    if command == "1":
        i += 1
        credit_card = Credit_card()
        card_info = (i, credit_card.card_num, credit_card.pin, credit_card.balance)
        cur.execute("INSERT INTO card VALUES (?,?,?,?)", card_info)
        conn.commit()
        print("\nYour card has been created")
        print(f"Your card number:\n{credit_card.card_num}\nYour card PIN:\n{credit_card.pin}\n")
    elif command == "2":
        user_card_num = input("\nEnter your card number:\n")
        user_pin = input("Enter your PIN:\n")
        t = (user_card_num, user_pin)
        cur.execute("SELECT * FROM card WHERE number=?", (t[0],))
        conn.commit()
        corr = cur.fetchone()  # my card
        if not corr or corr[2] != t[1]:
            print("\nWrong card number or PIN!")
        else:
            print("\nYou have successfully logged in!\n")
            while True:
                cur.execute("SELECT * FROM card WHERE number=?", (t[0],))
                conn.commit()
                corr = list(cur.fetchone())

                option = input("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n")
                if option == "1":
                    print(f"Balance: {corr[3]}\n")
                elif option == "2":
                    amount = int(input("Enter income:\n"))
                    corr[3] += amount
                    cur.execute("UPDATE card SET balance=? WHERE number=?", (corr[3],corr[1]))
                    conn.commit()
                    print("Income was added!\n")
                elif option == "3":
                    enter_card_num = input("\nTransfer\nEnter card number:\n")
                    if not check_luhn(enter_card_num):
                        print("Probably you made mistake in the card number. Please try again!\n")
                    else:
                        cur.execute("SELECT * FROM card WHERE number=?", (enter_card_num,))
                        conn.commit()
                        info = cur.fetchone()  # target card
                        if not info:
                            print("Such a card does not exist.\n")
                        else:
                            money_trans = int(input("Enter how much money you want to transfer:\n"))
                            if corr[3] < money_trans:
                                print("Not enough money!\n")
                            else:
                                info = list(info)
                                corr[3] -= money_trans
                                info[3] += money_trans
                                cur.execute("UPDATE card SET balance=? WHERE number=?", (corr[3], corr[1]))
                                cur.execute("UPDATE card SET balance=? wHERE number=?", (info[3], info[1]))
                                conn.commit()
                                print("Success!\n")
                elif option == "4":
                    cur.execute("DELETE FROM card WHERE number=?",(user_card_num,))
                    conn.commit()
                    print("\nThe account has been closed!\n")
                    break
                elif option == "5":
                    print("\nYou have successfully logged out!\n")
                    break
                elif option == "0":
                    finish = True
                    break
    else:
        finish = True


finish = False
i = 0
while not finish:
    bank_os()
print("\nBye!")



















