#!/usr/bin/python

import collections
import string
import sys

def ComputeGroup(stack, allwords):
    group = collections.defaultdict(set)
    while len(stack) > 0:
        word = stack.pop()
        group[word] = set()
        for perm in Permutations(word):
            if perm in allwords:
                allwords.remove(perm)
                stack.append(perm)
                group[word].add(perm)
                group[perm].add(word)
    return group

def Permutations(word):
    for permindex in range(len(word)):
        for permval in string.ascii_lowercase:
            newword = word[:permindex] + permval + word[permindex+1:]
            if newword != word:
                yield newword

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: words.py <dictfile>"
        sys.exit(1)

    f = open(sys.argv[1])
    allwords = set()
    for line in f:
        word = line.strip().lower()
        if len(word) != 4:
            continue
        if not all(c in string.ascii_lowercase for c in word):
            continue
        allwords.add(word)
    f.close()

    print "%s 4-letter words found" % len(allwords)

    stack = []
    groups = []
    while len(allwords) > 0:
        word = allwords.pop()
        stack.append(word)
        group = ComputeGroup(stack, allwords)
        if len(group) < 25:
            print "Group of %s words found: %s" % (len(group), ', '.join(group.keys()))
        else:
            print "Group of %s words found" % len(group)
        groups.append(group)


