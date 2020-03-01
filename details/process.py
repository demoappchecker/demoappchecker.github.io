fin = open("data.txt","r")
print("{ \"jewllery\" : [",end="") 
for data in fin.readlines():
	d1 = data.replace("\n","").split(",")
	print("{ \"name\" : \""+d1[0]+"\", \"type1\" : \""+d1[1]+"\", \"type2\" : \""+d1[2]+"\", \"height\" : "+d1[3]+", \"width\" : "+d1[4]+", \"price\" : \""+d1[5]+"\" },",end="")
print("] }")
fin.close()