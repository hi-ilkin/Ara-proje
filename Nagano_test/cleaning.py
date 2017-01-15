"""This project cleans our tweet dataset from: RT, and similar tweets"""
from collections import OrderedDict

import tweet_preprocessor as tp
import re

infile = open('nagano.txt', encoding='utf_8')
outfile = open('nagano_new.txt', 'w', encoding='utf_8')

tweets = []

tp.set_options(tp.OPT.HASHTAG, tp.OPT.URL, tp.OPT.MENTION)

for line in infile:
    if line[0] == '*':
        line = line.replace(line[0], '')

    if line and line[0:2] != 'RT':
        line = tp.tokenize(line)
        # print(line)
        # print(line,file=outfile)
        tweets.append(line)

for line in tweets:
    unique_lines = OrderedDict.fromkeys((line for line in tweets if line))

for key in unique_lines.keys():
    print(key, file=outfile)
