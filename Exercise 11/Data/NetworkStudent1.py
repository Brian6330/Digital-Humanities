#
#  simple code to generate a graph
#

import os
import json
from networkx.readwrite import json_graph
import networkx as nx
import matplotlib.pyplot as plt


C = nx.cycle_graph(4)

nx.draw(C, with_labels=True)
plt.show()


S = nx.star_graph(4)
nx.draw(S, with_labels=True)
plt.show()


P = nx.path_graph(5)
nx.draw(P, with_labels=True)
plt.show()


G = nx.Graph()
G.add_node('a')
nodes_to_add = ['b', 'c', 'd']
G.add_nodes_from(nodes_to_add)

G.add_edge('a', 'b')
edges_to_add = [('a', 'c'), ('b', 'c'), ('c', 'd')]
G.add_edges_from(edges_to_add)

nx.draw(G, with_labels=True)
plt.show()

nx.draw(G, with_labels=True,
            node_color='blue',
            node_size=1600,
            font_color='white',
            font_size=16)

plt.show()

# overview of a graph G
G.nodes()
G.edges()

for node in G.nodes:
   print(node)

G.number_of_nodes()
G.number_of_edges()
G.neighbors('b')

for neighbor in G.neighbors('b'):
   print(neighbor)

# testing
nx.is_tree(G)
nx.is_connected(G) 
G.has_node('a')
G.has_node('x')
G.has_edge('a', 'b')
G.has_edge('a', 'd')
('c', 'd') in G.edges
len(list(G.neighbors('a')))


# another way to build a graph
    
V = {1, 2, 3, 4, 5}
E = {(1, 2), (1, 4), (2, 5), (3, 4), (4, 5)}


G = nx.Graph()
G.add_nodes_from(V)
G.add_edges_from(E)

nx.draw_networkx(G, font_color="black",
                 node_size=700, node_color='lightblue')
plt.axis('off');
plt.show()


# Examples with graph stored in a json file

with open('./data/Example1.json', 'w') as f:
    json.dump(json_graph.node_link_data(G), f)

G = 1
d = 2

with open('./data/Example1.json', 'r') as f:
    d = json.load(f)

G = json_graph.node_link_graph(d)
print(f"Graph with {len(G.nodes())} nodes and {len(G.edges())} edges.")


with open('./data/Example2.json', 'r') as f:
    d = json.load(f)

G = json_graph.node_link_graph(d)
print(f"Graph with {len(G.nodes())} nodes and {len(G.edges())} edges.")



for u, v in G.nodes(data=True):
    print (u,v)

for u, v, d in G.edges(data=True):
    print (u,v, d)


for u, v, d in G.edges(data=True):
    print (u,v, d['size'])


plt.axis('off')
color_map1 = {'M':'lightblue', 'F':'pink'}
color_map2 = {1:'black', 2:'green'}
pos = nx.spring_layout(G, k=0.5, iterations=200)
nx.draw(G, pos, with_labels=True, node_size=700,
        node_color=[color_map1[G.nodes[node]['gender']] for node in G],
        edge_color=[color_map2[d['size']] for u,v,d in G.edges(data=True)])
plt.show()



with open('./data/Campnet.json', 'r') as f:
    d = json.load(f)
    
G = json_graph.node_link_graph(d)    
print(f"Graph with {len(G.nodes())} nodes and {len(G.edges())} edges.")

pos = nx.spring_layout(G, k=0.5, iterations=200)
nx.draw(G, pos, font_color="black", node_size=700,
        with_labels=True,node_color='lightblue')
plt.axis('off');
plt.show()




with open('./data/Campnet.json', 'r') as f:
    d = json.load(f)

G = json_graph.node_link_graph(d)
print(f"Graph with {len(G.nodes())} nodes and {len(G.edges())} edges.")

nx.draw_networkx(G, font_color="black",
                 node_size=700, node_color='lightblue')
plt.axis('off');
plt.show()


plt.axis('off')
color_map1 = {'M':'lightblue', 'F':'pink'}
nx.draw(G, with_labels=True, node_size=500,
        node_color=[color_map1[G.nodes[node]['gender']] for node in G],
        edge_color='black')
plt.show()


