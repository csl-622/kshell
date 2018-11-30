import networkx as nx
import matplotlib.pyplot as ply
import random
import numpy as np

G=nx.Graph() 
G = nx.read_edgelist('Graph_NAME.txt', nodetype = int)
n = len(G.nodes())
print("no of nodes in graph:"+str(n))
t = int(n/100)
N=list(G.nodes())
H1=[]
H2=[]
D=[]
DDD=[]
DD=[]
index=0
''' Finding the H1 indeces of the nodes of graph'''
for i in range(n):
      P = list(G.neighbors(N[i]))
      for j in range(len(P)):
            D.append(G.degree(P[j]))
      D.sort()
      myset=set(D)
      DDD=list(myset)
      
      for b in range(len(DDD)):
      
            DD.append(D.count(DDD[b])) 
      for h in range(len(DDD)):
            if( DD[h] >= DDD[h] ):index=DDD[h]	
      H1.append(index)
      D=[]
      DD=[]
      DDD=[]
      index = 0
''' Finding the H2 indeces of the nodes of graph '''

E=[]
EE=[]
EEE=[]
for i in range(n):
      R = list(G.neighbors(N[i]))
      for j in range(len(R)):
            E.append(H1[N.index(R[j])])
      E.sort()
      mset=set(E)
      EEE=list(mset)
      
      for k in range(len(EEE)):
      
            EE.append(E.count(EEE[k])) 
      for h in range(len(EEE)):
            if( EE[h] >= EEE[h] ):index=EEE[h]	
      H2.append(index)
      E=[]
      EE=[]
      EEE=[]
      index = 0
maximum = max(H2)
smallest_paths = []
i=0
j=0
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
            diameter_shells.append(H2[diameter[i][j]])
            if(H2[diameter[i][j]] == maximum) :
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

