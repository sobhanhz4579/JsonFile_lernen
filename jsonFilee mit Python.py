import json



with open("jsf.json","r+") as json_file:
    j=json.load(json_file)



userName=input("Enter userName:")

jj=j.keys()

if userName in jj:
    print(j.values())
else:
    password=input("Enter pass:")
    dNeu2={userName:{"password":password}}

    with open("jsf.json",'a') as json_file:
        ww=json.dump(dNeu2,json_file,indent=4)





