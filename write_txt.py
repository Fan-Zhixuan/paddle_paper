import random
a=range(0,145981)
b=random.sample(a,29196)
b = sorted(b)
with open("val.txt","w") as f:
    for i in a:
        if i in b:
            f.write('images/T'+str(i).zfill(6)+'.jpg labels/T'+str(i).zfill(6)+'.png\n')
f.close
with open("train.txt","w") as f:
    for i in a:
        if i not in b:
            f.write('images/T'+str(i).zfill(6)+'.jpg labels/T'+str(i).zfill(6)+'.png\n')
f.close