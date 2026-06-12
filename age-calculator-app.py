from datetime import date

print("======AGE CALCULATOR======")

Birth_day = int(input("Enter Birth Day: "))
Birth_month = int(input("Enter Birth Month: "))
Birth_year = int(input("Enter Birth Year: "))

if Birth_month < 1 or Birth_month > 12:
    print("Invalid Month")
    exit()
elif Birth_day < 1 or Birth_day > 31:                 # this will handel invalide inputs
    print("Invalid Day")
    exit()
elif Birth_month == 2 and Birth_day > 29:             # this will handel february
    print("Invalid Day for February")
    exit()
elif Birth_month in [4, 6, 9, 11] and Birth_day > 30:
    print("Invalid Day")                                   # this will handel april,june,september,november
    exit()
else:
    print("Valid Input")

today = date.today()

age = today.year - Birth_year

if (today.month, today.day) < (Birth_month, Birth_day): # if birthday not arrived
    age -= 1
next_Birthday = date(today.year, Birth_month, Birth_day)


if next_Birthday < today:                                           #If birthday has already happened:
                                                                    #Next Birthday = Birthday Next Year
                                                                    #Days Left = Next Birthday - Today

    next_Birthday = date(today.year + 1, Birth_month, Birth_day) 
else:

    next_Birthday = date(today.year, Birth_month, Birth_day)       #If birthday has not happened yet:
                                                                   #Days Left = Birthday This Year - Today

Days_left = (next_Birthday - today).days


print(f"\n🎂 Your Age is {age} years.") 

if Days_left == 0:
    print("🎉 Happy Birthday!")
else:
    print(f"🎉 Days until next birthday: {Days_left}")
print(f"📅 Next Birthday: {next_Birthday}")
