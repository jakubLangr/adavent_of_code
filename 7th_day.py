import networkx as nx

def load(file_name: str):
    file_object = open(file_name, 'r')
    loaded = file_object.read()
    split_s = loaded.split('\n')
    return split_s

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

def construct_requirements(graph):
    requirements = {}
    reversed_adj_list = list(graph.adj.keys())[::-1]
    for key in reversed_adj_list:
        requirements[key] = [x[0]
                             for x in list(graph.edges) if x[1] == key]
            
    return requirements


def check_requirements(reqs: dict, key: str, done: set):
    considered_key = set(reqs[key])
    return considered_key.issubset(done)


def next_valid_move(graph: nx.DiGraph(), key: str, reqs: dict, done: set):
    adj_nodes = graph[key]
    done = set(done)
    candidate_nodes = []
    for n in adj_nodes:
        done.add(n)
        if set(reqs[n]).issubset(done):
            candidate_nodes.append(n)
        else:
            done.remove(n)

    return sorted(candidate_nodes), done

def graph_to_order(graph):
    '''
     AdjacencyView({'C': {'A': {}, 'F': {}}, 'A': {'B': {}, 'D': {}}, 'F': {'E': {}}, 'B': {'E': {}}, 'D': {'E': {}}, 'E': {}})

    Out[420]: ['C', 'A', 'F', 'B', 'D', 'E']
    '''
    # TODO: Maybe perform a check we are indeed at the start node

    bfs_list = sorted(list(graph.adj.keys()))
    progress = list(bfs_list[0])
    reqs = construct_requirements(graph)
    final_order = ''
    done = set()
    offset = 1

    while progress != []:
        init_key = progress.pop(0)
        key_list, done = next_valid_move(graph, init_key, reqs, done)
        if len(key_list)==1:
            final_order += key_list[0]
        elif len(key_list)>1:
            final_order += key_list[0]
            progress.append(key_list[1:])
        else:
            progress.append(init_key)
    
    print(final_order)
    return final_order

def solution(graph):
    reqs = construct_requirements(graph)
    valid_options = sorted([ k for k in reqs.keys() if reqs[k]==[]])
    done = []
    
    while valid_options!=[]:
        choice = valid_options.pop(0)
        graph.remove_node(choice)
        done += choice
        for k in list(graph.nodes):
            if check_requirements(reqs, k, done):
                valid_options.append(k)
        
        valid_options = list(set(valid_options))
        valid_options.sort()
        
    done = ''.join(done)
    return done
    

def part_one(file_name: str):
    loaded = load(file_name)
    graph = list_to_graph(loaded)
    result = graph_to_order(graph)
    assert set(graph.adj.keys()) == set(result)
    return result


G = list_to_graph(test_case)
assert solution(G) == "CABDFE"
file_name = 'day7_input.txt'

prev_guesses = [
    'YLOPDTQSXCMGHNEIABZKRWVUFJ',
    'YLOPDTQSXCMGHNEABIZKRUWVFJ',
    'JFVWURKZIBAENHGMCXSQTDPOLY',
    'HPDTNXYLOCGESIMAZKRUWQBVFJ'
]

loaded_file = load(file_name)
graph = list_to_graph(loaded_file)
result = solution(graph)
assert result not in prev_guesses
# assert result.startswith('HPDTNX')

def effort(step: str, base: int = 60):
    return ord(step) - ord("A") + base + 1

assert effort('Z') == 86
assert effort("C", base=0) == 3

print('Checks passed.')

class WorkItem:
    worker: int
    item: str
    start_time: int
    end_time: int


def part_two(graph, num_workers: int, base: int = 60):
    '''
    NOT DONE YET
    '''
    reqs = construct_requirements(graph)
    valid_options = sorted([ k for k in reqs.keys() if reqs[k]==[]])
    done = []
    time = 0
    work_items = '?'
    
    while valid_options!=[]:
        # done?
        for work_item in work_items:
            if work_item and work_item.end_time <= time:
                pass
        
        choice = valid_options.pop(0)
        graph.remove_node(choice)
        done += choice
        for k in list(graph.nodes):
            if check_requirements(reqs, k, done):
                valid_options.append(k)
        
        valid_options = list(set(valid_options))
        valid_options.sort()
        available_workers = [ i for i in range(num_workers)
                              if i is None]
        
        while available_workers and valid_options:
            worker_id = available_workers.pop()
        
    done = ''.join(done)
    return done




