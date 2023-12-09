"""
SNA Practical 2 :Perform following tasks:
1)View data collection forms and/or import one mode/two-mode dataset;
2)Basic Networks matrices transformations

"""

import networkx as nx
import pandas as pd

data_collection_form = pd.DataFrame({
    'Node1' : [1,3,4,5,6,],
    'Node2' : [2,4,7,6,3],
    'Weight' : [1,2,2.6,5.0,3.3]
})

print("Data Collection Form :\n", data_collection_form)

one_mode_data = pd.DataFrame({
    'Node' : [2,3,4,8,4,9],
    'Attribute1' : ['A' , 'B' , 'D' , 'E' , 'F' , 'I'],
    'Attribute2' : [0.5, 1.2, 2.6, 8.6, 4.3, 5.2]
})

print("\n One Mode Dataset:\n", one_mode_data)

two_mode_data = pd.DataFrame({
    'Node1' : [2,4,8,6,7],
    'Node2' : ['A','C','D','J','K'],
    'Weight' : [1.8,2.9,8.6,4.4,9.0]
})

print("\n Two Mode Dataset:\n", two_mode_data)

G_one_mode = nx.from_pandas_edgelist(data_collection_form, 'Node1', 'Node2', 'Weight')

B_two_mode = nx.from_pandas_edgelist(two_mode_data, 'Node1' , 'Node2' , ['Weight'], create_using=nx.Graph)

adjacency_matrix = nx.to_numpy_array(G_one_mode)
print("\n Adjacency Matrix 1 : \n",adjacency_matrix)




