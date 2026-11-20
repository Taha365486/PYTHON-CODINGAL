print("###############################################################")
print("                     WELCOME TO RIDE BUILDER!                  ")
print("###############################################################")
print()

print("STEP1 :Pick your vehicle")
print("1- Bike")
print("2- Car")
print()

choice = int(input("Enter 1 or 2 :"))
print()

if choice == 1:
    print("STEP2 : Pick your bike type")
    print("1- Road Bike")
    print("2- Mountain Bike")
    print()
    bike_type = int(input("Enter 1 or 2 :"))
    print()

    if bike_type == 1:  
        print("You picked  : Scooty")
        print("Speed       : 100km/hr")
        print("Best for    : City Roads")
    else:
        print("You picked  : Dirt Bike")
        print("Speed       : 50km/hr")
        print("Best for    : Off-Road")
elif choice == 2:
    print("STEP3 : Pick your car type")
    print("1- BMW")
    print("2- KIA KERONSE")
    print()
    car_type = int(input("Enter 1 or 2"))
    print()
    if car_type == 1:
        print("You picked : BMW")
        print("Seats      : 4 Passengers")
        print("Best for   : Racing (SPORT CAR)")
    else:
        print("You picked : KIA KERONSE")
        print("Seats      : 7 Passengers")
        print("Best for   : Family trips")
else:
    print("That was not a valid choice")
    print("Please Enter 1 for Bike or 2 for Car")

print()
print("############################################")
print("           YOUR CUSTOM RIDE IS READY!       ")
print("              ENJOY YOUR JOURNEY!           ")
print("############################################")
