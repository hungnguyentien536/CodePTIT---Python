import sys

input = sys.stdin.readline


def normalize(name):
    return ' '.join(word.capitalize() for word in name.split())


n = int(input())
students = []

for i in range(1, n + 1):
    name = normalize(input().strip())
    score = float(input())
    ethnic = input().strip()
    area = input().strip()

    bonus = 0

    if area == '1':
        bonus += 1.5
    elif area == '2':
        bonus += 1

    if ethnic != 'Kinh':
        bonus += 1.5

    total = score + bonus

    status = "Do" if total >= 20.5 else "Truot"

    code = f"TS{i:02d}"

    students.append((code, name, total, status))

students.sort(key=lambda x: (-x[2], x[0]))

for code, name, total, status in students:
    print(code, name, f"{total:.1f}", status)