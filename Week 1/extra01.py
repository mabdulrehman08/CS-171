#extra01.py
#Creating a simple currency converter program
#common finanical application
origin_currency=input("Enter the origin currency name\n")
destination_currency=input("Enter the destination currency name\n")
exhnage_rate=float(input("Enter the exchange rate from " + origin_currency +" to "+ destination_currency +"\n"))
amount=float(input("Enter the amount "+ origin_currency + "\n"))
currency=(exhnage_rate*amount)
print("{amount:.2f} {origin_currency} is equivalent to {currency:.2f} {destination_currency}")

