name = input("Enter your name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA (0-5): "))
field = input("Enter your field of interest: ")
graduated = input("Have you graduated? (yes or no): ").lower()

print()

if age < 25 and gpa >= 3.5 and graduated == "yes":
    print("You are eligible for a scholarship.")
elif age < 30 and gpa >= 2.5:
    print("You are eligible for an internship.")
else:
    print("You are not eligible, apply again later.")