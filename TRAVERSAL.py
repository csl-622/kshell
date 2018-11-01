import os

no_of_dataset = 11

for i in range(1,no_of_dataset+1,1):
	print("CURRENTLY RUNNING DATASET : "+str(i))
	os.system("python KSHELL.py "+str(i))
print("FINISHED")