days = int(input())

people_who_liked_advertise = 2
current_people_reached = people_who_liked_advertise

for i in range(1, days):
    current_people_reached = (current_people_reached * 3) // 2
    people_who_liked_advertise += current_people_reached

print(people_who_liked_advertise)
