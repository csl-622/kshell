import networkx as nx
import matplotlib.pyplot as ply
import random
import numpy as np
G=nx.Graph() 
G = nx.read_edgelist('graph_name.txt', nodetype = int)
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
q=0
x=0
#walk
max_encountered_list = []
walk=[]
shell_list=[]
shell_set_list=[]
distint_shell_list=[]
F=[]
no_of_steps=[]
H2_1=[]
#k = len(buckets)
#periphery nodes:
for i in range(len(G.nodes())):
      if(H2[i] == min(H2)):H2_1.append(N[i])

maximum = max(H2)
total = 0  
#print(H2_1)	  
while(q<50): 
          start = random.choice(H2_1)
          r=0
          repeat_count = 0

          while ((H2[N.index(start)] < maximum ) and (r<t)):
               
               walk.append(start)
               M=list(G.neighbors(start))
               if(len(M)==0):
                      start = random.choice(H2_1)
                      repeat_count = repeat_count+1
               for j in range(len(M)):
                      F.append(H2[N.index(M[j])])
               #print(F)
               ind = max([i for i,j in enumerate(F) if j == max(F)])		  
               F=[]
               if(H2[N.index(M[ind])] > H2[N.index(start)]):                   
                      start = M[ind]
               else:
                      repeat_count  =  repeat_count+1
                      start = M[ind]
               r = r+1
          print(str(q)+"st walk: the number of steps taken to reach the inner shell are = "+str(r))
          print("no of times it got stuck at the local maximum or for not having neighbors is: "+str(repeat_count))
          total = total + r
          q=q+1
print("avg no of steps taken in an iteration to reach inner most shell are: "+str(total/q))         
