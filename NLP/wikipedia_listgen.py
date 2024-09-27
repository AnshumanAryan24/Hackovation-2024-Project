import wikipedia

# for term in wikipedia.search("Compiler Design"):
#     res = wikipedia.summary(term).split()[0:100]
#     print(' '.join(res))

def relateddesc(search_term: str, n_words: int = 100):
    if (n_words < 0):
        n_words = 100
    search_term = "_".join(search_term.split())    
    res_dict = {term: ' '.join(wikipedia.summary(term).split()[0:n_words]) for term in wikipedia.search(search_term)}
    return res_dict

if __name__ == '__main__':
    for key, value in relateddesc("Compiler Design", 20).items():
        print(key, ": ", value)
        print()