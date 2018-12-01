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
G = nx.read_edgelist('email-Eu-Core.txt', nodetype = int)
n = len(G.nodes())

print("no of nodes in graph:"+str(n))
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
for w in range(n):
      shell_no.append(0)
k=len(buckets)
print("no of shells: "+str(k))
maximum = k-1
j=0
r=0
smallest_paths = []                  
for j in range(len(N)):
      for r in range(k):
            if(N[j] in buckets[r]):shell_no[j] = r 

for i in range(len(N)-1):
       for j in range(i+1, len(N)):
             
             if(nx.has_path(G,N[i],N[j]) == True):smallest_paths.append(nx.shortest_path(G,N[i],N[j]))
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
inner_hit = []
for i in range(len(diameter)):
      diameter_shells = []
      number = 0
      hit = 0
      for j in range(len(diameter[i])):
            diameter_shells.append(shell_no[diameter[i][j]])
            if(shell_no[diameter[i][j]] == maximum) :
                   number = number +1
                   hit = 1
      inner_encountered.append(number)
      inner_hit.append(hit)	
      print(i)	
      print(diameter_shells)
      print('no of times the diameter passed  through inner nodes are : '+str(number))
	  
avg = sum(inner_encountered)/len(inner_encountered)
avgg = sum(inner_hit)/len(inner_hit)
print("no of tiimes it hit inner shell in each iteration: ")
print(inner_encountered)
print("to see whether it hit the inner shell : ")
print(inner_hit)
print('no of times on an average the diameter encountered the inner nodes is : '+str(avg))
print("no of times on an average the diameter hit the inner shell is : "+str(avgg))

