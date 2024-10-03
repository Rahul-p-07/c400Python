import requests
taxizone=requests.get("https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv",)
#print(taxizone.text)
records=taxizone.text
rec=records.split("\n")[1:266]
file= open("taxi_zone_lookup.txt","w")
x=len(rec)
borough=[]
c=0
for i in rec:
    y=i.split(",")[1]
    if y not in borough:
        borough.append(y)
    if y=='"Brooklyn"':
        c+=1

fin=sorted(borough)
file.write(f'''The total number of records are: {x}
The Unique Boroughs are: {fin}
The Count of Brooklyn borough : {c}''')