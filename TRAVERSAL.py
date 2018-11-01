import os

no_of_dataset = 11
percent_node_list = [1,5,10,15]

for i in range(1,no_of_dataset+1,1):
	print("CURRENTLY RUNNING DATASET : "+str(i))
	for j in percent_node_list:
		print("===============> PERCENT NODE : "+str(j))
		os.system("python KSHELL.py "+str(i)+" "+str(j))
print("FINISHED")