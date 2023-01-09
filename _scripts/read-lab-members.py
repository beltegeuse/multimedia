import csv
f = open("List of members - Multimedia Lab - Feuille 1.csv", encoding='utf-8')
reader = csv.DictReader(f)
prof = ""
students = []
team = {}
for r in reader:
    if r["Professors"] != "":
        team[prof] = students
        students = []
        prof = r["Professors"]
        print(prof)
    else:
        students += [r["Students"]]

team[prof] = students
print(team)