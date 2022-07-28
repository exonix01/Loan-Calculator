import math
import argparse
import sys

def differentiated_payments(P, n, i):
    sum = 0
    for x in range(n):
        D = math.ceil ((P / n) + i * (P - (( P * (x)) / n)))
        print(f'Month {x + 1}: payment is {D}')
        sum += D
    overpayment = sum - P
    print(f'Overpayment = {overpayment}')

def number_of_payments(a, p, i):
    n = math.ceil(math.log(a / (a - i * p) , 1 + i))
    year = n // 12
    month = n % 12
    if year == 0:
        if month > 1:
            print(f'It will take {month} months to repay this loan!')
        else:
            print(f'It will take {month} month to repay this loan!')
    elif month == 0:
        if year > 1:
            print(f'It will take {year} years to repay this loan!')
        else:
            print(f'It will take {year} year to repay this loan!')
    else:
        if month == 1 and year == 1:
            print(f'It will take {year} year and {month} month to repay this loan!')
        elif month == 1:
            print(f'It will take {year} years and {month} month to repay this loan!')
        elif year == 1:
            print(f'It will take {year} year and {month} months to repay this loan!')
        else:
            print(f'It will take {year} years and {month} months to repay this loan!')
    return n

message = 'Incorrect parameters.'

parser = argparse.ArgumentParser()
parser.add_argument('--type', default = 0)
parser.add_argument('--payment', default = 0)
parser.add_argument('--principal', default = 0)
parser.add_argument('--periods', default = 0)
parser.add_argument('--interest', default = 0)
len_args = len(sys.argv) - 1
args = parser.parse_args()

if len_args != 4:
    print(message)
else:
    typ = args.type
    payment = float(args.payment)
    principal = int(args.principal)
    periods = int(args.periods)
    interest = float(args.interest)
    interest_m = (interest / 12) / 100 
    if payment < 0 or principal < 0 or periods < 0 or interest < 0:
        print(message)
    else:
        if typ == 'annuity':
            if payment == 0:
                payment = math.ceil (principal * ((interest_m * (1 + interest_m) ** periods) / ((1 + interest_m) ** periods - 1)))
                print(f'Your annuity payment = {payment}!')
            elif principal == 0:
                principal = payment / ((interest_m * (1 + interest_m) ** periods) / ((1 + interest_m) ** periods - 1))
                print(f'Your loan principal = {principal}!')
            elif periods == 0:
                periods = number_of_payments(payment, principal, interest_m)
            overpayment = payment * periods - principal
            print(f'Overpayment = {overpayment}')
        elif typ == 'diff':
            differentiated_payments(principal, periods, interest_m)
        else:
            print(message)