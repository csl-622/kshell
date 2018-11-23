import networkx as nx
import matplotlib.pyplot as ply
import random
import numpy as np

def check_existence(H,d):
        f = 0
        for each in H.nodes():
                  if H.degree(each) <= d:
                           f =1
                           break
        return f				      
        
def find(H,it):
       set1=[]
       for each in H.nodes():
                if H.degree(each) <= it :
                            set1.append(each)	
       return set1						

G=nx.Graph() 
G = nx.read_edgelist('graph_name.txt', nodetype = int)
n = len(G.nodes())

print("no of nodes in graph:"+str(n))
t = int(n/100)
N=list(G.nodes())

'''  Finding the buckets '''
H = G.copy()
it = 1
tmp = []
buckets = []
shell_no=[]
while(1):
          flag =check_existence(H, it)
          if flag == 0:
                    it = it+1
                    buckets.append(tmp)
                    tmp = []
          if flag ==1:
                    node_set = find(H,it)
                    for each in node_set:
                             H.remove_node(each)
                             tmp.append(each)
          if H.number_of_nodes() == 0:
                    buckets.append(tmp)
                    break

k=len(buckets)
print("no of shells: "+str(k))
max_shell_no = k
for i in N:
         shell_no.append(i)
                  
for j in range(n):
      for r in range(k):
            p=len(buckets[r])
            for y in range(p):
                  if (N[j] == buckets[r][y]) : shell_no[j] = r+1    			
v = (list)(G.nodes()) 
smallest_paths = []
i=0
j=0
for i in range(len(v)-1):
       for j in range(i+1, len(v)):
             
             if(nx.has_path(G,v[i],v[j]) == True):smallest_paths.append(nx.shortest_path(G,v[i],v[j]))
smallest_paths.sort(key=len)			 

d = len(smallest_paths[len(smallest_paths)-1]) - 1
diameter = []
for i in range(len(smallest_paths) - 1, -1, -1):
      if(len(smallest_paths[i]) == d):diameter.append(smallest_paths[i])
print('diameter length of graph is: '+ str(d) )	  
#print(diameter)	  
diameter_shells = []
i=0
j=0
inner_encountered=[]
for i in range(len(diameter)):
      diameter_shells = []
      number = 0
      for j in range(len(diameter[i])):
            diameter_shells.append(shell_no[diameter[i][j]])
            if(shell_no[diameter[i][j]] == k) : number = number +1
      inner_encountered.append(number)	
      print(i)	
      print(diameter_shells)
      print('no of times diameter innermost shell is : '+str(number))
avg = sum(inner_encountered)/len(inner_encountered)
print(inner_encountered)
print('no of times on an average the diameter encountered the inner shell is : '+str(avg))


