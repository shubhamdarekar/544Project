cipher = "The quick brown fox jumps over the lazy dog"
plain = "rvn wxolz mtauy had qxkif aent rvn jbpg cas"
key = dict()

for i in range(len(cipher)):
    key[plain[i].lower()] = cipher[i].lower()

print(key)

key2 = {"A":"R", "B":"V", "C":"M", "D":"B", "E":"X", "F":"N", "G":"C", "H":"U", "I":"K", "J":"P", "K":"S", "L":"T", "M":"A", "N":"Y", "O":"H", "P":"Q", "Q":"I", "R":"F", "S":"E", "T":"J", "U":"W", "V":"Z", "W":"L", "X":"D", "Y":"O", "Z":"G"}

print(key2)

total = 0
for i in key.keys():
    og = key[i]

    pred = key2.get(i.upper(),"").lower()

    if og == pred:
        total+=1

print("Correct substitutions: ", total,"/",len(key)," = ", total/len(key))
