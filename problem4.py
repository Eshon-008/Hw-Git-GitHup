import json

with open("student.json", "r", encoding="utf-8") as f:
    students = json.load(f)

best = max(students, key=lambda s: s["grade"])

worst = min(students, key=lambda s: s["grade"])

average = round(sum(s["grade"] for s in students) / len(students), 1)

print(f"Eng yaxshi talaba: {best['name']} — {best['grade']}")
print(f"Eng past baho: {worst['name']} — {worst['grade']}")
print(f"O'rtacha baho: {average}")