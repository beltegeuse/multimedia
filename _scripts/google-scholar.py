
from scholarly import scholarly, ProxyGenerator
import argparse

def get_all_pubs(id):
    # Retrieve the author's data, fill-in, and print
    # Get an iterator for the author results
    first_author_result = scholarly.search_author_id(id)
    print(first_author_result["name"])
    print(first_author_result["affiliation"])

    # Retrieve all the details for the author
    author = scholarly.fill(first_author_result )
    
    pubs = [pub['bib'] for pub in author['publications']]
    return pubs


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="id of the author to get list of publications")
    parser.add_argument("--output", help="output bib file", default="")
    args = parser.parse_args()
    
    pg = ProxyGenerator()
    success = pg.FreeProxies()
    scholarly.use_proxy(pg)
    
    pubs = get_all_pubs(args.id)
    print("Titles:")
    for pub in pubs:
        print(" - ", pub)

    if args.output != "":
        f = open(args.output, "w")
        for pub in pubs:
            print("Get: ", pub["title"])
            q = scholarly.search_pubs(pub["title"])
            pub = next(q)
            bib = scholarly.bibtex(pub)
            print(bib)
            f.write(str(bib))
            f.write("\n")
            f.flush()
                    
           
        f.close()