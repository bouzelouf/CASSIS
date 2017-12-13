import codecs, difflib, Levenshtein, distance

with codecs.open("titles.tvs","r","utf-8") as f:
    title_list = f.read().split("\n")[:-1]




def LD(s, t):
    s = s.split(" ")
    t = t.split(" ")
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1,
               LD(s[:-1], t[:-1]) + cost])
    return res
print(LD("Python", "Peithen"))
