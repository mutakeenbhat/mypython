name={'ahraaz':25,'muta':22,'azra':25,'gazala':24,'kuttu':2,'sobaan':5,'aleem':26}
#age={25,24,25,24,2,6,26}
#data=dict(zip(name,age))

#for key,value in name.items():
    #print(key,":",value)
for key in name:
    print(key)
for value in name.values():
    print(value)
for key in sorted(name):
    print(key, ":", name[key])
