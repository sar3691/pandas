import pandas as pd

#data showing
def show_the_data(pf):
    
    content=[pf.head,pf.tail,pf.info,pf.to_string]
    j=int(input("1,head 2,tail ,3.info,4.show full\n"))
    if j==3 or j==4:print(content[j-1]())
    else:
        try:    
            k=int(input("size"))
            print(content[j-1](k))
        except Exception:
            print(
                content[j-1]())


#fill the data
def fill_the_data(pf):
     edit=[pf.mean,pf.median,pf.mode]#data fill
     x=int(input("choose the edit option \n1.mean\n2.mediam\n3.mode\n"))
     y=edit[x-1]()
     pf.fillna(y,inplace=True)
     print("------------filled--------")
     
#delete the data
def delete_data(pf):
    pf.dropna() #delete empty column
    pf.drop_duplicates() #delete empty data
    print("fixed")
    

#save the data
def save_data(pf):
    ty=int(input("which type to save \n1.csv\n2.json\n"))
    tp=[".csv",".json"]
    na=input("name of the file or location\n")
    save_format[ty-1](na+tp[ty-1])
    print("file saved")

def display(pf):
    print(pf.to_string())    
    

functions=[pd.read_csv,pd.read_json] #open
i=int(input("choose the file formate \n1.csv \n2.json\n"))
a=input("file location\n")
try:
    pf=functions[i-1](a)
except Exception:
    print("wrong location")
    exit()
    
save_format=[pf.to_csv,pf.to_json]#save

#manipulation
while True:
    ar=int(input("1.show\n2.manipulate\n3.remove empty datas and dublicate\n4.preview\n"))


    if ar==1:
        show_the_data(pf)
    elif ar==2:
        fill_the_data(pf)
    elif ar==3:
        delete_data(pf)
    elif ar==4:
        display(pf)
    else:
        break
    
print(pf.to_string())
#save
sa=int(input("do you want save \n1.yes\n2.no\n"))
if sa==1:
    save_data(pf)
else:
    print("canceled")
    
