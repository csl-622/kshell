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
G = nx.read_edgelist('soc-Epinions1.txt', nodetype = int)
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
max_shell_no = k-1
j=0
r=0                  
for j in range(len(N)):
      for r in range(k):
            if(N[j] in buckets[r]):shell_no[j] = r 
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
l =  max(H2)
print("no of different H2 indeces are : "+str(l+1))

#finding correlativity
concordant=0
discordant=0
equals =0
for i in range(len(N)-1):
       for j in range(i+1, len(N)):
             if(((shell_no[i] > shell_no[j]) and (H2[i] > H2[j])) or ((shell_no[i] < shell_no[j]) and (H2[i] < H2[j]))) : concordant = concordant+1
             elif(((shell_no[i] < shell_no[j]) and (H2[i] > H2[j])) or ((shell_no[i] > shell_no[j]) and (H2[i] < H2[j]))) : discordant = discordant+1
             else:equals=equals+1             
correlativity = (concordant - discordant)/(concordant + discordant + equals)
print("no of concordant pairs are : "+str(concordant)+" ; no of discordant pairs are : "+str(discordant) +" ; rest : " + str(equals))
print("correlativity between the h2indeces and coreness is : "+str(correlativity))
      
