#!/usr/bin/env python

# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
from operator import itemgetter


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    # Use the `reduce` function to keep a running count of the number of words
    # that match the specified criteria. The lambda expression expects the
    # accumulator (`a`) as the first argument (initially 0, as specified by the
    # third argument to `reduce`), and a word (`w`) to inspect as the second
    # argument. It returns the updated accumulator value by adding 1 to the
    # current accumulator value if the given word matches the criteria, or 0
    # otherwise. This works because `True` is treated as the integer 1, and
    # `False` as 0.
    return reduce(lambda a, w: a + (len(w) > 1 and w[0] == w[-1]), words, 0)


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    # Sort using 2-tuples as keys, where the first element of the tuple is a
    # Boolean value that is False if the word starts with 'x'; True otherwise.
    # The second element of the tuple is the word itself. This results in
    # tuples like the following:
    #
    #     (True, 'bbb')
    #     (False, 'xzz')
    #
    # This effectively partitions the words into 2 buckets (words starting with
    # 'x', and words not starting with 'x'). Sorting the words using such
    # tuples as keys ensures that all words starting with 'x' are considered
    # "less than" all words not starting with 'x'. Within each partition, words
    # are sorted as usual.
    return sorted(words, key=lambda w: (not w.startswith('x'), w))


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    return sorted(tuples, key=itemgetter(1))


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    return reduce(lambda l, e: l if l and e == l[-1] else l + [e], nums, [])


def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    >>> linear_merge(['a', 'b'], [])
    ['a', 'b']
    >>> linear_merge([], ['a', 'b'])
    ['a', 'b']
    >>> linear_merge([], [])
    []
    """
    return linear_merge_acc(list1, list2, [])


def linear_merge_acc(list1, list2, acc):
    if len(list1) == 0:
        return acc + list2
    if len(list2) == 0:
        return acc + list1
    if list1[0] < list2[0]:
        return linear_merge_acc(list1[1:], list2, acc + [list1[0]])
    return linear_merge_acc(list1, list2[1:], acc + [list2[0]])
