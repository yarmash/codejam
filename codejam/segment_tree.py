import operator

# For theory, see:
# https://www.youtube.com/watch?v=eBslys79xr4
# https://www.youtube.com/watch?v=dddEwytZE7g
# TODO: add support for updates on ranges
class SegmentTree:
    """
    A segment tree class for RSQ/RMQ queries, with support for elements modification.
    Time complexity (n is the number of elements in the original sequence):
        * build - O(n)
        * query - O(log n)
        * modify - O(log n)
    """
    def __init__(self, seq, query_type='sum'):
        self.seq = seq
        self.query_type = query_type

        if query_type == 'sum':
            self.func = operator.add
            self.neutral_value = 0
        elif query_type == 'max':
            self.func = max
            self.neutral_value = -float('inf')
        elif query_type == 'min':
            self.func = min
            self.neutral_value = float('inf')
        else:
            raise ValueError('Unknown type: ' + query_type)

        self.tree = [None]*(4*len(seq))
        self._build(0, 0, len(seq) - 1)

    def _build(self, v, vl, vr):
        if vl == vr:
            self.tree[v] = self.seq[vl]
            return

        vm = (vl + vr) // 2
        self._build(2*v + 1, vl, vm)
        self._build(2*v + 2, vm + 1, vr)
        self.tree[v] = self.func(self.tree[2*v + 1],
                                 self.tree[2*v + 2])

    def query(self, l, r):
        return self._query(0, 0, len(self.seq)-1, l, r)

    def _query(self, v, vl, vr, l, r):
        if r < vl or vr < l:
            return self.neutral_value
        if l <= vl and vr <= r:
            return self.tree[v]

        vm = (vl + vr) // 2
        return self.func(self._query(2*v + 1, vl, vm, l, r),
                         self._query(2*v + 2, vm + 1, vr, l, r))

    def modify(self, pos, val):
        return self._modify(0, 0, len(self.seq)-1, pos, val)

    def _modify(self, v, vl, vr, pos, val):
        if pos < vl or vr < pos:
            return
        if vl == vr:
            self.tree[v] = val
            return

        vm = (vl + vr) // 2
        if pos <= vm:
            self._modify(2*v + 1, vl, vm, pos, val)
        else:
            self._modify(2*v + 2, vm + 1, vr, pos, val)
        self.tree[v] = self.func(self.tree[2*v + 1],
                                 self.tree[2*v + 2])
