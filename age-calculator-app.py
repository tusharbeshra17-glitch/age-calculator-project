from datetime import date

print("\n")
print("╔══════════════════════════════════════╗")
print("║           🎂 AGE CALCULATOR          ║")
print("╚══════════════════════════════════════╝")

Birth_day = int(input("Enter Birth Day: "))
Birth_month = int(input("Enter Birth Month: "))
Birth_year = int(input("Enter Birth Year: "))

today = date.today()

age = today.year - Birth_year

print("\n")
print(" ╔══════════════════════════════════════╗")
print(" ║              RESULT                  ║")
print(" ╠══════════════════════════════════════╣")
print(f"║  🎉 Your Age is : {age} Years        ║")       
print(" ╚══════════════════════════════════════╝")

print("\n✨ Thank You For Using Age Calculator ✨")