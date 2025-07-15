def get_words(content):
    words = content.split()
    maybe = len(words)
    print(f"Found {maybe} total words")
    print("--------- Character Count -------")

def get_characters(content):
    how_many = {}
    lowers = content.lower()
    for l in lowers:
        if l not in how_many:
            how_many[l] = 1
        else:
            how_many[l] += 1
    sort_characters(how_many)

def sort_characters(how_many):
    final = []
    for t in how_many.items():
        dic = {}
        dic["char"] = t[0]
        dic["num"] = t[1]
        final.append(dic)
    final.sort(key=sort_on, reverse=True)

    for f in final:
        t = f["char"]
        if t.isalpha():
            print(f"{t}: {f['num']}")
    print("============= END ===============")

def sort_on(item):
    return item["num"]



