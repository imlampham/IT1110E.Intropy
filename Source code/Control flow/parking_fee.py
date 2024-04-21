type = int(input())
hours = int(input())
if type == 1:
    if hours < 3:
        fee = 0.70 * hours
    else:
        fee = 0.70 * 3 + 2.50 * (hours - 3)
elif type == 2:
    if hours < 3:
        fee = 1.50 * hours
    else:
        fee = 1.50 * 3 + 2.00 * (hours - 3)
else:
    if hours < 3:
        fee = 2.50 * hours
    else:
        fee = 2.50 * 3 + 3.25 * (hours - 3)
formated_fee = '{:.2f}'.format(fee)
print(formated_fee)