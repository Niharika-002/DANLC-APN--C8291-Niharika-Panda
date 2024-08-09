# Wap to read age of 15 people and find the number of adults, babies and school age students.

babies = 0
school = 0
adults = 0

for i in range(15):
    a = int(input(f"enter the age {i+1}: "))
    if a >= 18:
        adults += 1
    if a >= 0:
        babies += 1
    if a >= 5:
        school += 1

print("------------")
print(f"Number of adults: {adults}")
print(f"Number of babies: {babies}")
print(f"Number of school-age students: {school}")

