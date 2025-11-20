x=int(input("Enter 1st Number:"))
y=int(input("Enter 2nd Number:"))
z=int(input("Enter 3rd Number:"))
sum=x+y+z
Avg=sum/3
print(f"{sum} is the sum")
print(f"{Avg} is the Average")


print("Choose from the follwing options:")
print("1. Celcius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice=int(input("Enter your choice(1 or 2):"))
if choice==1:
  C=float(input("Enter value in Celsius:"))
  F=(C*9/5)+32
  print(f"{F}\u00B0F is the value in Fahrenheit")
  elif choice==2:
  F=float(input("Enter value in Fahrenheit:"))
  C=(F-32)*5/9
  print(f"{C}\u00B0C is the value in Celsius")
  else:
  print("Invalid Choice!!!!!!!!!!!")