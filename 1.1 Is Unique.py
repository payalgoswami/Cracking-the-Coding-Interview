s=input()
d={}
for i in s:
    if i in d: 
        print("Not unique")
        break
    else: 
        d[i]=1
else:
    print("unique")
tewst
