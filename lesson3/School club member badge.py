member_name = input("enter member name :")
club_name = input("enter club name :")

member_number = 8
points = 9.5
is_active = True

print(member_number , type(member_number))
print(points , type(points))
print(is_active , type(is_active))

badge_code = member_name[:3]
club_name[-1] + str(member_number)

print("Badge code :", badge_code)

print("")
print("=========CLUB BADGE=========")
print("Member :" + member_name)
print("Club :" + club_name)
print("Code :" + badge_code)
print("Points | Active :" + str(points) + " | " + str(is_active))