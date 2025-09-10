
inp = open('input.txt', 'r', encoding="utf-8")
outp = open('output.txt', 'w', encoding="utf-8")
strng, wrds = [], set()
s = (inp.readline()).rstrip()
while len(s) > 0:
    strng = list(s.split(' '))
    s = (inp.readline()).rstrip()
    for elem in strng:
        wrds.add(elem)
outp.write(str(len(wrds)))
inp.close()
outp.close()

