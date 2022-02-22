from datetime import date
def test(month, year): 
    return str(date(year,month,13).strftime("%A")=='Monday')

print(test(6,2022))
print(test(3,2022))