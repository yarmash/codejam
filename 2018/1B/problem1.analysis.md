## Rounding Error

### Test set 1

This test set can be solved using a complete search. We can try every possible partition of **N**
voters among **N** languages. If two partitions differ only in the order of their languages, then
we consider those partitions equivalent.

Therefore, we can consider a partition as an **N**-tuple (x<sub>1</sub>, x<sub>2</sub>, ...,
x<sub>**N**</sub>), where x<sub>i</sub> ≥ x<sub>i + 1</sub> and Σ x<sub>i</sub> = **N**.

Even with **N** = 25, there are [no more than 2,000](https://oeis.org/A000041) different
partitions. For each partition, we can use the following greedy algorithm to check whether the
partition can be achieved by only adding voters: let us sort the **C**<sub>i</sub> values in
non-increasing order — that is, such that **C**<sub>i</sub> ≥ **C**<sub>i + 1</sub>. Then the
partition can be achieved by only adding voters if and only if **x**<sub>i</sub> ≥
**C**<sub>i</sub> for all 1 ≤ i ≤ **L**. Among all such partitions, we can find the largest
percentage sum, which is our answer.

### Test set 2

For this test set, we can remove our assumption that a partition and **C** must be sorted
non-increasingly. Therefore, we consider a partition of **N** voters to **N** languages as
(x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>**N**</sub>), where Σ x<sub>i</sub> = **N**.

To solve this test set, we can use [dynamic
programming](https://en.wikipedia.org/wiki/Dynamic_programming) (DP). We define a function f(a, b)
as the following:

Among all partitions (x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>a</sub>) such that Σ (1 ≤ i ≤ a)
x<sub>i</sub> = b and x<sub>i</sub> ≥ **C**<sub>i</sub> for all 1 ≤ i ≤ a, what is the maximum Σ (1
≤ i ≤ a) round(x<sub>i</sub> / **N** × 100) possible? If there is no satisfying partition, then
f(a, b) = -∞. We can assume **C**<sub>i</sub> = 0 for i > **L**.

We can first handle the base case of the function. We can easily compute f(1, b) since there is
only at most one satisfying partition. Therefore, f(1, b) = round(b / **N** × 100) if b ≥
**C**<sub>1</sub>, or -∞ otherwise.

The recurrence f(a, b) of this function can be computed by considering all possible values of
x<sub>a</sub>. Let i be the value of x<sub>a</sub>. Therefore, x<sub>a</sub> contributed round(i /
**N** × 100) to the total percentage, and there are (b - i) votes left to be distributed among
x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>a - 1</sub>. Therefore, for a > 1, f(a, b) = max
(**C**<sub>a</sub> ≤ i ≤ b) (round(i / **N** × 100) + f(a - 1, b - i)).

Since we want to distribute **N** voters to x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>**N**</sub>,
the answer for the problem is f(**N**, **N**).

Function f has O(**N**<sup>2</sup>) possible states and each state takes O(**N**) time to compute.
Therefore, this solution runs in O(**N**<sup>3</sup>) time.

### Test set 3

We can solve this test set with a greedy strategy. For each language, we will either be rounding
the percentage up or down. We get the maximum answer when as many of these as possible are rounded
up.

Therefore, we can ignore any languages that are already being rounded up. Since there can be
arbitrarily many languages, nothing ever forces us to disturb these languages by adding another
vote—it's no worse to add that vote to some new language instead. We figure out how many more votes
each language (including languages nobody has even mentioned yet) would need in order for it to be
rounded up.

We greedily satisfy as many of these as possible, starting with the ones that take the fewest
additional votes. This solution runs in O(**N** × log(**N**)) time.
