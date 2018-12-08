#!/usr/bin/env python3

from collections import defaultdict

def parse(filename):
    """
        Return list of tuple as : (predecessor, successor)
    """
    res = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            splitted = line.split()
            predecessor = splitted[1]
            successor = splitted[-3]
            res.append( (predecessor, successor))
    return res

def create_graph(data):
    """
        Create a graph using dictionary.
        The key of the dictionary represent a node.
        Its values represent its successors
    """
    graph = defaultdict(list)
    for p, s in data:
        graph[p].append(s)
    return graph

def find_predecessors(graph, node):
    """
        Return a list of nodes that are predecessors
        to this node
    """
    res = []
    for n in graph:
        sucessor = graph[n]
        if node in sucessor:
            res.append(n)
    return res

def find_nodes_with_no_predecessor(graph):
    """
        Find ndoes that don't have any predecessors.
        These nodes might be the starting node for traversing the graph
    """
    nodes = []
    for node in graph:
        predecessors = find_predecessors(graph, node)
        if not predecessors:
            nodes.append(node)
    return nodes


def topological_sort(graph):
    S = sorted(find_nodes_with_no_predecessor(graph))
    L = []
    while S:
        n = S[0]
        del S[0]
        L.append(n)
        next_nodes = graph[n]
        del graph[n]
        for m in next_nodes[:]:
            nodes = find_predecessors(graph, m)
            if not nodes:
                S.append(m)
        S = sorted(S)
    return L


def main():
    data = parse('input')
    graph = create_graph(data)
    print(''.join(topological_sort(graph)))

if __name__ == "__main__":
    main()

