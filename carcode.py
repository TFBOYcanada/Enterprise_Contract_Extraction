print("enter the 4 letter car code :")
#c=input()
import  sys
c=sys.argv[1]
b=str(c.upper())  # input the carcode

a="H"
EE=" Elite"
Category={"N":"Mini Elite","E":"Economy"}
Category[a]="Economy"+EE
Cat=["C","D","I","J","S","R","F","G","P","U","L","W","O","X"]
Nam=["compact","compact"+EE,"intermediate","intermediate"+EE,"standard","standard"+EE,"Fullsize","Fullsize"+EE,
     "Premium","Premium"+EE,"Luxury","Luxury"+EE,"Ovrsize","Special"]
for i ,j in zip( Cat, Nam):
    Category[i]=j
ty="B C D W V L S T F J X P Q Z E M R H Y N G K"
Type=ty.split()
tr="M N C A B D"
fu="R N D Q H I E C L S A B M F V Z U X"
Trans=tr.split()
Fuel=fu.split()
Tname="2-3 Door, 2/4 Door,4-5 Door,Wagon/Estate,Passenger Van,Limousine,Sport,Convertible,SUV,Open Air All Terrain,Special,Pick up Regular Cab, Pick up Extened Cab,Special Offer Car,Coupe,Monospace,Recreational Vehicle,Motor Home,2 Whell Vehicle,Roadster,Crossover,Commercial Van/Truck"
Tyn=Tname.split(',')
TD="Manual,Manual 4WD,Manual AWD,Auto,Auto 4WD,Auto AWD"
Trn=TD.split(",")
Fa="Unspecified Fuel with Air,Unspecified Fuel without Air,Diesel Air, Diesel No air,Hybrid Air,Hybrid No Air,Electric Air, Electric No Air,LPG/Compressed Gas air, LPG/Compressed Gas No Air,Hydrogen Air,Hydrogen No Air,Multi Fuel/Power Air,Multi Fuel/Power No Air,Petrol Air,Petrol No Air,Ethanol Air,Ethanol No Air"
Fn=Fa.split(",")
Typed={}
Transd={}
Fueld={}


for i,j in zip(Type,Tyn):
    Typed[i] = j
for i,j in zip(Trans,Trn):
    Transd[i] = j
for i,j in zip(Fuel,Fn):
    Fueld[i] = j
try:
    result=Category[b[0]] +" "+Typed[b[1]]+" | " + Transd[b[2]] +"-"+ Fueld[b[3]]
except:
    result="invalid carcode"
print(result)