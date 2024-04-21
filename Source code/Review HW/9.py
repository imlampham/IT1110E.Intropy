vehicle_type = int(input())
hours = int(input())
if vehicle_type == 1:
   fee_1, time, fee_2 = [0.7, 3, 2.5]
elif vehicle_type == 2:
   fee_1, time, fee_2 = [1.5, 3, 2.0]
elif vehicle_type == 3:
   fee_1, time, fee_2 = [2.5, 2, 3.25]

if hours <= time:
   total_fee = fee_1 * hours
else:
   total_fee = fee_1 * time + fee_2 * (hours - time)

print('{:.2f}'.format(total_fee))