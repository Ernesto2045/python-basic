ages = []
age = 0
count = 0

count = int(input("Enter the students count: "))

# loop from 0 to count
for i in range(0, count):
    age = int(input("Enter student age: "))
    ages.append(age)

print("The ages were successfully added to the list.")

sum = 0

# loop from 0 to count
for i in range(0, count):
    sum = sum + ages[i]

print(sum);

average = sum / count

print("The average age is", str(average))


