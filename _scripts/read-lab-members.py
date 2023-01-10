import csv
import codecs 

def translate_cycle(v):
    if v == "3rd":
        return "phd"
    elif v == "2nd":
        return "master"
    else:
        return "other"

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
        students += [(r["Students"], translate_cycle(r["Cycle"]))]

team[prof] = students
for (k, vs) in team.items():
    print(f"**{k}**")
    for v in vs: 
        print(f" - {v}")

import json
def export_list(filename, entries):
    d = {
        "current" : [],
        "past" : []
    }
    for e in entries:
        d["current"] += [{"name" : e[0], "type" : e[1]}]
    json_object = json.dumps(d, indent=4, ensure_ascii=False).encode('utf8')

    with codecs.open(filename, "w", "utf-8") as outfile:
        outfile.write(json_object.decode())

export_list("../content/team/drouin/students.json", team["Simon Drouin"])
export_list("../content/team/mcguffin/students.json", team["Michael McGuffin"])
export_list("../content/team/paquette/students.json", team["Eric Paquette"])
export_list("../content/team/andrews/students.json", team["Sheldon Andrews"])
export_list("../content/team/levesque/students.json", team["Vincent Levesque"])
export_list("../content/team/labbe/students.json", team["David Labbé"])
export_list("../content/team/coulombe/students.json", team["Stephane Coulombe"])
export_list("../content/team/vasquez/students.json", team["Carlos Vazquez"])
export_list("../content/team/gruson/students.json", team["Adrien Gruson"])