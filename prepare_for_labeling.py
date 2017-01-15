"""This project cleans our tweet dataset from: RT, and duplicate tweets"""
from collections import OrderedDict

import tweet_preprocessor as tp
import re

path = 'F:\Internet Explorer\Ders\Calismalar\python\exp\\'
name = 'ds.txt'

in_name = path+name
out_name = path + 'cleaned_' + name
infile = open(in_name,encoding='utf-8')
outfile = open(out_name, 'w',encoding='utf-8')

tweets = []

# tp.set_options(tp.OPT.HASHTAG, tp.OPT.URL, tp.OPT.MENTION)
index = 0
index_list = []                 # keeps unique tweets original index

#
print("Cleaning RT and empty lines... ",end='')
for line in infile:
    # delete stars from line starting
    if line[0] == '*':
        line = line.replace(line[0], '')

    # delete empty and RT sites
    if line and line[0:2] != 'RT':
        line = tp.clean(line)

        # delete duplicates
        line = line.strip().lower()
        if line not in tweets:
            tweets.append(line)
            index_list.append(index)
    index += 1
infile.seek(0)
print("OK.\n")

i = 0
# print original but cleaned tweets

# TODO: OPTIMIZE HERE: READING FROM ORIGINAL FILE IS TOO MUCH

print('Writing results to a new file... ', end='')
# print(len(index_list))      # number of lines in the out file
for line in infile:
    if line and i in index_list:
        try:
            print(line, file=outfile, end='')       # if there is a character problem with a line
        except UnicodeEncodeError as e:
            print('Character error at line number {}. This line will be passed.'.format(i))
            continue

    i += 1
print("OK.\n")

print("DONE..")
