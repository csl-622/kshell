'''
  code for k shell decomposition in a given graph
  print shells of nodes
'''
import networkx as nx
import matplotlib.pyplot as plt


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

	return		


input_graph_file = ""

G = nx.read_edgelist(input_graph_file,create_using=nx.Graph(), nodetype = int)

H = G.copy()

temp = [] # for the currently filled bucket

buckets = [] #list of lists(buckets)

deg = 1 # for degree of nodes

while(1):
	
	count = check(H,deg)

	if count = 1:
		shell_set = find_set(H,deg)
		for j in shell_set:
			H.remove_node(j)
			temp.append(j)

	if count = 0:
		deg = deg +1
		buckets.append(temp)
		temp = [] # start with new temp array


	if H.numbers_of_nodes() == 0:
		buckets.append(temp)
		break
		
print(buckets)
    

