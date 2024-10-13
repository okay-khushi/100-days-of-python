print("Welcome to the tip calculator!!")
total=float(input("what was the total bill?"))
tip=float(input("how much tip would you like to give?(in percentage)"))     
peep=int(input("how  many people to split the bill?"))
tip=total*(tip/100)
each=(total+tip)/peep
each=round(each,2)
print(f"each person should pay: {each}")