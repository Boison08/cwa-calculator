import math

courses: dict = {}
w_avg: int = 0
credit: int = 0

while True:
    try:
        count = int(input("How many courses do you do? "))
    except ValueError:
        print("Don't try me!\n")

for i in range(count):
    course = input(f"\n{i+1}. Enter your course, credit and score in this format: [Eg. Twi 2 73]\n")
    list = course.split()
    marks = [int(x) for x in list[-2:]]
    courses[" ".join(list[:-2])] = marks
    
print()     # empty line

for k,v in courses.items():
    w_avg += math.prod(v)
    credit += v[0]
    print( f"{k}: {v[0]} {v[1]}")

swa = w_avg / credit
print(f"\nTotal credits: {credit}, Weighted marks: {w_avg}\nCWA: {round(swa, 2)}")