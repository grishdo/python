from sys import argv

script_name, production, rate, bonus = argv


def payroll_calc(production1, rate1, bonus1):
    return int(production) * int(rate) + int(bonus)


print(payroll_calc(production, rate, bonus))
