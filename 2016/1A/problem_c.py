#!/usr/bin/env python

"""BFFs"""

from collections import defaultdict


def main():

    def get_component(kid, id_to_bff, bff_to_ids):
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

    def get_cycle_len(component, id_to_bff):
        # find the cycle len
        kid = next(iter(component))
        seen = set()
        while kid not in seen:
            seen.add(kid)
            kid = id_to_bff[kid]
        # okay, we've reached the loop now
        cycle = {kid}
        start = kid
        kid = id_to_bff[kid]
        length = 1
        while kid != start:
            cycle.add(kid)
            kid = id_to_bff[kid]
            length += 1
        return length, cycle

    def get_chain_len(component, cycle, bff_to_ids):
        def get_subchain_len(bff):
            chain = 0
            for kid in bff_to_ids[bff]:
                if kid not in cycle:
                    chain = max(chain, 1+get_subchain_len(kid))
            return chain

        chain_len = 2
        for kid in cycle:
            chain_len += get_subchain_len(kid)

        return chain_len

    T = int(input())  # the number of test cases

    for case in range(1, T+1):
        input()  # the total number of kids in the class, ignored
        id_to_bff = {}  # every kid has a single bff
        bff_to_ids = defaultdict(list)  # a kid may be a bff of multiple kids

        for kid_id, bff_id in enumerate(map(int, input().split()), 1):
            id_to_bff[kid_id] = bff_id
            bff_to_ids[bff_id].append(kid_id)

        kids = set(id_to_bff)
        components = []

        while kids:
            kid = kids.pop()
            component = get_component(kid, id_to_bff, bff_to_ids)
            components.append(component)
            kids.difference_update(component)

        connectable_components = []
        candidates = []

        for component in components:
            cycle_len, cycle = get_cycle_len(component, id_to_bff)
            if cycle_len == 2:
                chain_len = get_chain_len(component, cycle, bff_to_ids)
                connectable_components.append(chain_len)
            else:
                candidates.append(cycle_len)

        res = max(max(candidates, default=0), sum(connectable_components))

        print(f'Case #{case}: {res}')


main()
