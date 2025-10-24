def count_alpha(fname):
    c = [0]*26
    with open(fname) as f:
        for ch in f.read().lower():
            if 'a' <= ch <= 'z': c[ord(ch)-97] += 1
    for i,v in enumerate(c):
        print(chr(97+i), ":", v)

count_alpha('yourfile.txt')
