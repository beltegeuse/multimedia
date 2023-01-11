import json
import requests
from pylatexenc.latex2text import LatexNodes2Text

def get_content(url):
    response = requests.get(url)
    return response.text



if __name__=="__main__":
    profs = json.load(open("ets-bib.json", "r"))
    for p in profs["profs"]:
        print(f"Retrive: {p['file']}")
        content = get_content(p["url"])    
        #content = LatexNodes2Text().latex_to_text(content)
        f = open(p["file"], "w", encoding="utf8")
        f.write(content)
