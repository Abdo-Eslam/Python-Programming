student =[]

for _ in range(int(input("range:"))):
    name = input("name:")
    score = float(input("score:"))
    student.append([name, score])

grades = sorted(set(score for name, score in student))
second_lowest = grades[1]

names = sorted(name for name, score in student if score == second_lowest)

for name in names:
    print(name)
    