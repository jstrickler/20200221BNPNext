#!/usr/bin/env python

with open('DATA/words.txt') as words_in:
    q_words = (word.rstrip() for word in words_in if word.startswith('q') and word[1] != 'u')

    for q_word in q_words:
        print(q_word)

