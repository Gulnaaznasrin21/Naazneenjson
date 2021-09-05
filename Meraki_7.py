import json
dic={"Name": "Abhishek","Designation": "CEO of navgurukul","Gender":"male","Age": "29"}
with open("Naaz.json","w") as file:
    json.dump(dic,file,indent=4)
a=json.dumps(dic)
print(dic)