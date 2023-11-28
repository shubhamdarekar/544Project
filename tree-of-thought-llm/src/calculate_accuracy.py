cipher = "DROBO HGC YXKO EZYX G DSWO G PSCROBWGX VSFOM HSDR RSC HSPO SX G ZSQCDLO KVYCO IL DRO COG GXM OFOBL MGL RO HOXD YED PSCRSXQ GXM RO PSCROM GXM RO PSCROM GXM YXKO RO HGC CSDDSXQ HSDR RSC BYM VYYUSXQ GD DRO KVOGB HGDOB GXM RO CGD GXM RO CGD DROX RSC VSXO CEMMOXVL HOXD MYHX PGB MYHX IOVYH GXM HROX RO MBOH SD EZ GQGSX RO IBYEQRD YED G VGBQO PVYEXMOB"
plain = "there was once upon a time a fisherman lived with his wife in a pigstye close by the sea and every day he went out fishing and he fished and he fished and once he was sitting with his rod looking at the clear water and he sat and he sat then his line suddenly went down far down below and when he drew it up again he brought out a large flounder"

key = dict()

for i in range(len(cipher)):
    key[plain[i].lower()] = cipher[i].lower()

print(key)

key2 = {"A": "S", "B": "R", "C": "P", "D": "O", "E": "X", "F": "C", "G": "Y", "H": "G", "I": "F", "J": "M", "K": "V", "L": "N", "M": "T", "N": "U", "O": "I", "P": "A", "Q": "B", "R": "D", "S": "W", "T": "E", "U": "H", "V": "K", "W": "Q", "X": "Z", "Y": "L", "Z": "J"}

print(key2)

total = 0
for i in key.keys():
    og = key[i]

    pred = key2.get(i.lower(),"")

    if og == pred:
        total+=1

print("Correct substitutions: ", total,"/",len(key)," = ", total/len(key))
