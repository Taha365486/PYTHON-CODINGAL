import keyword
#ask three questions
person_name = input("enter your name:")
goal_name = input("enter one skill you want to get better at:")
target_month = input("enter the month you want to reach it by:")
#store practise time
daily_minutes = 30
#print the heading
print("\nMY PERSONAL GOAL PLAN\n")
#print four plan lines
print("Name:", person_name)
print("Goal:", goal_name)
print("Target month", target_month)
print("Daily practise :", daily_minutes, "minutes")
#print two lines that join up 
print("Status:", end="  ")
print("Not started")
print("Reminder:", end=" - ")
print("Practise every day!")
#print the sentence and keywords
print("In one sentence:", person_name, "wants to get better at", goal_name, "By practising", daily_minutes, "minutes every day until", target_month)
#Print Python's reserved word list.
print(keyword.kwlist)