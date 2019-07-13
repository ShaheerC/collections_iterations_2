#EXERCISE 9
print("===START OF EXERCISE 9===")

#9.1
grocery_list = ["carrots", "toilet paper", "apples", "salmon",]
for item in grocery_list:
    print("* {}".format(item))

#9.1.2
def function_grocery_list (food):
    for item in food:
        print("* {}".format(item))

grocery_list.append("rice")

function_grocery_list(grocery_list)

#9.2
print(len(grocery_list))

#9.3
if "bananas" in grocery_list:
    print("You need to pick up bananas.")
else: 
    print("You don't need to pick up bananas today.")

#9.4
print(grocery_list[1])

#9.5
grocery_list.sort()
function_grocery_list(grocery_list)

#9.6
grocery_list.pop(3)
function_grocery_list(grocery_list)

#EXERCISE 10
print("===START OF EXERCISE 10===")

#10.1
students = {
    "cohort1" : 34,
    "cohort2" : 42,
    "cohort3" : 22
}

#10.2
def student_display(cohort_num):
    for cohort, student in cohort_num.items():
        print("{}: {} students".format(cohort, student))

student_display(students)

#10.3
students ["cohort4"] = 43
student_display(students)

#10.4
print(students.keys())

#10.5
students = {cohort: student * 1.05 for cohort, student in students.items()}
student_display(students)

#10.6
students.pop("cohort2")
student_display(students)

#10.7
totalstudents = 0
for student in students.values():
    totalstudents += student
print(totalstudents)