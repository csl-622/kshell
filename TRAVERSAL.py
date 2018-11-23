import os

no_of_dataset = 1
percent_node_list = [1]
part_1 = 0
part_2 = 0
part_3 = 1


for i in range(1,no_of_dataset+1,1):
	print("CURRENTLY RUNNING DATASET : "+str(i))
	for j in percent_node_list:
		print("===============> PERCENT NODE : "+str(j))
		os.system("python KSHELL.py "+str(i)+" "+str(j)+" "+str(part_1)+" "+str(part_2)+" "+str(part_3))

print("FINISHED")