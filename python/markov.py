#!/usr/bin/env python

from __future__ import print_function

import random
import re
import sys
from collections import defaultdict


class MarkovText(object):
    def __init__(self, words, n=2):
        self.ngram_to_following_words = defaultdict(list)

        # Create a 'seed' ngram that is simply filled with None values. For
        # 2-grams, this will lead to the following mappings in the
        # ngram_to_following_words dictionary:
        #
        #     (None, None)  -> [word1]
        #     (None, word1) -> [word2]
        #
        # where word1 and word2 are the first and second input words,
        # respectively. Note that since no such 2-grams actually exist in the
        # input (although, technically they could, but that would be weird),
        # the only time either 2-gram could be chosen is when the generate
        # method initially chooses one of them at random.
        #
        # We could leave them out of the dictionary, but there's no harm in
        # having them either. There's likely little difference in generated
        # text values for sufficiently large inputs.
        ngram = (None,) * n

        # For each word in the input, add the word to the list of words that
        # follow the current ngram.
        for word in words:
            self.ngram_to_following_words[ngram].append(word)
            # Create the next ngram by dropping the zeroth word from the current
            # ngram, and appending the current word. The next word we get from
            # the input words is obviously the word that follows this ngram.
            ngram = ngram[1:] + (word,)

    def generate(self, n=100):
        if n <= 0:
            raise StopIteration

        def ends_sentence(token):
            return re.match('.+[.?!]"?$', token) is not None

        def seed_ngram():
            keys = self.ngram_to_following_words.keys()
            ngrams = keys if type(keys) == list else list(keys)
            seed = random.choice(ngrams)

            # Look for a seed ngram that ends a sentence so that the first word
            # we generate is a word that starts some sentence (since a word
            # that follows a ngram that ends a sentence is the start of a
            # following sentence).
            while not ends_sentence(seed[-1]):
                seed = random.choice(ngrams)

            return seed

        # Randomly choose a 'seed' ngram from all ngrams found in the input, so
        # that we can begin generating words.
        ngram = seed_ngram()

        # Generate up to n words, starting with a randomly chosen word from the
        # words that follow the current ngram.
        while True:
            try:
                word = random.choice(self.ngram_to_following_words[ngram])
            except IndexError:
                # When the currently chosen ngram is the last ngram of
                # the input, and that ngram appears nowhere else in the input,
                # there are no words that follow that ngram, so the value of
                # self.ngram_to_following_words[ngram] is an empty sequence.
                #
                # Since there is nothing to randomly choose from an empty
                # sequence, random.choice raises IndexError. In this case, we
                # want to stop iteration because we have no sensible means for
                # choosing the next word, but at least we're presumably at the
                # end of a sentence.
                raise StopIteration

            yield word
            n -= 1

            # Create the next ngram by dropping the zeroth word from the current
            # ngram, and appending the current word.
            ngram = ngram[1:] + (word,)

            # Even if we've generated the requested number of words, don't stop
            # generating words until we've reached what appears to be the end of
            # a sentence. This is simply to avoid generating output that ends in
            # the middle of a sentence.
            if n <= 0 and ends_sentence(word):
                raise StopIteration


def _words(source):
    with open(source) as lines:
        for line in lines:
            for word in line.split():
                yield word


def _main(source, max_words=100, ngram_len=2):
    for word in MarkovText(_words(source), ngram_len).generate(max_words):
        print(word, end=' ')


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: %s file max_words [ngram_size]" % sys.argv[0])
        sys.exit(1)

    _filename = sys.argv[1]
    _max_words = int(sys.argv[2])

    if len(sys.argv) < 4:
        _main(_filename, max_words=_max_words)
    else:
        _ngram_size = int(sys.argv[3])
        _main(_filename, _max_words, _ngram_size)
