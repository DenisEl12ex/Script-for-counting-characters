def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

file = open("newfile.txt", "w")
file.write("""Wdskcsv jvnkj snvknv fvfsvnsvs
ayiturujej ppcpooii epoddckssc ikdkdw fwfop.
Fhhwds skwmw nebe amayu ioaa edededfef.
Ioofmffm sasff cnvn polokc wdwdwdwedf
ededejfn opode. Lwnnee zmxnc ewe nertt joi 
fafafsx!""")
file.close()
filename = "newfile.txt"
with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))