#!/usr/bin/env python3

import sys

from py2neo import Graph
from py2neo.data import Node, Relationship


def main():

    # pass the input file as an argument instead of stdin to allow for using input()
    with open(sys.argv[1]) as f:
        T = int(next(f))  # the number of test cases
        cases = [(int(next(f)), map(int, next(f).split())) for case in range(T)]

    graph = Graph()

    for case, (N, kids) in enumerate(cases, 1):
        print(f'Test case #{case}, N={N}', end=' ')

        graph.run('MATCH (n) DETACH DELETE n')

        nodes = [None, *[Node('Kid', name=i) for i in range(1, N+1)]]

        for i, v in enumerate(kids, 1):
            rel = Relationship(nodes[i], 'BFF', nodes[v])
            graph.create(rel)

        input('(press Enter to continue) ')


main()
