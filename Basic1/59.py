feet=float(raw_input("Enter feet: "))
inch=float(raw_input("Enter inches: "))

centi=inch*2.54
centi=centi+(feet*30.48)

print(centi)