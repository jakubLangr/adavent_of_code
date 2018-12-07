import networkx as nx

def load(file_name: str):
    file_object = open(file_name, 'r')
    loaded = file_object.read()
    split_s = loaded.split('\n')
    return split_s

new_file = load('day7_input.txt')

test_case = [
    "Step C must be finished before step A can begin.",
    "Step C must be finished before step F can begin.",
    "Step A must be finished before step B can begin.",
    "Step A must be finished before step D can begin.",
    "Step B must be finished before step E can begin.",
    "Step D must be finished before step E can begin.",
    "Step F must be finished before step E can begin."
]

def list_to_graph(list_text):
    G = nx.DiGraph()
    for text in list_text:
        text_list = text.split(' ')
        sn = text_list[1]
        en = text_list[-3]
        G.add_edge(sn, en)
    
    return G

G = list_to_graph(test_case)

def graph_to_order(graph):
    '''
     {'C': ['A', 'F'], 'A': ['B', 'D'], 'B': ['E']}
    '''
    # TODO: Maybe perform a check we are indeed at the start node
    dfs_results = nx.dfs_successors(G)
    final_order = list(dfs_results)[0][0]
    for key in dfs_results.keys():
        adj_nodes = sorted(dfs_results[key])
        for node in adj_nodes:
            import ipdb
            ipdb.set_trace()
            if node in final_order:
                final_order = final_order.replace(node, '')
        final_order += ''.join(adj_nodes)

    return final_order



result = graph_to_order(test_case)
print(result)
print(graph_to_order(test_case) == "CABDFE")
