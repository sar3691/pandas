import pandas as pd
a=input("enter the location")
functions=[pd.read_csv,pd.read_json]
i=int(input("1.csv \n2.json"))

pf=functions[i-1](a)
content=[pf.head,pf.tail,pf.info]
j=int(input("1,head 2,tail ,3.info"))
if j==3:print(content[j-1])
else:
    try:    
        k=int(input("size"))
        print(content[j-1](k))
    except Exception:
        print(content[j-1]())




