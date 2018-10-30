import networkx as nx
import string
import matplotlib.pyplot as plt
import operator
import random

####### H INDEX CALCULATOR
def H_index(degree, H_value_of_neighbours):
	## VARIABLES
	min_h = 0

	for i in range(0,degree,1):
		min_h = i + 1

		if(H_value_of_neighbours[i] < min_h):
			return (min_h - 1)
		elif(H_value_of_neighbours[i] == min_h):
			return min_h

	return min_h

def check(H,deg):
	flag = 0
	for i in H.nodes():
		if H.degree(i) <= deg:
			flag = 1
			break
	return flag		


def find_set(H,deg):
	temp2 = []
	for i in H.nodes():
		if H.degree(i) <= deg:
			temp2.append(i)

	return temp2


############################################################################
#
#
#  START OF MAIN BODY
#
#
############################################################################

## VARIABLES
G = 0
H = 0
temp = []
buckets = []
deg = 1
no_of_Hindex = 4
actual_max_shell = 0
dict_shell = {}
no_run = 30
percent_of_nodes = 1.0
percent_nodes = 0 
current = 0
max_shell = 0
neighbour_max_shell = 0
neighbour_max_shell_value = 0


## ( creating digraph )
G = nx.read_adjlist("DATASET/1/dataset1.txt",create_using=nx.Graph(), nodetype=int)

## ( Updating the variables )
nodes_list = list(G.nodes())
edges_list = list(G.edges())
no_nodes = len(nodes_list)
no_edges = len(edges_list)
percent_nodes = (int)((percent_of_nodes/100.0)*no_nodes)


## ( Creating Dictionary with nodes as keys and its position in list as values )
dict_nodes = {}

for i in range(0,no_nodes,1):
	dict_nodes[nodes_list[i]] = i

## ( Creating a nested list storing node and its consecutive h-index data )
#   Example = [ 24 , 20 , 19 , 18 , 17 , 15 , 13 ]
#	Here : 	24 = Node number
#			20 = h0 index i.e degree
#			19 = h1 index
#			18 = h2 index ....
#			13 = shell number
node_details = [ [nodes_list[i],0,0,0,0,0,0] for i in range(0,no_nodes,1)]

###### CALCULATNG H INDEX OF NODES
for h in range(0,no_of_Hindex+1,1):
	for i in range(0,no_nodes,1):
		neighbours = [m for m in G[node_details[i][0]]]
		degree = len(neighbours)

		if ( h  == 0 ):
			node_details[i][h+1] = degree
		else:
			H_value_of_neighbours = [ 0 for j in neighbours]
			
			for j in range(0,degree,1):
				neighbour_node_no = dict_nodes[neighbours[j]]
				H_value_of_neighbours[j] = node_details[neighbour_node_no][h]

			H_value_of_neighbours = sorted(H_value_of_neighbours,reverse=True)
			
			node_details[i][h+1] = H_index(degree, H_value_of_neighbours)


## ( Creating copy of graph for getting the shell number of nodes )
H = G.copy()

###### CALCULATING SHELL NUMBER OF NODES
while(True):
	count = check(H,deg)
	if ( count == 1 ):
		shell_set = find_set(H,deg)
		for j in shell_set:
			H.remove_node(j)
			temp.append(j)

	if ( count == 0 ):
		deg = deg +1
		buckets.append(temp)
		temp = [] # start with new temp array

	if (len(H.nodes()) == 0):
		buckets.append(temp)
		break

## ( Creating Dictionary with nodes as keys and its shell number as values )
for i in range(0,len(buckets),1):
	for j in buckets[i]:
		node_details[dict_nodes[j]][6] = i+1
		dict_shell[j] = i+1

## ( Displaying the details of nodes in graph )
# print("==========================================")
# for i in node_details:
# 	print(i)
# print("==========================================")


## ( Updating variable and displaying max shell number in graph )
actual_max_shell = len(buckets) + 1
print("ACTUAL MAX SHELL : "+str(actual_max_shell))


###### RANDOM WALK
# print("=========================================")
# print("RANDOM WALK :")
# print("=========================================")

# # ( Random walk main process )
# for i in range(0,no_run,1):
# 	print("--------------------------------------")
# 	print("RUN NO  : "+str(i+1))
# 	current = random.choice(nodes_list)
# 	max_shell = dict_shell[current] + 1

# 	for j in range(1,percent_nodes,1):
# 		print(str(current)+":"+str(dict_shell[current]+1)),
# 		neighbours = [m for m in G[current]]
# 		current = random.choice(neighbours)
# 		if ( max_shell < dict_shell[current] + 1 ):
# 			max_shell = dict_shell[current] + 1
# 		print("->"),
# 	print()
# 	print("MAX SHELL REACHED : "+str(max_shell))

###### HILL CLIMBING
print("=========================================")
print("HILL CLIMBING :")
print("=========================================")

## ( Hill climbing main process )
for i in range(0,no_run,1):
	print("--------------------------------------")
	print("RUN NO  : "+str(i+1))
	current = random.choice(nodes_list)
	max_shell = dict_shell[current] + 1

	for j in range(1,percent_nodes,1):
		print(str(current)+":"+str(dict_shell[current]+1)),
		
		if ( dict_shell[current] + 1 != actual_max_shell ):
			neighbours = [m for m in G[current]]
			neighbour_max_shell = neighbours[0]
			neighbour_max_shell_value = dict_shell[neighbour_max_shell] + 1
			for k in neighbours:
				#print(str(k)+":"+str(dict_shell[k]+1))
				if ( neighbour_max_shell_value < dict_shell[k] + 1 ):
					neighbour_max_shell = k
					neighbour_max_shell_value = dict_shell[k] + 1
		else:
			break

		current = neighbour_max_shell
		if ( max_shell < neighbour_max_shell_value ):
			max_shell = neighbour_max_shell_value
		print("----->"),
	print()
	print("MAX SHELL REACHED : "+str(max_shell))