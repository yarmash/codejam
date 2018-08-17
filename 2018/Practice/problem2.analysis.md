## Senate Evacuation

### Test set 1

With at most three parties and at most nine senators, various brute force approaches will work. One exhaustive strategy is to generate all possible different evacuation orders, treating senators from the same party as interchangeable, and then try all possible different ways of chopping those into groups of one or two senators.

Another, simpler strategy is to keep randomly choosing and trying one of the nine possible evacuations (A, B, C, AA, AB, AC, BB, BC, CC) as long as the chosen senator(s) exist and the evacuation will not cause a new absolute majority. You may worry that this strategy could get stuck, but the outcome of any legal evacuation will just be another possible test case for the problem, and the statement guarantees that every test case has a solution! With more parties and senators, though, this strategy might bog down in the details of checking the legality of evacuations, so we should come up with a more efficient approach.

### Test set 2

Intuitively, it is safest to remove one senator at a time, and to always draw from whichever party has the most remaining senators (or any such largest party, if there is a tie). But this strategy won't always work! For example, if we have two senators from party A and two from party B, and no others, which is a valid test case, then removing one senator from either party will give the other party an absolute majority.

However, this strategy _is_ always safe whenever there are more than two parties present. Suppose that party 1 is currently the largest, or tied for the largest, of at least three parties, and that we remove a single senator from party 1\. Clearly, making party 1 smaller cannot give it an absolute majority that it didn't have before. But could some other party acquire an absolute majority as a result? Suppose that the removal of a senator from party 1 were to cause party 2, which currently has X senators, to have an absolute majority. But since party 1 was the largest, or tied for the largest, before a senator was removed, party 1 must still have at least X-1 senators. Moreover, since at least one more party is present, there is at least 1 other senator who is not from party 1 or 2\. So there are a total of at least X remaining senators who are not from party 2, which means the X senators of party 2 are not enough to give it an absolute majority, so we have a contradiction.

If we start with three or more parties and keep evacuating a single senator from the largest party in this way, then at some point, we must reach a step in which we go from three parties to two parties. These two remaining parties must have only one senator each. Since we just removed the one remaining senator from the third party, it must have been a largest party, so the other two can be no larger. So we can remove this last pair of senators in a single evacuation as a final step.

What if we start with two parties? Since the problem statement guarantees that no party begins with a majority, these parties must have equal numbers of senators. So, we can evacuate them in pairs, one from each party, until the evacuation is complete.

This approach takes more steps than are needed — most of those single evacuations can be paired up — but it gets the job done.
