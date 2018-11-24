import networkx as nx
import matplotlib.pyplot as ply
import random
import numpy
G=nx.Graph() 
G = nx.read_edgelist('graph_name.txt', nodetype = int)
n = len(G.nodes())
print("no of nodes in graph:"+str(n))
t = int(n/100)
N=list(G.nodes())
q=0
x=0
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
H2_distinct = set(H2)
H2_distinct_list = list(H2_distinct)
print("no of distinct shells in this graph : "+str(len(H2_distinct_list )) )         	  
H2_1=[]
for i in range(len(G.nodes())):
      if(H2[i] == min(H2)):H2_1.append(N[i])
maximum = max(H2)
total = 0  

#random walk
distint_shell_list = []
walk=[]
shell_list=[]
max_encountered_list = []
shell_set_list =[]
while(q<50): 
         start = random.choice(H2_1)
         for m in range(t):
               
               walk.append(start)
               M=list(G.neighbors(start))
               if(len(M)==0):start = random.choice(H2_1)			  
               start = random.choice(M)
         #print(walk)
         
         for o in range(t):
               shell_list.append( H2[N.index(walk[o])])
         #print(shell_list)
         shell_set = set(shell_list)
         shell_set_list = list(shell_set)
         for s in range(t):
               if(shell_list[s] == maximum) : x=x+1
         print("walk "+str(q+1)+" no of distint shells encountered = "+str(len(shell_set_list)))
         max_encountered_list.append(x)
         distint_shell_list.append(len(shell_set_list))
         print("         no of times max shell_no encountered is :" + str(x))
         max_encountered_list.append(x)
         q = q+1
         walk=[]
         shell_list=[]	 
         x=0
print(max_encountered_list)
avg = sum(max_encountered_list)/len(max_encountered_list)
avgg = sum(distint_shell_list)/len(distint_shell_list)
print("on an average in random walk of length "+str(t)+" we encountered a node of max shell no for "+str(avg)+" times")
print("Hence avg no of steps taken to reach inner shell are : "+str(t/avg))
print("on average in every walk " +str(avgg)+" distint shells are encountered")                        
