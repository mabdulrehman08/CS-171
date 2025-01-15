
import math
#Name:Muhammad Abdulrehman
#Date:01/13/2025
#file name=hw01.py
#CS-171-WEEK01-HW01
# This program estimates the gross and net pay for an employee based on their hourly wage, hours worked, and total taxes/deductions.
#Three inputs from the customer
print("Welcome to Gross and Net Pay Estimator.")
#how much earned in hours
hourly_wage=(float(input("Enter Hourly Wage in dollars (float):\n")))
#hour spend on work
work_hours=(int(input("Enter Hours Per Week (integer):\n")))
#how many week in one hour
week_year=(int(input("Enter Weeks Per Year Worked(integer):\n")))
gross_pay=(hourly_wage*work_hours*week_year)
# the weekly pay
income_week=hourly_wage*work_hours
#social security tax
social_security_tax=(gross_pay*0.06)
remaining_inc=(gross_pay-social_security_tax)
#Medicare Tax
medicare_tax=(remaining_inc*0.02)
remaining_inc=(remaining_inc-medicare_tax)
#Irs Wage Tax
irs_wage_tax=(remaining_inc*0.12)
remaining_inc=(remaining_inc-irs_wage_tax)
#PA State tax
pa_state_tax=(remaining_inc*0.0307)
remaining_inc=(remaining_inc-pa_state_tax)
#Philadephia Tax
philly_tax=(remaining_inc*0.0375)
remaining_inc=(remaining_inc-philly_tax)
#heath insurance
heath_insurance=(396*12)
remaining_inc=(remaining_inc-heath_insurance)
#net pay information
remaining_income_after_tax=remaining_inc
net_pay_per_week=(remaining_income_after_tax/7)
net_pay_per_hour=(net_pay_per_week/work_hours)
net_pay_to_gross_pay=((remaining_income_after_tax/gross_pay)*100)
#INCOME LEFT AFTER TAX DEDUCTION
deduction=(100-net_pay_to_gross_pay)

#Outputs
print("Gross Pay Information")
print ("You will make ${:.2f}per week.".format(income_week)) 
print("You will make ${:.2f}per year.".format(gross_pay) )  
#1
print("Taxes and Deductions")
print("You will pay ${:.2f} in Social Security Taxes.".format(social_security_tax))
print("You will pay ${:.2f} in Medicare Taxes.".format(medicare_tax))
print("You will pay ${:.2f} in IRS Taxes.".format(irs_wage_tax))
print("You will pay ${:.2f} in PA State Taxes.".format(pa_state_tax))
print("You will pay ${:.2f} in Phila Taxes.".format(philly_tax))
print("You will pay ${:.2f} for health insurance.".format(heath_insurance))
#2
print("Net Pay Information")
print("Your take home pay will be ${:.2f} per year.".format(remaining_income_after_tax))
print("This is an hourly take home pay of ${:.2f}.".format(net_pay_per_hour))
print("This is a weekly take home pay of ${:.2f}.".format(net_pay_per_week))
print("Your Net Pay is ${:.2f}percent of your Gross Pay.".format(net_pay_to_gross_pay))