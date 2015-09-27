import collections
import random


def get_ngrams(original, n=3):
    """Splits a original into n-letter chunks.

    This works for words...
    >>> list(get_ngrams("anderson", n=3))
    ['and', 'nde', 'der', 'ers', 'rso', 'son']

    or lists (sentences).
    >>> list(get_ngrams(["The", "quick", "brown", "fox"], n=3))
    [['The', 'quick', 'brown'], ['quick', 'brown', 'fox']]
    """
    if len(original) < n:
        return

    i = 0
    while i < len(original) - (n - 1):
        yield original[i:i+n]
        i += 1


def all_but_last(items):
    """Return a tuple of all but the last item in items.
    >>> all_but_last([1, 2, 3, 4])
    (1, 2, 3)
    """
    return tuple(items[0:-1])


class Markov(object):
    """A simple generator that can either be fed in a word, or a list of words.
    If the former, then it will generate other words, if the latter, it will
    generates lists of words (sentences).
    It will attempt to ensure that the generated output begins and ends with a
    suitable sequence.
    """

    def __init__(self, n=3):
        self.cache = collections.defaultdict(lambda : [])
        self.beginnings = []
        self.endings = set()
        self.n = n

    def add(self, item):
        """Add a word (or a list of words) to the markov generator.
        """
        ngrams = list(get_ngrams(item, n=self.n))

        if len(ngrams) == 0:
            return

        first = ngrams[0]
        self.beginnings.append(all_but_last(first))

        last = ngrams[-1]
        # We chop off the first item of the last sequence, because that is
        # what we will be looking for in generate.
        #
        self.endings.add(tuple(last[1:]))

        for ngram in ngrams:
            key = all_but_last(ngram)
            last_item = ngram[-1]
            self.cache[key].append(last_item)

    def generate(self, end_prob=.2):
        """Generate a random sequence.
        end_prob is the probability of stopping whenever a known ending
        sequence is encountered.
        """
        current_tuple = random.choice(self.beginnings)
        result = list(current_tuple)

        while True:
            key = current_tuple

            if self.cache[key]:
                last_item = random.choice(self.cache[key])
                # Now the current tuple is
                #
                current_tuple = current_tuple[1:] + (last_item,)
            else:
                break

            result.append(last_item)

            if current_tuple in self.endings and random.random() < end_prob:
                break

        return result

