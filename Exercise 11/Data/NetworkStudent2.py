#
# Simple code example with paths
#
import json
from networkx.readwrite import json_graph
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_nodes_from([1,2,3,4])
G.add_edges_from([(1,2),(2,3),(1,3),(1,4)])

nx.draw(G, with_labels=True)
plt.show()


nx.has_path(G, 3, 4)
list(nx.all_simple_paths(G, 3, 4))

nx.shortest_path(G, 3, 4)

nx.shortest_path_length(G, 3, 4)

nx.is_connected(G)

nx.shortest_path(G, 1)
nx.shortest_path_length(G, 1)

nx.shortest_path(G)

for u,v in nx.shortest_path_length(G):
   print(u,v)

nx.average_shortest_path_length(G)


# a second example

G2 = nx.Graph()

G2.add_edge(1,2)
G2.add_edge(2,3)
G2.add_edge(3,1)
G2.add_edge(4,5)

nx.draw(G2, with_labels=True)
plt.show()

nx.is_connected(G2)

nx.has_path(G2, 3, 5)
nx.shortest_path(G2, 3, 5)


nx.number_connected_components(G2)

list(nx.connected_components(G2))

components = list(nx.connected_components(G2))
len(components[0])

core_nodes = max(nx.connected_components(G2), key=len)
core = G2.subgraph(core_nodes)

nx.draw(core, with_labels=True)
plt.show()

#
# Directd graph

D = nx.DiGraph()
D.add_edges_from([
    ('a', 'e'),
    ('e', 'd'),
    ('d', 'f'),
    ('f', 'e') ])

nx.draw(D, with_labels=True)
plt.show()

for u,v in nx.shortest_path_length(D):
   print(u,v)

nx.average_shortest_path_length(D)



with open('./data/ExUndirected.json', 'r') as f:
   d = json.load(f)

G = json_graph.node_link_graph(d)


nx.draw(G, with_labels=True, arrowsize=20,
      node_color='lightblue', node_size=1600, width=2,
      font_color='black', font_size=16)
plt.show()

nx.has_path(G, 'a', 'b')
nx.has_path(G, 'a', 'c')
nx.shortest_path(G, 'a', 'b')
nx.shortest_path_length(G, 'a', 'b')
nx.shortest_path(G, 'a')

for u,v in nx.shortest_path_length(G):
   print(u,v)


with open('./data/ExDirected.json', 'r') as f:
   d = json.load(f)

G = json_graph.node_link_graph(d)

for u,v in nx.shortest_path_length(G):
   print(u,v)


nx.average_shortest_path_length(G)   # not possible

G.remove_node('c')
nx.average_shortest_path_length(G)


#
# Directed and weighted
#

with open('./data/ExDirectedWt.json', 'r') as f:
   d = json.load(f)

G = json_graph.node_link_graph(d)

color_mapLink = {1:'lightblue', 2:'blue', 3:'black'}
nx.draw(G, with_labels=True, arrowsize=20,
        node_color='lightblue', node_size=800, width=2,
        font_color='black', font_size=16,
        edge_color=[color_mapLink[d['size']] for u,v,d in G.edges(data=True)])
plt.show()


for u,v in nx.shortest_path_length(G):
   print(u,v)

nx.shortest_path_length(G, 'a', 'b')

nx.shortest_path_length(G, 'a', 'b', 'size')


nx.average_shortest_path_length(G)

G.remove_node('c')
nx.average_shortest_path_length(G)

nx.average_shortest_path_length(G, weight='size')



#
#  Degree and diameter
#
# Undirected graph
G = nx.Graph()
nodes_to_add = ['a', 'b', 'c', 'd']
G.add_nodes_from(nodes_to_add)
edges_to_add = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('c', 'd')]
G.add_edges_from(edges_to_add)

# draw the graph
nx.draw(G,
        with_labels=True,
        node_color='blue',
        node_size=800,
        font_color='white',
        font_size=16)
plt.show()

G.degree('a')

G.degree('c')

G.degree()

meanDegree = 0
for aNode, aDegree in G.degree():
   meanDegree += aDegree

meanDegree / len(G.degree())


# directed graph

W1 = nx.DiGraph()
W1.add_edge('a', 'b', weight=6)
W1.add_weighted_edges_from([('b', 'c', 3), ('b', 'd', 5)])

for (i, j, w) in W1.edges(data='weight'):
   if (w > 3):
      print ('(%s, %s, %d)' % (i, j, w))

W1.degree('b', weight='weight')


# undirected graph


with open('./data/ExUndirectedV2.json', 'r') as f:
   d = json.load(f)

G = json_graph.node_link_graph(d)

for u, v in G.nodes(data=True):
   print (u,v)

for u, v, d in G.edges(data=True):   print (u, v, d)


nx.clustering(G, "b")

nx.clustering(G)

nx.triangles(G)


nx.average_clustering(G)


# With Graph G22

nx.is_connected(G2)

nx.has_path(G2, 3, 5)
nx.shortest_path(G2, 3, 5)

nx.number_connected_components(G2)
list(nx.connected_components(G2))

components = list(nx.connected_components(G2))

len(components[0])

core_nodes = max(nx.connected_components(G2), key=len)
core = G2.subgraph(core_nodes)

nx.draw(core, with_labels=True)
plt.show()




import json
from networkx.readwrite import json_graph
import networkx as nx
import matplotlib.pyplot as plt

# Store graph G
with open('./data/Example1.json', 'w') as f:
   json.dump(json_graph.node_link_data(G), f)

# Read a graph
with open('./data/Example2.json', 'r') as f:
   d = json.load(f)

G1 = json_graph.node_link_graph(d)
print(f"Graph with {len(G1.nodes())} nodes and {len(G1.edges())} edges.")


# Read a graph
with open('./data/Example2.json', 'r') as f:
   d = json.load(f)

G = json_graph.node_link_graph(d)
print(f"Graph with {len(G.nodes())} nodes and {len(G.edges())} edges.")

for u, d in G.nodes(data=True):
   print (u,d)

for u, v, d in G.edges(data=True):
   print (u, v, d)

for u, v, d in G.edges(data=True):
   print (u, v, d['size'])

# Commen view of the graph
nx.draw(G1, with_labels=True)
plt.show()

# Draw with colors
color_map1 = {'M':'lightblue', 'F':'pink'}
color_map2 = {1:'black', 2:'green'}

nx.draw(G1, with_labels=True,
      node_color=[color_map1[G1.nodes[node]['gender']] for node in G1],
      edge_color=[color_map2[d['size']] for u,v,d in G1.edges(data=True)])

plt.show()


# a larger example CampNet

with open('./data/Campnet.json', 'r') as f:
   d = json.load(f)

G = json_graph.node_link_graph(d)

print(f"Graph with {len(G.nodes())} nodes and {len(G.edges())} edges.")

nx.draw_networkx(G, font_color="black")

plt.axis('off')
plt.show()

color_map1 = {'M':'lightblue', 'F':'pink'}

nx.draw(G, with_labels=True,
      node_color=[color_map1[G.nodes[node]['gender']] for node in G])

plt.show()


#
# Read a graph from a file
# Actor dataset

G = nx.read_graphml('./Dataset/Actor/actors_costar.graphml')

print('Nodes:', len(G.nodes()),' links:', len(G.edges()))

G.has_node('nm0000056')

G.has_node('nm0000054')

nx.shortest_path_length(G, 'nm0000056', 'nm0000054')

nx.shortest_path(G, 'nm0000056', 'nm0000054')

len(list(G.neighbors('nm0000054')))


for aN in list(G.neighbors('nm0000054')):
   print ('(%s)' % (aN)


#
# Read a graph from a file
# Flights in US

G = nx.read_graphml('./Dataset/openflights/openflights_usa.graphml')

G.nodes['IND']
G.nodes['IND']['name']





