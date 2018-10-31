mesin =[[1,0,0,1,1,0,1],[1,0,1,0,1,0,1],[1,0,0,1,1,1,1],[0,0,0,1,1,0,1],[1,1,0,0,1,1,1]]

true = []
false = []
for i in range(len(mesin)):
	for j in range(len(mesin[i])):
		if mesin[i][j] == 0:
			true.append(mesin[i][j])
		else:
			false.append(mesin[i][j])
print("Banyak data True adalah: "+str(len(true)))
print("Banyak data False adalah: "+str(len(false)))