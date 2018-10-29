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
no_of_Hindex = 4

## CREATING DIGRAPH 
G = nx.read_adjlist("facebook_combined.txt",create_using=nx.Graph(), nodetype=int)

nodes_list = list(G.nodes())
edges_list = list(G.edges())
no_nodes = len(nodes_list)
no_edges = len(edges_list)

## CREATING A DICTIONARY FOR NODES AND POSITION
dict_nodes = {}

for i in range(0,no_nodes,1):
	dict_nodes[nodes_list[i]] = i

node_details = [ [nodes_list[i],0,0,0,0,0,0] for i in range(0,no_nodes,1)]


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


##### GETTING THE SHELL NUMBER OF THE NODES
H = G.copy()

temp = [] # for the currently filled bucket
buckets = [] #list of lists(buckets)
deg = 1 # for degree of nodes

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

#####
dict_shell = {}

for i in range(0,len(buckets),1):
	for j in buckets[i]:
		node_details[dict_nodes[j]][6] = i+1
		dict_shell[j] = i+1

# print("==========================================")
# for i in node_details:
# 	print(i)
# print("==========================================")


###### RANDOM WALK

## VARIABLES
no_run = 30
percent_of_nodes = 1.0
percent_nodes = (int)((percent_of_nodes/100.0)*no_nodes)
current = 0
max_shell = 0

print("ACTUAL MAX SHELL : "+str(len(buckets)+1))
for i in range(0,no_run,1):
	print("==================================")
	print("RUN NO  : "+str(i+1))
	current = random.choice(nodes_list)
	max_shell = dict_shell[current] + 1

	for j in range(1,percent_nodes,1):
		print(str(current)+":"+str(dict_shell[current])),
		neighbours = [m for m in G[current]]
		current = random.choice(neighbours)
		if ( max_shell < dict_shell[current] + 1 ):
			max_shell = dict_shell[current] + 1
		print("->"),
	print()
	print("MAX SHELL REACHED : "+str(max_shell))