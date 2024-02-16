# Given the following tax brackets:
# a. Income up to $10 000: 10%
# b. Income over $10 000 and up to $40 000: 15%
# c. Income over $40 000 and up to $80 000: 20%
# d. Income over $80 000: 25%
# 2. Ask the user for their income and calculate the tax they owe based on the brackets.
# Tips : Note that this is a progressive tax, so they'll owe different amounts for different
# portions of their income.

lower_bracket_tax = 10000 * 0.1
middle_bracket_tax = 30000 * 0.15
upper_bracket_tax = 40000 * 0.20

income = float(input("Type your income: "))

if income > 80000:
    excess = income - 80000
    excess_tax = excess * 0.25
    fixed_tax = lower_bracket_tax + middle_bracket_tax + upper_bracket_tax

elif income > 40000:
    excess = income - 40000
    excess_tax = excess * 0.20
    fixed_tax = lower_bracket_tax + middle_bracket_tax

elif income > 10000:
    excess = income - 10000
    excess_tax = excess * 0.15
    fixed_tax = lower_bracket_tax

else:
    total_tax = income * 0.10
    print("The total taxes you owe are ", total_tax)
    exit()

total_tax = excess_tax + fixed_tax
print("The total income tax you owe is ", total_tax)

print(
    "///////////////////////////////////////////////SEPARACION////////////////////////////////////////////"
)

Ingreso = int(input("Dame tu sueldo: "))
lower_bracket_tax = 1000
middle_bracket_tax = 4500
upper_bracket_tax = 8000

if Ingreso > 10000:
    sobrante = Ingreso - 10000
else:
    lower_bracket_tax = Ingreso * 0.10
    print(lower_bracket_tax)

if sobrante > 30000:
    sobrante = sobrante - 30000
else:
    middle_bracket_tax = sobrante * 0.15
    print(lower_bracket_tax + middle_bracket_tax)

if sobrante > 40000:
    sobrante = sobrante - 40000
else:
    upper_bracket_tax = sobrante * 0.20
    print(lower_bracket_tax + middle_bracket_tax + upper_bracket_tax)

final_bracket_tax = sobrante * 0.25
print(lower_bracket_tax + middle_bracket_tax + upper_bracket_tax + final_bracket_tax)
