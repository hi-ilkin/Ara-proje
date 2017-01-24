import re
from collections import Counter
import math

import numpy as np
import time

import preprocess_and_create_arff as prep
import tweet_preprocessor as tp
import editdistance as ed
from nltk.corpus import wordnet as wt
from AllData import SimilarityMatrix as SMM
import Hierarchical_clustering as hc
from normalizr import Normalizr


def noiseCleaning(summarize):
    """
    Cleaning hashtags, usernames, urls, numbers, punctuations, emojis, stop words folding all to lowercase
    tokenizing dataset and returning tokenized set

    :param summarize: obj of Similarity_Matrix
    :return: cleaned and tokenized dataset
    """
    tokenized_dataset = []  # keeps tokenized tweets

    normalizr = Normalizr(language='en')

    for line in summarize.get__tweets():
        # clear url, hashtags and usernames and fold to lower case
        line = tp.clean(line.lower())

        # clear numbers
        line = re.sub('\d', '', line)

        # clear punctutations, other symbols and stopwords
        line = normalizr.normalize(line)

        # tokenize all tweets
        tok = line.split()

        # collect all tweets in a list, each tweet is a list
        tokenized_dataset.append(tok)

    return tokenized_dataset


def cc_UHU(summarize):
    """ count Username, Hashtag, URL

        :return - url, username, hashtag, special character, stop word free dataset
    """

    # number of lines in our tweet set
    tweet_count = summarize.tweet_count()

    # TODO: TERM SIMILARITY:
    # TODO: count similar URL , USERNAME and HASHTAGS

    # regex patterns
    url_pattern = 'http[s]*://[^\s]*'
    user_name_pattern = '@\w+'
    hashtag_pattern = '#\w+'

    for i in range(tweet_count - 1):
        for j in range(i + 1, tweet_count):
            url_match_i = re.findall(url_pattern, summarize.get__tweets(i))  # URLs of tweet i
            url_match_j = re.findall(url_pattern, summarize.get__tweets(j))  # URLs of tweet j

            usrname_match_i = re.findall(user_name_pattern, summarize.get__tweets(i))  # username of tweet i
            usrname_match_j = re.findall(user_name_pattern, summarize.get__tweets(j))  # username of tweet j

            hashtag_match_i = re.findall(hashtag_pattern, summarize.get__tweets(i))  # hashtags of tweet i
            hashtag_match_j = re.findall(hashtag_pattern, summarize.get__tweets(j))  # hashtags of tweet j

            # intersect 2 matching object gives us a set of similar elements
            # length of this intersection is similar url/username/hashtag count between 2 tweets
            try:
                # intersect url
                summarize.increase_value('uhu', i, j, len(set(url_match_i).intersection(url_match_j)))

                # intersect usernames
                summarize.increase_value('uhu', i, j, len(set(usrname_match_i).intersection(usrname_match_j)))

                # intersect hashtags
                summarize.increase_value('uhu', i, j, len(set(hashtag_match_i).intersection(hashtag_match_j)))
            except IndexError:
                print("\nCurrent indexes are: {} , {}\n".format(i, j))
                exit()
            # old version of cleaning
            # tokenized_clean_tweets = prep.noiseCleaning(tokenized_dataset)  # noise cleaning


# TODO: Selecting similar tweets
def select_summarize(summarize, *args):
    """
    Selects summary tweet. for clustered and non-clustered tweets

    :param summarize: Object of Similarity_Matrix
    :param args: for non-clustered tweets , leave empty, for clustered tweets, send list of labels in a cluster
    :return:
    """

    similarity = summarize.get__value('similarity')
    t_similarity = similarity.transpose()

    # summarizing with clustering
    # selects most weighted tweet in the cluster
    if len(args) == 1:
        label_id = args[0]
        count = len(label_id)

        # weight of each tweet
        weight = np.zeros(count, dtype=np.int64)

        # calculate weight of each tweet
        for i in range(count):
            weight[i] = np.sum(similarity[label_id[i]]) + np.sum(t_similarity[label_id[i]])
            # print("weight of {} >> {}".format(label_id[i], weight[i]))
        # most weighted tweet
        index = np.argmax(weight)
        print("{}".format(summarize.get__tweets(label_id[index])))

    # summarizing without clustering
    # selects most weighted tweet in the set
    else:
        count = summarize.tweet_count()
        weight_1 = np.zeros(count, dtype=np.int64)
        for i in range(0, count):
            # print(np.sum(similarity[i]))
            # print(np.sum(t_similarity[i]),'\n')
            weight_1[i] = np.sum(similarity[i]) + np.sum(t_similarity[i])
            print("weight of {} >> {}".format(i, weight_1[i]))

        for i in range(0, 5):
            index = np.argmax(weight_1)

            # print("biggest value is in {},{}".format(row, col))
            weight_1[index] = 0

            print("{}".format(summarize.get__tweets(index)))


# TODO: !!!! BIG PROBLEM !!!! TOTALLY EMPTY TWEETS AFTER PREPROCESS

def write2File(dataset):
    """
    writes cleaned tweets to a file and creates a list of cleaned tweets

    :param dataset: tweet list
    :return: list of cleaned tweet
    """

    # writing to a file
    try:
        fin = open('temp_tweet_set.txt', 'w+')
    except FileNotFoundError as e:
        print("error: ", e)

    temp_line = ''
    cleaned_tweets = []
    for line in dataset:
        for word in line:
            if word and len(word) > 2:
                print(word, file=fin, end=' ')  # joining words and creating tweets again
                word += ' '
                temp_line += word

        cleaned_tweets.append(temp_line)
        temp_line = ''
        print('', file=fin)

    return cleaned_tweets


############################################################################################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  END of write2File(dataset)~~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################


def calc_ces(summarize, tweets):
    """
    Calculates Cosine similarity, Edit distance and Semantic similarity between tweets

    :param summarize: Object of Similarity_Matrix class. Keeps data
    :param tweets: tokenized tweets
    """

    tweet_count = summarize.tweet_count()

    print("Calculating cosine similarity , Levensthein distance and Semantic similarity...", end='')

    for i in range(0, tweet_count - 1):
        for j in range(i + 1, tweet_count):

            # todo: cosine similarity
            vec1 = Counter(tweets[i])  # Creating a counter object ,
            vec2 = Counter(tweets[j])  # Which gives us number of each word in the sentence

            intersection = set(vec1.keys()) & set(vec2.keys())  # intersection of sentences
            numerator = sum([vec1[x] * vec2[x] for x in intersection])  # calculating cosine similarity

            sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
            sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
            denominator = math.sqrt(sum1) * math.sqrt(sum2)

            if not denominator:  # if one of the sentences is empty, denominator is 0
                summarize.increase_value('ed', i, j, 0.0)
            else:
                inc_value = float(numerator) / denominator
                summarize.increase_value('cosine', i, j, inc_value * 10)  # increase similarity value

            # todo: Levenshtein Distance and Semantic similarity
            # second part - Lenevshetin distance

            synset_of_t1 = []  # keeps all synsets of words in tweet1
            synset_of_t2 = []  # and tweet2

            for word1 in tweets[i]:
                # counting synsets for word1 for semantic similarity
                synset_of_t1 = synset_of_t1 + wt.synsets(word1)

                for word2 in tweets[j]:
                    # counting synsets for word2 for semantic similarity
                    synset_of_t2 += wt.synsets(word2)

                    L_dist = len(max(word1, word2)) - ed.eval(word1, word2)
                    if L_dist > 0:
                        summarize.increase_value('ed', i, j, L_dist)

            synset_intersection_count = set(synset_of_t1).intersection(set(synset_of_t2))  # intersection of t1 and t2

            # len of the intersection is our similarity value
            summarize.increase_value('semantic', i, j, len(synset_intersection_count))

    print("OK!")

############################################################################################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  END of ces(summarize, tweets)~~~~~~~~~~~~~~~~~~~~~~~~~~#
############################################################################################

def main():
    start_time = time.time()
    fin_name = "California_test\\cal_500.txt"  # result set file
    print("Opening and reading tweets...", end='')
    summarize = SMM()
    summarize.openFile(fin_name, encodeWith='utf_8')  # opening file
    print('OK!')

    # number of lines in our tweet set
    tweet_count = summarize.tweet_count()

    # initializing matrices with 0
    print('Initializing matrices with value 0...', end='')
    summarize.initialize()
    print('OK!')

    # count UHU
    print("Calculating similar Username, Hashtag and Url counts...", end='')
    cc_UHU(summarize)
    print('OK!')

    # clear redundant information and tokenize
    print("Clearing tweets form redundant information and tokenizing...", end='')
    new_tweets = noiseCleaning(summarize)
    print("OK!")

    # TODO: calculate edit distance, cosine similarity and semantic similarity together
    calc_ces(summarize, new_tweets)

    # creating similarity graph = term_level + semantic_level
    print("Creating similarity graph...", end='')
    summarize.create_similarity_graph()
    print('OK!')

    # TODO : CLUSTERING
    # clustering similar tweets
    print("Clustering results...", end='')
    cluster_labels = hc.cluster(summarize.get__value('similarity'))
    print("OK!")
    #
    print("Selecting top tweets...\n")
    print("Total Cluster number: ", len(cluster_labels))
    for label in cluster_labels:

        # Creating summary
        if len(label) > 1:  # don't use 1 sample clusters in summarize
            select_summarize(summarize, label)
            # print(label)

    # summarizing without clustering
    # select_summarize(summarize)

    # summarize.printSlice(summarize.get__similarity_graph(), [125, 125, 150, 150], 2)
    # summarize.printSlice(summarize.get__similarity_graph(), round_step=2)

    print("\nEVERYTHING is OK, CONGRATULATIONS...")
    end_time = time.time()

    print("\nWork time = ", end_time-start_time)

######################################################################################################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  END of main() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
######################################################################################################

if __name__ == "__main__": main()
