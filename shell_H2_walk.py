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
G = nx.read_edgelist('filename.txt', nodetype = int)
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
max_shell_no = k
for i in N:
         shell_no.append(i)
                  
for j in range(n):
      for r in range(k):
            p=len(buckets[r])
            for y in range(p):
                  if (N[j] == buckets[r][y]) : shell_no[j] = r+1    				           
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
#print(len(H1))	
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
#print("success")

q=0
x=0
#print(H2)

#walk
max_encountered_list = []
walk=[]
shell_list=[]
shell_set_list=[]
distint_shell_list=[]
F=[]
no_of_steps=[]
k = len(buckets)

while(q<50): 
         start = random.choice(buckets[k-1])
         for m in range(t):
               
               walk.append(start)
               M=list(G.neighbors(start))
               if(len(M)==0):start = random.choice(buckets[k-1])
               for j in range(len(M)):
                     F.append(H2[N.index(M[j])])
               #print(F)
               ind = max([i for i,j in enumerate(F) if j == max(F)])		  
               F=[]                   
               start = M[ind]
               
         
         
         for o in range(t):
               shell_list.append( shell_no[walk[o]])
         shell_set = set(shell_list)
         shell_set_list = list(shell_set)
         for s in range(t):
               if(shell_list[s] == max_shell_no) : x= x+1
         print("walk "+str(q+1)+" :no of times max shell_no encountered is :" + str(x))
         print("           no of distint shells encountered = "+str(len(shell_set_list)))
         if(x != 0): 
                print("          no of steps required to encounter max shell are "+str(t/x))
                no_of_steps.append(t/x)
         else:
                print("          in coverage of .01*nodes it did not reach innermost shell")
                no_of_steps.append(0)		
         max_encountered_list.append(x)
         distint_shell_list.append(len(shell_set_list))
         q = q+1
         walk=[]
         shell_list=[]
         
         x=0
              
print(max_encountered_list)
avg = sum(max_encountered_list)/len(max_encountered_list)
avgg = sum(distint_shell_list)/len(distint_shell_list)
avggg = sum(no_of_steps)/len(no_of_steps)
print("on an average in length of "+str(t)+" we encountered a node of max shell no for "+str(avg)+" times")
print("on average in every walk " +str(avgg)+" distint shells are encountered")
