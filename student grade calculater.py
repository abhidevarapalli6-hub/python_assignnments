def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"

n = int(input("Enter number of subjects: "))

total = 0

for i in range(n):
    mark = float(input(f"Enter marks of Subject {i+1}: "))
    total += mark

average = total / n

print("Average =", average)
print("Grade =", calculate_grade(average))
