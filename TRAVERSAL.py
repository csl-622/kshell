import os

no_of_dataset = 11
percent_node_list = [1,5,10,15]
part_1 = 0
part_2 = 0


for i in range(1,no_of_dataset+1,1):
	print("CURRENTLY RUNNING DATASET : "+str(i))

	part_1 = 1
	part_2 = 0

	for j in percent_node_list:
		print("===============> PERCENT NODE : "+str(j))
		os.system("python KSHELL.py "+str(i)+" "+str(j)+" "+str(part_1)+" "+str(part_2))

	part_1 = 0
	part_2 = 1
	os.system("python KSHELL.py "+str(i)+" "+str(0)+" "+str(part_1)+" "+str(part_2))

print("FINISHED")