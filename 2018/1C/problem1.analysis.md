## A Whole New Word

### Test set 1

Since **L** ≤ 2, this test set can be solved using a complete search. First, we collect the letters
that appear among the first characters of the input words in a set C<sub>1</sub> and the letters
that appear among the second characters of the input words in a set C<sub>2</sub>. Any candidate
new word has the form c<sub>1</sub>c<sub>2</sub>, where c<sub>1</sub> is in C<sub>1</sub> and
c<sub>2</sub> is in C<sub>2</sub>. For each candidate new word, we check whether this word is in
the input. We can output any candidate new word which does not appear in the input as our answer.
If every candidate new word already appears in the input, the case is impossible.

Since there are only at most 26<sup>2</sup> different candidate words that we need to try, this
solution will run very quickly.

### Test set 2

In early rounds of Code Jam, a complete search will often work for the first test set, but will
generally not work for subsequent test sets. This problem is an exception! Our approach above will
work just fine for test set 2.

We can create sets C<sub>1</sub>, C<sub>2</sub>, ..., C<sub>**L**</sub> as in the solution above,
and then use them to generate candidate words as before, one at a time. If we encounter a word that
is not in the input, we can return it as our answer. If it turns out that there are exactly **N**
candidate words (which implies that every word that could be generated is already in the input),
the case is impossible. Otherwise, we can be sure that we will have found an answer by the time we
generate and check the (**N** + 1)th candidate word, since there are only **N** words in the input
list.
