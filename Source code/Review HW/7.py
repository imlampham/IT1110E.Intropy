basic_salary = int(input())
if basic_salary <= 10000:
   HRA = 20/100
   DA = 80/100
if 10001 <= basic_salary <= 20000:
   HRA = 25/100
   DA = 90/100
if basic_salary >= 20001:
   HRA = 30/100
   DA = 95/100
da = basic_salary * DA
hra = basic_salary * HRA
gross_salary = basic_salary + da + hra
print('{:.2f}'.format(gross_salary))
