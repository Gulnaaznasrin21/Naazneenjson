a=["neelam","programer","24","2400"]
p=["komal","trainer","24","20000"]
k=["anuradha","HR","25","40000"]
c=["Abhishek","manager","29","63000"]
b=["name","designation","age","salary"]
dict1={}
dict2={}
dict3={}
dict4={}
dict5={}

i=0
while i<len(a):
    dict1[b[i]]=a[i]
    dict2[b[i]]=p[i]
    dict3[b[i]]=k[i]
    dict4[b[i]]=c[i]
    i+=1
dict5["emp1"]=dict1
dict5["emp2"]=dict2
dict5["emp3"]=dict3
dict5["emp4"]=dict4

print(dict5)