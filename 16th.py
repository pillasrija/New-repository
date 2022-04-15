s="heLlo WorlD !123"
keys = ["capitals","small","digits","specialcharacters"]
d = dict.fromkeys(keys,0)
print(d)
for character in s:
    if character.isdigit():
        d =["digits"] += 1
    elif character.isupper():
        d =["capitals"] += 1
    elif character.islower():
        d=["small"] += 1
    else:
        d =["special characters"] += 1
print(d)