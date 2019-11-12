import networkx as np
import math
import random as rand
def rndom(n,e,c):
    if (e==1):
      p=rand.uniform(c*math.log(n)/n,1)
    else:
      p=rand.uniform(0,c*math.log(n)/n)
    g=np.gnp_random_graph(n,p)
    np.draw(g,node_size=20,node_color="dodgerblue")
    giant=max(np.connected_component_subgraphs(g),key=len)
    np.draw(giant,node_size=10,node_color="dodgerblue")
    return(p)
