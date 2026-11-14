print("=========SMART SCHOOL DAY PLANNER=========")
print("Answer your 3 quick questions and I will plan your day! /n")
day = input("What is it ? (monday to sunday)").strip().capitalize()
weather = input("What is your weather ? (sunny/rainy/cloudy)").strip().lower()
homework = input("Is your homework done ? (yes/no)").strip().lower()

print()
print(f"====Your plan for {day}====")
print("-" * 35)

if day in ("Sunday","Saturday"):
    print("Day type  :Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day Type  :First day of the week. Pack your weekly planner")
elif day == "Friday":
    print("Day Type  :Last School day. Return library books today")
elif day in ("Tuessday", "Wednesday", "Thursday"):
    print("Day Type  :Regular scool day. Stay focused")
else:
    print("Day Type  :Do not recognised. Please try again")



if weather == "sunny" and homework == "yes":
    print("After school: Head to the park - great weather and homework is done!")

if weather == "rainy" or weather == "cloudy":
    print("Weather tip : Pack your umbrella - it may get wet outside.")

if not (homework == "yes"):
    print("Homework    : Not done yet. Finish it before going out!")
  
if weather == "rainy" and not (homework == "yes"):
    print("Best plan   : Stay in, finish homework, then watch your favourite show.")
  
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan   : All set for a great school day - you are prepared!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan   : Perfect weekend weather - head outside and have fun!")
else:
    print("Best plan   : Take it one step at a time - you have got this!")

print()
print("Plan complete! Have a wonderful day!")
