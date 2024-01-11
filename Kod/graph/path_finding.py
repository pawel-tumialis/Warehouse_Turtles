import pandas as pd
import numpy as np
import networkx as nx

from graph.graph import create_warehouse

def dijkstra_len(warehouse, dijkstra):
    length = 0
    for i in range(len(dijkstra)-1):
        length += warehouse[dijkstra[i]][dijkstra[i+1]]["weight"]
    return length


def create_smoll_graph(df, warehouse):
    
    smoll_graph=nx.Graph()
    for i in range(len(df["Lokacja"])):
        for j in range(i+1,len(df['Lokacja'])): 
            alpha = 0.9 * dijkstra_len(warehouse, nx.dijkstra_path(warehouse, df['Lokacja'][i], df['Lokacja'][j])) + 0.1 * df["Waga (kg)"][i]
            smoll_graph.add_edge(df['Lokacja'][i], df['Lokacja'][j], weight=alpha)

    return smoll_graph

def check(df, nodes):
    for index, row in df.iterrows():
        name = row['Lokacja']
        if not (name in nodes):
            df = df.drop(df.index[index]).reset_index(drop=True)
    return df

### PATH FINDER ###

def calc_dist(graph, path):
    dist = 0
    for idx in range(len(path)-1):
        dist += graph[path[idx]][path[idx+1]]
    return dist
 
# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, n):
    verticles = len(graph) 
    random_paths = [np.random.permutation(range(1,verticles-1)) for _ in range(n)]
    for i in range(len(random_paths)):
        random_paths[i] = np.append(random_paths[i], np.array([verticles-1]))
        random_paths[i] = np.insert(random_paths[i], 0, 0)
    
    min_dist, min_path = 300000, random_paths[0]

    for path in random_paths:
        dist = calc_dist(graph, path)
        if dist < min_dist:
            min_dist = dist
            min_path = path
    return min_path, min_dist

 
def find_path(df):
    warehouse = create_warehouse()
    new_record = pd.DataFrame([{"ID Produktu":222,"Nazwa Produktu":"klki","Lokacja":"H1Biuro","Ilość":45,"Waga (kg)":1}])
    new_record2 = pd.DataFrame([{"ID Produktu":222,"Nazwa Produktu":"klki","Lokacja":"H5Punkt rozładunku","Ilość":45,"Waga (kg)":1}])
    df = pd.concat([df, new_record2], ignore_index=True)
    df = pd.concat([new_record, df], ignore_index=True)

    warehouse_nodes = warehouse.nodes()
    df = check(df, warehouse_nodes)
    

    smoll_graph = create_smoll_graph(df, warehouse)
    numpy_array_graph = nx.to_numpy_array(smoll_graph)

    min_path, min_dist= travellingSalesmanProblem(numpy_array_graph, 50000)

    vertices_names = []
    for i in range(len(min_path)-1):
        v_start = min_path[i]
        v_koniec = min_path[i+1]
        # vertices_names.append(df["Lokacja"][v_start])
        dijkstra_path=nx.dijkstra_path(warehouse, df['Lokacja'][v_start], df['Lokacja'][v_koniec])
        vertices_names.extend(dijkstra_path[:-1])
    vertices_names.append("H5Punkt rozładunku")
    return vertices_names


if __name__ == '__main__':
    df = pd.read_csv('C:\dev\hest_hackaton\Droga.csv')
    find_path(df, create_warehouse())
   