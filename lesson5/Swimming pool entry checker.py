age = int(input("How old are you :"))
swim = input("Can you swim 25 meteres? (yes/no)").strip().lower()
adult = input("Is anadult with you? (yes/no)").strip().lower()
timing = input("Timing of arriving here is 12pm to 5pm:")

print()
print("====Entry Decision====")
print("-" * 32)
if age < 4:
    print("Age group   :Toddler")
elif age < 12:
    print("Age group   :Child")
elif age < 18:
    print("Age group   :Teen")
else:
    print("Age group   :Adult")

if swim == "yes" and adult == "yes":
    print("Deep pool   :Allowed: you can swim if an adult is with you")
if age < 12 or swim == "no":
    print("Shallow end :Stay in the shallow end today")
if not (adult == "yes"):
    print("Reminder   :No adult with you - Tell the lifeguard")
if swim == "yes" and swim == "no":
    print("Error   :Please answer the swimming question with yes or no")
