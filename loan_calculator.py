import math
import sys

args = sys.argv
type = args[1].split("=")[1]
principal = None
payment = None
interest = None
periods = None

def calculate_annuity(principal, payment, interest, periods):
    if not principal:
        factor = math.pow(1 + interest, periods)
        principal = payment / (interest * factor / (factor - 1))
        principal = math.floor(principal)
        print(f"Your credit principal = {principal}!")
    if not payment:
        factor = math.pow(1 + interest, periods)
        payment = principal * (interest * factor / (factor - 1))
        payment = math.ceil(payment)
        print(f"Your annuity payment = {payment}!")
    if not periods:
        periods = math.log((payment / (payment - interest * principal)), 1 + interest)
        periods = math.ceil(periods)
        year = periods // 12
        remain_month = periods % 12
        if year < 1:
            print(f"You need {periods} months to repay this credit!")
        elif remain_month < 1:
            print(f"You need {year} years to repay this credit!")
        elif year == 1 and remain_month == 0:
            print("You need 1 year to repay this credit!")
        else:
            print(f"You need {year} years and {remain_month} months to repay this credit!")
    overpayment = math.ceil(payment * periods - principal)
    print(f"Overpayment = {overpayment}")

def calculate_diff(principal, periods, interest):
    paid = 0
    for i in range(1, int(periods) + 1):
        factor = principal - (principal * (i - 1)) / periods
        payment = principal / periods + (interest * factor)
        print(f"Month {i}: paid out {math.ceil(payment)}")
        paid += math.ceil(payment)
    overpaid = math.ceil(paid - principal)
    print(f"Overpayment = {overpaid}")

def check_parameter(apara):
    global principal, periods, interest, payment
    para_name = apara.split("=")[0]
    para_value = float(apara.split("=")[1])
    if "principal" in para_name:
        principal = para_value
    elif "periods" in para_name:
        periods = para_value
    elif "interest" in para_name:
        interest = para_value / (100 * 12)
    else:
        payment = para_value

if len(args) != 5 or type not in ["annuity", "diff"]:
    print("Incorrect parameters")
else:
    for i in range(2, 5):
        check_parameter(args[i])
    if type == "diff" and payment:
        print("Incorrect parameters")
    else:
        if type == "annuity":
            calculate_annuity(principal, payment, interest, periods)
        else:
            calculate_diff(principal, periods, interest)


