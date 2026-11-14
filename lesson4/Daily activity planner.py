homework_time = int(input("Enter your homework time in minutes :"))
if homework_time > 60:
    plan = "start homework now"
    print("That is a long homework session")
else:
    plan = "finish homework quikly"
    print("That is a short homework session")

free_time = input("Is there a free time ? (yes/no) :")
if free_time == "yes":
    print("Remember to pick a hobby")
else:
    print("Continue to your study")

print("")
print("Daily Planner Completed")
print("=========DAILY PLAN=========")
print("Homework Minutes :", homework_time)
print("Plan :", plan)
print("Free Time :", free_time)