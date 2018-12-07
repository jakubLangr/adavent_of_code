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
    [('C', {'A': {}, 'F': {}}),
    ('A', {'B': {}, 'D': {}}),
    ('F', {'E': {}}),
    ('B', {'E': {}}),
    ('D', {'E': {}}),
    ('E', {})]
    '''
    adj_list = list(G.adjacency())[::-1]
    final_order = adj_list[0][0]
    first_check = True
    for node in adj_list:
        adj_nodes = sorted(list(node[1].keys()))[::-1]
        checked_nodes = [ x for x in adj_nodes if x not in final_order ]
        first_check = False
        final_order += ''.join(checked_nodes)

    final_order += adj_list[-1][0]
    
    return final_order[::-1]


result = graph_to_order(test_case)
print(result)
print(graph_to_order(test_case) == "CABDFE")
