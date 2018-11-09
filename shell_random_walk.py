import networkx as nx
import matplotlib.pyplot as ply
import random
import numpy
#necessary function to find the buckets list
def check_existence(H,d):
        f = 0
        for each in H.nodes():
                  if H.degree(each) <= d:
                           f =1
                           break
        return f				      
#necessary function to find the buckets list        
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

#computing the shells in the graph
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
#shell_no : list which has the shell numbers of nodes in order they are present in G
for j in range(n):
      for r in range(k):
            p=len(buckets[r])
            for y in range(p):
                  if (N[j] == buckets[r][y]) : shell_no[j] = r+1         
q=0
x=0
#random walk
distint_shell_list = []
walk=[]
shell_list=[]
max_encountered_list = []
shell_set_list =[]
while(q<50): 
         start = random.choice(N)
         for m in range(t):
               
               walk.append(start)
               M=list(G.neighbors(start))
               if(len(M)==0):start = random.choice(N)			  
               start = random.choice(M)
         #print(walk)
         
         for o in range(t):
               shell_list.append( shell_no[N.index(walk[o])])
         #print(shell_list)
         shell_set = set(shell_list)
         shell_set_list = list(shell_set)
         for s in range(t):
               if(shell_list[s] == k) : x=x+1
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
print("on an average in length of "+str(t)+" we encountered a node of max shell no for "+str(avg)+" times")
print("on average in every walk " +str(avgg)+" distint shells are encountered")                        