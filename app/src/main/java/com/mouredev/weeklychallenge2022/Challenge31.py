def leapYears(year):
    return year%400==0 or (year%100!=0 and year%4==0)

cont=0
year=2022
print("Proximos 30 años bisiestos:")
while cont<=30:
    if leapYears(year):
        print(year)
        cont+=1
    year+=1
