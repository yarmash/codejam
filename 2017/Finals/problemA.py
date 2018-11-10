#!/usr/bin/env python

from itertools import starmap


class Die:
    def __init__(self, id=None, current_value=None):
        self.id = id
        self.current_value = current_value

    def __repr__(self):
        return f'Die({self.id!r})'


class DieValue:
    def __init__(self, value, dice):
        self.value = value
        self.dice = dice  # Set of dice containing this value

    def __repr__(self):
        return f'DieValue({self.value!r}, {self.dice!r})'

    def find_unused_die(self):
        """Returns the first unused die among the ones containing this value, or None if not found."""
        return next((die for die in self.dice if die.current_value is None), None)

    def assign_die(self):
        """If no die is used by this value, use the first die among the ones containing this value."""
        if all(die.current_value is None for die in self.dice):
            self.dice[0].current_value = self

    def unassign_die(self):
        """If a die is used by this value, unassign it."""
        for die in self.dice:
            if die.current_value == self:
                die.current_value = None
                break


class TestCase:
    visited = set()  # To skip already visited dice when recursively shuffling

    def __init__(self, ndice, values):
        self.ndice = ndice
        self.values = values

    def free_by_shuffling(self, die):
        """
        Attempt to recursively free a die by selecting a different die for the same value.
        Return True if the die has been freed, False if no other die can be found.
        """
        assert die.current_value is not None

        stack = [die]
        found = False

        while stack:
            this_die = stack.pop()

            if found:
                if stack:
                    this_die.current_value = stack[-1].current_value
                    stack[-1].current_value = None
                continue

            for other_die in this_die.current_value.dice:
                if other_die.current_value is None:
                    stack.extend((this_die, other_die))
                    found = True
                    break
            else:
                self.visited.add(this_die)

                for other_die in this_die.current_value.dice:
                    if other_die not in self.visited:
                        stack.extend((this_die, other_die))
                        break
                else:
                    if stack:
                        for other_die in stack[-1].current_value.dice:
                            if other_die not in self.visited:
                                stack.append(other_die)
                                break
        return found

    def find_unused_by_shuffling(self, value):
        """
        Attempt to find an unused die for the specified value by possibly shuffling other already used dice.
        Return a now-unused die, or None if no shuffling results in an unused die.
        """

        self.visited.clear()

        for die in value.dice:
            if self.free_by_shuffling(die):
                return die

        return None

    def find_longest_straight(self):
        """Finds the maximum length of dice with consecutive values."""
        max_length = 1
        end_index = 0

        for begin_index, value in enumerate(self.values):
            value.assign_die()

            begin_value = value.value
            max_possible_length = min(len(self.values) - begin_index, self.ndice)

            next_begin_index = begin_index + 1

            if end_index <= begin_index:
                end_index = begin_index + 1

            while end_index < len(self.values):
                value = self.values[end_index]
                if value.value != begin_value + end_index - begin_index:
                    # Not a consecutive value, restart scanning from there
                    next_begin_index = end_index
                    break

                die = value.find_unused_die()
                if die is None:
                    die = self.find_unused_by_shuffling(value)
                if die is None:
                    break

                die.current_value = value
                end_index += 1

                if end_index - begin_index > max_length:
                    max_length = end_index - begin_index

                if max_length == max_possible_length:
                    break

            if max_length == max_possible_length:
                break

            # The old values at the beginning are no longer useful, free their dice
            for idx in range(begin_index, next_begin_index):
                self.values[idx].unassign_die()

        return max_length


def main():
    T = int(input())

    for i in range(T):
        ndice = int(input())
        value2dice = {}  # map values to lists of dice

        for j in range(1, ndice+1):
            die = Die(id=j)

            for value in map(int, input().split()):
                value2dice.setdefault(value, []).append(die)

        # Set of distinct values on the face of all dice, sorted by value
        values = list(starmap(DieValue, sorted(value2dice.items())))
        case = TestCase(ndice, values)

        print(f'Case #{i+1}: {case.find_longest_straight()}')


main()
