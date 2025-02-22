import networkx as nx
import string
import matplotlib.pyplot as plt
import operator
import random
import sys

############################################################################
#
#
#  FUNCTIONS
#
#
############################################################################

###### H INDEX CALCULATOR
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

###### CHECK FOR NODES LESS THAN DEGREE
def check(H,deg):
	flag = 0
	for i in H.nodes():
		if H.degree(i) <= deg:
			flag = 1
			break
	return flag		

###### FIND SET OF NODES WITH LESS DEGREE
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

## CHOICES
dataset_value = sys.argv[1]
percent_of_nodes = float(sys.argv[2])
part_1 = int(sys.argv[3])
part_2 = int(sys.argv[4])

## VARIABLES
G = 0						# Graph G
H = 0						# Copy of Graph G
no_nodes = 0				# No of nodes in Graph G
no_edges = 0				# No of edges in Graph G
nodes_list = []				# A list of all nodes in Graph
edges_list = []				# A list of all edges in Graph
dict_nodes = {}				# A dictionary with Keys : Nodes ; Values : Nodes position in list (nodes_list)
node_details = []			# A nested list storing node and its consecutive h-index data

temp = []
buckets = []
deg = 1
no_of_Hindex = 4
actual_max_shell = 0
dict_shell = {}
dict_nodes_visited = {}
no_run = 30
percent_nodes = 0 

current = 0
max_shell = 0



## ( creating digraph )
G = nx.read_adjlist("DATASET/"+dataset_value+"/dataset"+dataset_value+".txt",create_using=nx.Graph(), nodetype=int)

## ( updating files )
file_node_details = open("OUTPUT/"+dataset_value+"/node_details_"+dataset_value+".txt",'w+')
file_random_walk = open("OUTPUT/"+dataset_value+"/random_walk_"+dataset_value+"_"+str(sys.argv[2])+".txt",'w+')
file_hill_climbing_1 = open("OUTPUT/"+dataset_value+"/hill_climbing_1_"+dataset_value+".txt",'w+')
file_hill_climbing_2 = open("OUTPUT/"+dataset_value+"/hill_climbing_2_"+dataset_value+".txt",'w+')

## ( Updating the variables )
nodes_list = list(G.nodes())
edges_list = list(G.edges())
no_nodes = len(nodes_list)
no_edges = len(edges_list)
percent_nodes = (int)((percent_of_nodes/100.0)*no_nodes)


## ( Updating dictionary : dict_nodes i.e. A Dictionary with Keys : nodes; Values : nodes position )
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
file_node_details.write("==========================================\n")
for i in node_details:
	for j in range(0,len(i),1):
		file_node_details.write(str(i[j])+"\t")
	file_node_details.write("\n")
file_node_details.write("==========================================\n")


## ( Updating variable and displaying max shell number in graph )
actual_max_shell = len(buckets) + 1
file_random_walk.write("ACTUAL MAX SHELL : "+str(actual_max_shell)+"\n")
file_hill_climbing_1.write("ACTUAL MAX SHELL : "+str(actual_max_shell)+"\n")
file_hill_climbing_2.write("ACTUAL MAX SHELL : "+str(actual_max_shell)+"\n")



#######################################################################################################
#######################################################################################################



## VARIABLES
distinct_shell = []
total_no_distinct_shell = 0


###### RANDOM WALK
if (part_1 == 1):
	file_random_walk.write("=========================================\n")
	file_random_walk.write("RANDOM WALK :\n")
	file_random_walk.write("=========================================\n")

	## ( Random walk main process )
	for i in range(0,no_run,1):
		file_random_walk.write("--------------------------------------\n")
		file_random_walk.write("RUN NO  : "+str(i+1)+"\n")
		
		current = random.choice(buckets[0])
		max_shell = dict_shell[current] + 1
		distinct_shell = []

		for j in range(1,percent_nodes,1):
			file_random_walk.write(str(current)+":"+str(dict_shell[current]+1))
			if (dict_shell[current]+1) not in distinct_shell:
				distinct_shell.append((dict_shell[current]+1))

			neighbours = [m for m in G[current]]
			current = random.choice(neighbours)
			if ( max_shell < dict_shell[current] + 1 ):
				max_shell = dict_shell[current] + 1
			file_random_walk.write("->")

		total_no_distinct_shell = total_no_distinct_shell + len(distinct_shell)

		file_random_walk.write("\n")
		file_random_walk.write("MAX SHELL REACHED : "+str(max_shell)+"\n")
		file_random_walk.write("DISTINCT SHELLS : ")

		for k in distinct_shell:
			file_random_walk.write(str(k)+" : ")
		
		file_random_walk.write("\n")
	file_random_walk.write("++++++++++++++++++++++++++++++++++++++++\n")
	file_random_walk.write("AVERAGE DISTINCT SHELLS : "+str((float)(total_no_distinct_shell)/(float)(no_run))+"\n")



#######################################################################################################
#######################################################################################################




## VARIABLES
neighbour_max_h = []
neighbour_max_h_value = 0
h_index_compare = 2
neighbour_h = 0
neighbour_least_travelled = 0
node_least_visited = 0

###### HILL CLIMBING
if (part_2 == 1):

	###################################################################################
	## ( travelling least traveled maximum shell )
	file_hill_climbing_1.write("=========================================\n")
	file_hill_climbing_1.write("HILL CLIMBING 1 :\n")
	file_hill_climbing_1.write("=========================================\n")

	## ( Hill climbing main process )
	for i in range(0,no_run,1):
		dict_nodes_visited = {}

		for j in nodes_list:
			dict_nodes_visited[j] = 0

		file_hill_climbing_1.write("--------------------------------------\n")
		file_hill_climbing_1.write("RUN NO  : "+str(i+1)+"\n")
		current = random.choice(buckets[0])
		max_shell = dict_shell[current] + 1
		
		while(True):
			file_hill_climbing_1.write(str(current)+":"+str(dict_shell[current]+1))
			if ( dict_shell[current] + 1 == actual_max_shell ):
				break

			dict_nodes_visited[current] = ((int)(dict_nodes_visited[current])) + 1
			neighbours = [m for m in G[current]]

			neighbour_max_h = []
			neighbour_max_h_value = node_details[dict_nodes[neighbours[0]]][h_index_compare]
			
			for k in neighbours:
				if ( neighbour_max_h_value < node_details[dict_nodes[k]][h_index_compare]):
					neighbour_max_h_value = node_details[dict_nodes[k]][h_index_compare]

			for k in neighbours:
				if ( neighbour_max_h_value == node_details[dict_nodes[k]][h_index_compare]):
					neighbour_max_h.append(k)

			node_least_visited = neighbour_max_h[0]

			for k in neighbour_max_h:
				if ( dict_nodes_visited[k] < dict_nodes_visited[node_least_visited] ):
					node_least_visited = k

			current = node_least_visited
			if ( max_shell < dict_shell[current] + 1 ):
				max_shell = dict_shell[current] + 1
			file_hill_climbing_1.write("----->")

		file_hill_climbing_1.write("\n")
		file_hill_climbing_1.write("MAX SHELL REACHED : "+str(max_shell)+"\n")


	###################################################################################
	## ( Travelling node not travelled )
	file_hill_climbing_2.write("=========================================\n")
	file_hill_climbing_2.write("HILL CLIMBING 2 :\n")
	file_hill_climbing_2.write("=========================================\n")

	## ( Hill climbing main process )
	for i in range(0,no_run,1):
		dict_nodes_visited = {}

		for j in nodes_list:
			dict_nodes_visited[j] = 0

		file_hill_climbing_2.write("--------------------------------------\n")
		file_hill_climbing_2.write("RUN NO  : "+str(i+1)+"\n")
		

		current = random.choice(buckets[0]) 
		max_shell = dict_shell[current] + 1
		
		while(True):
			file_hill_climbing_2.write(str(current)+":"+str(dict_shell[current]+1))

			if ( dict_shell[current] + 1 == actual_max_shell ):
				break


			dict_nodes_visited[current] = ((int)(dict_nodes_visited[current])) + 1
			neighbours = [m for m in G[current]]

			neighbour_least_travelled = neighbours[0]
			neighbour_h = node_details[dict_nodes[neighbours[0]]][h_index_compare]

			for k in neighbours:
				if ( dict_nodes_visited[neighbour_least_travelled] < dict_nodes_visited[k] ):
					neighbour_least_travelled = k
				elif ( dict_nodes_visited[neighbour_least_travelled] == dict_nodes_visited[k] ):
					if ( neighbour_h < node_details[dict_nodes[k]][h_index_compare] ):
						neighbour_least_travelled = k

			current = neighbour_least_travelled
			if ( max_shell < dict_shell[current] + 1 ):
				max_shell = dict_shell[current] + 1
			file_hill_climbing_2.write("----->")

		file_hill_climbing_2.write("\n")
		file_hill_climbing_2.write("MAX SHELL REACHED : "+str(max_shell)+"\n")

	file_node_details.close()
	file_random_walk.close()
	file_hill_climbing_2.close()



#######################################################################################################
#######################################################################################################