tempreture = int(input("enter today's tempreture in celcius:"))
if tempreture < 20:
    outfit = "Jacket"
    print("It is cold today")
    print("Wear a", outfit)
else:
    outfit = "T-shirt"
    print("It is warm today")
    print("Wear a", outfit)

is_raining = input("Is it raining today ? (yes/no) :")
if is_raining == "yes":
    print("Bring an Umbrella")

wind_speed = int(input("enter the wind_speed in km/h :"))
if wind_speed > 30:
    needs_windbreaker = "yes"
    print("It is windy today")
    print("Wear a windbreaker over you", outfit)
else:
    needs_windbreaker = "no"
    print("It is calm today")
    print("No need to wear a windbreaker over you", outfit)

has_puddles = input("Are these puddles left on the ground (yes/no):")
if has_puddles == "yes":
    shoes = "Boots"
    print("It is wet today")
    print("Wear a", shoes)
else:
    shoes ="sneakers"
    print("It is Dry today")
    print("Wear a", shoes)

print("")
print("Weather Check Complete")
print("=======WEATHER OUTFIT=======")
print("Tempreture", tempreture)
print("Outfit Chosen", outfit)
print("Raining", is_raining)
print("Windbreaker Needed",needs_windbreaker)
print("Shoes Chosen", shoes)
print("=======THANK YOU=======")