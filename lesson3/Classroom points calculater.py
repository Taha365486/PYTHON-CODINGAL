noob1 = 56
noob2 = 70
noob3 = 147
noob4 = 79
noob5 = 120

total = noob1 + noob2 + noob3 + noob4 + noob5
average = total/8

print("Total points  :", total)
print("Average per noobs  :", average)

hakers_per_point = 2
reward_hakers = total*hakers_per_point
print("Total reward hakers  :", reward_hakers)

boxes = reward_hakers//25
leftover = reward_hakers%25

print("Full boxes packed :", boxes)
print("Leftover hakers :", leftover)

last_week = 500
print("Better than last week?  :", total > last_week)
print("Same as last week ?  :", total==last_week)
print("At least as good ?  :", total>=last_week)

total += 25
print("After bonus points :", total)

total -= 15
print("After missed task :", total)

reward_hakers = total*hakers_per_point
boxes = reward_hakers//25

print("Final boxes packed :", boxes)