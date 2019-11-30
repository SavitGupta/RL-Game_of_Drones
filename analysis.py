import os
import glob 
import matplotlib.pyplot as plt

list_of_files = glob.glob('/home/iiitd/Downloads/log*') 
latest_file = max(list_of_files, key=os.path.getctime)
latest_file = "/home/iiitd/Downloads/log-lstm.txt"
f = open(latest_file)

rewards = []
rew_per_ep = []
q1=[]
q2=[]
critic_loss=[]
actor_loss=[]

for line in f:
	first,sec = line.rstrip().split(' ')
	sec=float(sec)
	if(first == "r"):
		rewards.append(sec)
	elif(first=="E"):
		rew_per_ep.append(sec)
	elif(first=="Q1"):
		q1.append(sec)
	elif(first=="Q2"):
		q2.append(sec)
	elif(first=="CL"):
		critic_loss.append(sec)
	elif(first=="AL"):
		actor_loss.append(sec)
	else:
		print("err")

def smooth(lis,n):
	sm_lis = []
	avg=0
	i=0
	for elem in lis:
		i+=1
		if(i<=n):
			avg = avg*(i-1)+elem
			avg/=i
		else:
			avg = avg*n - lis[i-n] + elem
			avg/=n
		sm_lis.append(avg)
	return sm_lis


def my_plot(lis,n):
	ysmoothed = smooth(lis,n)
	plt.plot(ysmoothed)
	plt.show()

