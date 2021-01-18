#!/usr/bin/env python3

"""BFFs"""

from collections import defaultdict


def get_component(kid, id_to_bff, bff_to_ids):
    """Find the connected component containing the kid."""
    component = set()
    stack = [kid]
    while stack:
        kid = stack.pop()
        component.add(kid)

        # this kid's bff
        if id_to_bff[kid] not in component:
            stack.append(id_to_bff[kid])

        # kids for which this one is bff
        for kid_id in bff_to_ids[kid]:
            if kid_id not in component:
                stack.append(kid_id)
    return component


def get_cycle(component, id_to_bff):
    """Find the component's cycle."""
    kid = next(iter(component))
    seen = set()
    while kid not in seen:
        seen.add(kid)
        kid = id_to_bff[kid]
    # okay, we've reached the loop now
    cycle = set()
    while kid not in cycle:
        cycle.add(kid)
        kid = id_to_bff[kid]
    return cycle


def get_chain_len(cycle, bff_to_ids):
    """Find the longest chain that can be formed from a 2-cycle component."""
    chain_len = 2

    for kid in cycle:
        max_subchain_len = 0
        stack = [(kid, 0)]

        while stack:
            last_kid, subchain_len = stack.pop()
            if subchain_len > max_subchain_len:
                max_subchain_len = subchain_len

            for kid_id in bff_to_ids[last_kid]:
                if kid_id not in cycle:
                    stack.append((kid_id, subchain_len + 1))

        chain_len += max_subchain_len

    return chain_len


def main():
    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        N = int(input())  # the total number of kids in the class
        id_to_bff = {}  # every kid has a single bff
        bff_to_ids = defaultdict(list)  # a kid may be a bff of multiple kids
        kids = set()

        for kid_id, bff_id in enumerate(map(int, input().split()), 1):
            id_to_bff[kid_id] = bff_id
            bff_to_ids[bff_id].append(kid_id)
            kids.add(kid_id)

        components = []

        while kids:
            kid = kids.pop()
            component = get_component(kid, id_to_bff, bff_to_ids)
            components.append(component)
            kids.difference_update(component)

        connectable_components = []
        candidates = []

        for component in components:
            cycle = get_cycle(component, id_to_bff)
            if len(cycle) == 2:
                chain_len = get_chain_len(cycle, bff_to_ids)
                connectable_components.append(chain_len)
            else:
                candidates.append(len(cycle))

        res = max(max(candidates, default=0), sum(connectable_components))

        print(f'Case #{case}: {res}')


main()
