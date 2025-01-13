


#three inputs from the customer
print("Welcome to Gross and Net Pay Estimator.")
hourly_wage=(float(input("Enter Hourly Wage in dollars (float):\n")))
work_hours=(int(input("Enter Hours Per Week (integer):\n")))
work_year=(int(input("Enter Weeks Per Year Worked(integer):\n")))
# the weekly pay
income_week=hourly_wage*work_hours
gross_pay=hourly_wage*work_year
#the gross pay
print ("Your weekly pay is",income_week,"dollars per year") 
print("Your Gross Pay is",gross_pay,"dollars per year" )    