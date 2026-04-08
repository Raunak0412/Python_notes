
#  Python intrest calculator
pa=float(input("Enter ur principal amount: "))

r=float(input("Enter the rate:"))

t=int(input("Enter the time:"))

n=2

compound=pa*pow((1+r/100),t)

print(compound)