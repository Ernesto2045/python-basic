'''
There are x students in your classroom. 
You want code a program to get from the user:
- School name
- Scholar year
- Students count

For each student, we want to store their:
- Full name
- Age
- Latest score in Math test


The program should have the following output:

'The current school year for <SCHOOL_NAME> is <SCHOLAR_YEAR>'
'The average Math score is:' <AVERAGE_GRADE>

BONUS:
'The maximum score was <MAX_SCORE>

Ex: 
The current school year for Cypress Park HS is 2024
The average Math score is 92.0
The maximum score was 99.6
'''

print("Hi, this is a website for you teachers")
school_name=(input("School's name: "))
grade=(input("Student's school grade: "))
students_count=int(input("Amount of students: "))

print("School's name:", school_name, "\nGrade:", grade, "\nAmount of students:", students_count)

sum_score = 0
names = []
ages = []
scores = []
max_score = 0
max_score_index = -1

for i in range(0,students_count):
    name = input("Full name of Student: ")
    names.append(name)
    
    age=input("Age of Student: ")
    ages.append(age)
    
    score=int(input("Latest Score in Math test: "))
    scores.append(score)
    if scores[i] > max_score:
        max_score = scores[i]
        max_score_index = i
    sum_score += score
    # print( name ,"information:", "\nAge:", age, "\nScore:", score)
    
average_score = sum_score / students_count
print("Average Score:",average_score)

# Print the max score student's: name, age, grade
print("Best grade: ", max_score)
print("Name:" , names[max_score_index], "\nAge:", ages[max_score_index], "\nScore:", scores[max_score_index])
