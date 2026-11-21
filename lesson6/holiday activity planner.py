print("====================================")
print("    Welcome to Holiday Planner!     ")
print("====================================")
print()
 
print("Step 1: Pick your holiday type")
print("  1 - Dream holiday")
print("  2 - Nature trip")
print()
 
choice = int(input("Enter 1 or 2: "))
print()
 
if choice == 1:
    print("Step 2: Pick your Dream activity")
    print("  1 - Kashmir's Snowy Mountains")
    print("  2 - Kashmir's Beeautiful Lakes")
    print()
 
    dream_activity = int(input("Enter 1 or 2: "))
    print()
 
    if dream_activity == 1:
        print("You picked  : Kashmir's Snowy Mountains")
        print("Best time   : Morning")
        print("Remember    : Wearing Jackets and Carring Hotwater")
    else:
        print("You picked  : Kashmir's Beautiful Lakes")
        print("Best time   : Evening")
        print("Remember    : Carry Ice Skates,Helmet,Gloves and Thicksocks")
 
elif choice == 2:
    print("Step 2: Pick your Nature activity")
    print("  1 - Strawberries")
    print("  2 - Waterfalls")
    print()
 
    nature_activity = int(input("Enter 1 or 2: "))
    print()
 
    if nature_activity == 1:
        print("You picked  : Mahabaleshwar's Strawberies")
        print("Best for    : Strawberry picking and Farm visits")
        print("Remember    : Carring a Basket Wear comfortable shoes")
    else:
        print("You picked  : Mahabaleshwar Waterfalls")
        print("Best for    : Sightseeing and Enjoyement nature")
        print("Remember    : Wear non-slip shoes and Carry a raincoat")
 
else:
    print("That was not a valid choice.")
    print("Please enter 1 for Dream Holiday or 2 for Nature Trip.")
 
print()
print("====================================")
print("   Your holiday plan is ready!      ")
print("   Enjoy your trip!                 ")
print("====================================")
