principle=0
rate=0
time=0

while principle<=0:
    principle=float(input("enter your principle amount:"))
    if principle<=0:
        print("principle cannot be less than or equal to zero")


while rate<=0:
    rate=float(input("enter your interest rate: :"))
    if rate<=0:
        print("interest rate cannot be less than or equal to zero")

while time<=0:
    time=int(input("enter your time in years:"))
    if time<=0:
        print("time cannot be less than or equal to zero")
total=principle*pow((1+rate/100),time)
print(f"your balance after{time}years:${total:2f}")