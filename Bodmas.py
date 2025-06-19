Weight = int(input("Enter the Weight = "))
x = float(input("Enter the Float number of height = ")) #decimal values
Height = x * 0.3048 #To convert float value in meters
bml = (Weight / (Height**2))

if bml > 18.5 and bml < 24.9:
    print("Healthy")
elif bml > 25 and bml < 29.9:
    print("Over weight")
elif bml > 30:
    print("It can be Obesity")
else:
    print("Underweight (or) Unhealthy")