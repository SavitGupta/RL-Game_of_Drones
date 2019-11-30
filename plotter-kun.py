import matplotlib.pyplot as plt 
import os

l =os.listdir("../../AirSim_qualification/AirSimExe/Saved/Logs/RaceLogs/")
l.sort()

completion = []

for i in l:
# if i > "29-11-2019-19_37":
	f = open("../../AirSim_qualification/AirSimExe/Saved/Logs/RaceLogs/"+i,"r+")
	time = -1
	coll = 0
	for line in f:
		if "drone_1" in line and "penalty" in line:
			coll = int(line.split(" ")[-1])
		if "drone_1" in line and "finished" in line:
			time = int(line.split(" ")[2])
			break

	if time>=0:
		time = time +coll
		completion.append(time/1000.)


# print(completion)

plt.plot(completion)
plt.show()



 
# f = open("log 1575022226.355642.txt","r+")

# for l in f:
# 	print(l)