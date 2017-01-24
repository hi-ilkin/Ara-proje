"""A draft for testing functions before use"""
import random
import re

from nltk.corpus import stopwords
import tweet_preprocessor as tp

# sp_words = []
# sp_words = stopwords.words('english')
# sp_words.sort()
#
# for word in sp_words:
#     print(','+word)
#

# line = " d kdjfhadlskjfhaldfh ljh n666ASJKDFHS999sdkjf "
# line = line.strip().lower()
# print(line)

# ~~~~~~~~~~~~~~~~~~ Tweet_preprocessor test ~~~~~~~~~~~~~~~~~~~~~~~~
# s = 'Preprocessor is, #awesome 👍 http://github.com/s/preprocessor -3'
# new1 = tp.clean(s)
# new2 = tp.tokenize(s)
# print(new1)
# print(new2)
#
# tp.set_options(tp.OPT.HASHTAG)
# new3 = tp.tokenize(s)
# print(new3)
# s = "This is 332423 of +-, af@d'fa-3.4"
# neg_pattern = re.compile('[\W\d]+')
# pat = re.compile('[^a-zA-Z]+')
#
# s = re.sub(pat, '#', s)
# print(s)


# etiket degerini kaybetmeden her tviti tuta bilmek icin , liste icinde liste kullanilacak, boylece indis degerleri ile tvitlere ve etiketlerine erisile bilecek. Etiket degerleri ayri bir listede tutulacak
#
# b = ['aafads', '#dafb', 'http.w.com', 1, 'ilkin', 'dfa']
# big = list()
# c = list()
# for v in b:
#     if v != 1:
#         c.append(v)
#     else:
#         big.append(c)
#         c = []
# big.append(c)
#
# for bg in big:
#     print(bg)

# ~~~~~~~~~~~~~~~~~~~~~~  creating random tweet set  ~~~~~~~~~~~~~~~~~~~~~~~~~~
# fin_name = 'California_test\\california_cleaned.txt'
# fout_name = 'California_test\\random_1000_tweets.txt'
#
# fin = open(fin_name, 'r')
# fout = open(fout_name, 'w')
#
# tweets = []
# lines = fin.readlines()
# i = 0
# while i<1000:
#     myline = random.choice(lines)
#     if myline not in tweets:
#         if myline:
#             tweets.append(myline)
#             i+=1
#
# tweets.sort()
#
# for line in tweets:
#     print(line, file=fout,end='')


# ~~~~~~~~~~~~~~~~~~~~ pattern for urls ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
line = 'Preprocessor is, #awesome 👍 http://sdfs.c https://github.com/s/preprocessor -3'
#
# matchObj = re.search('http[s]*://[^\s]*', line, re.I)
#
# pattern = 'http[s]*://[^\s]*'
# matches = re.findall(pattern,line,re.I)
#
# print(matches)

# ~~~~~~~~~~~~~~~~~~~~~~~~ Comparing 2 lists ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ref: http://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches
# list_a = ['http://fasfs.c','http://sdfs.c','http://sdfsafdafd.c.cv','http://sdfs.c','https://sdfs.c','http://sdfs.v']
# list_b = ['http://sdfssdf.c']
#
# print(set(list_a).intersection(list_b))             # returns a new list of intersection
# print(len(set(list_a).intersection(list_b)))

# ~~~~~~~~~~~~~~~~~~~~~~~~ Split a line ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# s = line.split()
# print(s)

# ~~~~~~~~~~~~~ Deleting unnecessary characters from a sentence ~~~~~~~~~~~~~
# neg_pattern = re.compile('\W+''|\d+')
#
# word = re.sub(neg_pattern, '', line)
#
# print(word)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Cosine similarity ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ref : http://stackoverflow.com/questions/15173225/how-to-calculate-cosine-similarity-given-2-sentence-strings-python
# import re, math
# from collections import Counter
# import tweet_preprocessor as tp
#
# WORD = re.compile(r'\w+')
#
# def get_cosine(vec1, vec2):
#      intersection = set(vec1.keys()) & set(vec2.keys())
#      numerator = sum([vec1[x] * vec2[x] for x in intersection])
#
#      sum1 = sum([vec1[x]**2 for x in vec1.keys()])
#      sum2 = sum([vec2[x]**2 for x in vec2.keys()])
#      denominator = math.sqrt(sum1) * math.sqrt(sum2)
#
#      if not denominator:
#         return 0.0
#      else:
#         return float(numerator) / denominator
#
# def text_to_vector(text):
#      return Counter(text)
#
# text1 = 'Hello world'
# text2 = 'Hello fasf wrld'
# text3 = 'Hello world'
#
# tok1 = text1.split()
# tok2 = text2.split()
# tok3 = text3.split()
#
# vector1 = text_to_vector(tok1)
# vector2 = text_to_vector(tok2)
# vector3 = text_to_vector(tok3)
#
# print("vector1 : ", vector1)
# print("vector2 : ", vector2)
# print("vector3 : ", vector3)
#
# cosine1 = get_cosine(vector1, vector2)
# cosine2 = get_cosine(vector2, vector3)

# cos1 = get_cosine(Counter(tok1), Counter(tok2))
# cos2 = get_cosine(Counter(tok2), Counter(tok3))

# print('Cosine(t1,t2) = ', round(cosine1, 3))
# print('Cosine(t2,t3) = ', round(cosine2, 3))
#
# print('Cos(t1,t2) = ', round(cos1, 3))
# print('Cos(t2,t3) = ', round(cos2, 3))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Levenshtein Distance ~~~~~~~~~~~~~~~~~~~~~~~~
# import editdistance as ed
# import numpy as np
# word_list = ['Hello world', 'Hello fasf world', 'fafs da', 'daha da felloo']
#
# tok_list = []
# for sentence in word_list:
#     tok_list.append(sentence.split())
#
# sim_mat = np.zeros((len(tok_list),len(tok_list)))
#
# for s1 in range(0,len(tok_list)-1):
#     for s2 in range(s1+1, len(tok_list)):
#         sim_mat[s1][s2] += len(set(tok_list[s1]).intersection(set(tok_list[s2])))
#         print(sim_mat[s1][s2], end= ' ')
#     print("\n")

# print("distance between tokenized sentence: ",ed.eval(tok1, tok2))
#
# sum = 0
# print("Distance between each word in the sentence: ")
# for fs_id in tok_list:
#     for ss_id in tok_list:
#         if fs_id != ss_id:
#             sum = 0
#             for word1 in fs_id:
#                 for word2 in ss_id:
#                     dist = len(max(word1, word2)) - ed.eval(word1, word2)
#                     if dist > 0:
#                         sum += dist
#             print("Distance between {} and {} : {}".format(fs_id,ss_id,sum))
#     print()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Testing WORDNET ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
from nltk.corpus import wordnet as wt

tw1 = 'A Dog has a cat'
tw2 = 'the dog has the dog'

tok_1 = tw1.split()
tok_2 = tw2.split()

# >>> shortest path

print()
# t1 = []
# t2 = []
# for word in tok_1:
#     t1 = t1 + wt.synsets(word)
# print("t1", "->", t1)
#
# for word in tok_2:
#     t2 += wt.synsets(word)
# print("t2", "->", t2)
#
# t3 = set(t1).intersection(set(t2))
# for t in sorted(t3):
#     print(t)
#
# word1 = 'a'
#
# word2 = 'automobile'
#
# t1 = wt.synsets(word1)
# t2 = wt.synsets(word2)
#
# for s1 in t1:
#     print(s1.hypernyms()[0].hypernyms(), '->', s1.hypernyms(), '->', s1)
#
# print('\n')
# for s2 in t2:
#     print(s2.hypernyms()[0].hypernyms(), '->', s2.hypernyms(), '->', s2)
#
# print(t1)
#
# print("Printing lowest_common_hypernyms:")
# for word in tok_1:
#     for word1 in tok_2:
#         t1 = wt.synsets(word)
#         t2 = wt.synsets(word1)
#
#         print("words: ",word," <-> ", word1,": ")
#         com = set(t1).intersection(set(t2))
#         for synset1 in t1:
#             for synset2 in t2:
#                 path = synset1.path_similarity(synset2)
#                 print("path value between {} and {} : {}".format(synset1, synset2, path))
#         count = len(com)
#         print("common sysnsets for {} and {} : {}".format(word, word1, com))
#         if count >0 :
#             print("They have {} common synset.".format(count))
#         # print (wt.synset(t1).lowest_common_hypernyms(wt.synset(t2)))


# ~~~~~~~~~~~~~~~~~~~~ shuffle file lines ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import random
path = 'F:\\Internet Explorer\\Ders\\Ara proje\\Kodlama\\California_test\\'
# lines = open(path + 'random_1000_tweets.txt').readlines()
# random.shuffle(lines)
# open(path + 'shuffeled_random.txt', 'w').writelines(lines)


# ~~~~~~~~~~~~~~~~~~~ magic of numpy ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import numpy as np
#
# a = np.zeros((2, 3))
# b = np.zeros((2, 3))
#
#
# for i in range(0,2):
#     for j in range(0,3):
#         a[i][j] = random.randint(0, 10)
#         b[i][j] = random.randint(0, 10)
#
# print(a)
# print(b)
# c = np.zeros((2, 3))
# c = ((a + b))
#
# print(c)


# ~~~~~~~~~~~~~ Tests for hierarchical clustering ~~~~~~~~~~~~~~~~~~~~~~~~~
# a = []
#
# values = [8,3,4,5,5,6,2,3,4,5,2]
#
# for value in values:
#     i = 0             # index of row
#     flag = 0          # checks if sth added to the list
#
#     for line in a:
#         if value in line:
#             a[i].append(value)
#             flag = 1
#             break
#         i+=1
#
#     if not flag:
#         a.append([value])
#
#
# print(a)
import Hierarchical_clustering as hc
#
# l = [[5, 37, 34, 77, 42, 70, 61, 38, 87, 85, 15, 8, 49, 68, 4, 76, 32, 27, 55, 29, 80, 84, 26, 86, 19, 94, 33, 35, 21,
#       10, 88, 65, 48, 79, 98, 40, 89, 0, 73, 11, 16, 97, 22, 2, 83, 71, 30, 6, 93, 69, 50],
#      [31, 74,
#                                                                                              [5, 37, 34, 77, 42, 70, 61,
#                                                                                               38, 87, 85, 15, 8, 49, 68,
#                                                                                               4, 76, 32, 27, 55, 29, 80,
#                                                                                               84, 26, 86, 19, 94, 33,
#                                                                                               35, 21, 10, 88, 65, 48,
#                                                                                               79, 98, 40, 89, 0, 73, 11,
#                                                                                               16, 97, 22, 2, 83, 71, 30,
#                                                                                               6, 93, 69, 50]]]
# # lenf = 0
#
# # print(len(l[0]))
# # for line in l:
# #     lenf += len(line)
# #
# # print(lenf)
# a = [[3,4,5,6],[2,1]]
# b = [[2,1],[1]]
# a[0] += a[1]
# del a[1]
# print(a)
#
# exit()
#

# mat = np.array([[0, 21, 47, 21, 35, 39, 0],
#                [0, 0, 24, 33, 17, 35, 1],
#                [0, 0, 0, 25, 23, 25, 11],
#                [0, 0, 0, 0, 14, 25, 19,],
#                [0, 0, 0, 0, 0, 26, 0],
#                [0, 0, 0, 0, 0, 0, 1],
#                [0, 0, 0, 0, 0, 0, 0]])

# hc.cluster(mat)
# exit()

#
# label = []
# print(type(mat))
# exit()
#
# threshold = 30   # threshold value
# sim_value = np.amax(mat)    # largest similarity value of the list
# count = mat.shape[0]
# print(count)
#
# while sim_value >= threshold:
#     rows, cols = np.where(mat == sim_value)     # row and column value(s) of the list
#     for idx in range(len(rows)):
#         index_of_Cluster1 = 0  # index of row
#         isFirstInList = False  # checks if sth added to the list
#         value1 = rows[idx]
#         value2 = cols[idx]
#
#         for line in label:
#             if value1 in line:  # value1 is already in label list
#                 index_of_Cluster2 = 0
#                 isSecondInList = False
#                 for other_line in label:  # if value is in other set
#                     if value2 in other_line:
#                         label[index_of_Cluster1].append(label[index_of_Cluster2])
#                         isSecondInList = True
#                         break
#                     index_of_Cluster2 += 1
#
#                 if not isSecondInList:  # value2 is not in the the list
#                     label[index_of_Cluster1].append(value2)  # append value 2
#                 isFirstInList = True
#             index_of_Cluster1 += 1
#
#         # first value is not in the list but we must check if second in the list
#         if not isFirstInList:
#             index_of_Cluster2 = 0
#             isSecondInList = False
#             for line in label:
#                 if value2 in line:
#                     label[index_of_Cluster2].append(value1)
#                     isSecondInList = True
#                     break
#                 index_of_Cluster2 += 1
#
#         # both values are not in the list
#         if not isFirstInList and not isSecondInList:
#             label.append([value1, value2])
#
#         mat[rows[idx]][cols[idx]] = -1.0    # changing max value to prevent double check
#     sim_value = np.amax(mat)    # next largest value of the list
#
# print(label)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Testing new normilizer ~~~~~~~~~~~~~~~~~~~~~~~~~~

# from normalizr import Normalizr
# import re
#
# normalizr = Normalizr(language='en')
# line = 'Ünlü şair demiş ki çal kemanını.'
# line = tp.clean(line.lower())
# line = re.sub('\d','',line)
# line = normalizr.normalize(line)
# tok = line.split()
# l = []
# l.append(tok)
# print(line)
# exit()


# ~~~~~~~~~~~~ dict test ~~~~~~~~~~~~
# class Similarity_Matrix:
#     __UHU = []
#     __cosine_similarity = []
#     __edit_distance = []
#     __term_level_sim = []   # term level similarity graph
#     __semantic_sim = []     # semantic similarity graph
#     __similarity_graph = [] # total similarity = term + semantic
#     __tweets = []  # a list that keeps all tweets
#
#     __normilize_max = 10
#     __normilize_min = 0
#
#     __key_map = {'uhu': __UHU, 'cosine': __cosine_similarity, "ed": __edit_distance, 'semantic': __semantic_sim,
#                "similarity": __similarity_graph}
#
#     def initialize(self, tweet_count):
#         for key in self.__key_map:
#               key = np.zeros((tweet_count, tweet_count))
#
#     def getValue(self, name):
#         return self.__key_map[name]
#
#
# def getSim(name,value):
#     tweet_count = 10
#
#     # __sim1 = np.zeros((tweet_count, tweet_count))
#     # sim2 = np.zeros((tweet_count, tweet_count))
#     # sim3 = np.zeros((tweet_count, tweet_count))
#
#     __sim1 = []
#     sim2 = []
#     sim3 = []
#
#     name_dict = {'sim1': __sim1, 'sim2': sim2, "sim3": sim3}
#
#     for key in name_dict:
#         name_dict[key] = np.zeros((tweet_count, tweet_count))
#
#     # print(name_dict['sim1'])
#
#     name_dict[name][0][0] += value
#     return name_dict[name]
#
# # print(getSim('sim1'))
#
# print(getSim('sim3',4))

# --------------- function test ----------------

from nltk.corpus import stopwords
import tweet_preprocessor as twt_prep
from normalizr import Normalizr

pos_pattern = re.compile('\A[-]*[0-3]+')

tokenized_dataset = []  # consists tokinezed tweets
tweet = ''  # a temporary list  for a single tweet
label_list = []  # contains label information for tweets
dataset = open('data\\nag.txt')
normalizr = Normalizr(language='en')
adLine = True

count = 0


for line in dataset:
    # clear url, hashtags and usernames and fold to lower case
    line = tp.clean(line)

    # checking if line is a tweet or label
    isLabel = re.match(pos_pattern, line)

    if adLine and isLabel and len(line) < 3:

        # appending tokinezed tweet to our dataset and reset temp tweet list
        # tokenized_dataset.append(tweet)
        # tweet = ''

        # add label to the label list
        temp = int(line)
        if temp > 0:
            label_list.append(1)  # positive label
        else:
            label_list.append(0)  # negative label

    else:
        # clear numbers
        line = re.sub('\d', '', line)

        # clear punctutations, other symbols and stopwords
        line = normalizr.normalize(line)

        if line:
            tokenized_dataset.append(line.split())
            adLine = True
        else:

            adLine = False
        count += 1

print(count)

for line, label in zip(tokenized_dataset,label_list):
    print(line,',',label)