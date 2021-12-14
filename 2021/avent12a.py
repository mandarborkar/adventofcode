import networkx as nx

filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent13testinput.txt'

h1 = [x.split('-') for x in [x for x in open (filename).read().strip().split('\n')]]
x1 =[]

totalses = 0

for x in h1:
    x1.append(x[0])
    x1.append(x[1])
#    print (x1)

xset = set(x1)
uniquenodes = (list(xset))

# print (x1)
# print (uniquenodes)

# Creating a Graph
G = nx.Graph() # Right now G is empty
G.add_nodes_from(uniquenodes)
for i in range (0,len(x1),2):
    G.add_edge(x1[i],x1[i+1])

# Let us find all the paths available
for path in nx.all_simple_paths(G, source='start', target='end'):
 print(path)

# Let us find the dijkstra path from JAX to DFW.
# You can read more in-depth on how dijkstra works from this resource - https://courses.csail.mit.edu/6.006/fall11/lectures/lecture16.pdf
dijpath = nx.dijkstra_path(G, source='start', target='end')
dijpath

print ('dij path ' + str(dijpath))

# A = pgv.AGraph(data=G)
# print(A) # This is the 'string' or simple representation of the Graph

'''
# Creating a Graph
G = nx.Graph() # Right now G is empty

# Add a node
G.add_node(1) 
G.add_nodes_from([2,3]) # You can also add a list of nodes by passing a list argument

# Add edges 
G.add_edge(1,2)

e = (2,3)
G.add_edge(*e) # * unpacks the tuple
G.add_edges_from([(1,2), (1,3)]) # Just like nodes we can add edges from a list

# Let us find all the paths available
for path in nx.all_simple_paths(FG, source='JAX', target='DFW'):
 print(path)
'''