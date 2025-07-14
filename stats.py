def get_words(content):
    words = content.split()
    maybe = len(words)
    print(f"{maybe} words found in the document.")

def get_characters(content):
    how_many = {}
    lowers = content.lower()
    for l in lowers:
        if l not in how_many:
            how_many[l] = 1
        else:
            how_many[l] += 1
    print(how_many)
