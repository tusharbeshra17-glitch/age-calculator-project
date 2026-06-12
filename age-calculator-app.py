from datetime import date

print("======AGE CALCULATOR======")

Birth_day = int(input("Enter Birth Day: "))
Birth_month = int(input("Enter Birth Month: "))
Birth_year = int(input("Enter Birth Year: "))

today = date.today()

age = today.year - Birth_year

print(f"\n🎂 Your Age is {age} years.")