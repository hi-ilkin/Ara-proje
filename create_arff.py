import re

from nltk.corpus import stopwords
import tweet_preprocessor as twt_prep
from AllData import SimilarityMatrix as SMM
import tweet_preprocessor as tp
from normalizr import Normalizr


def createArff():
    label_list = []

    # getting train set
    train_data = SMM.get__tweets(SMM, 'train')

    # tokenizing and separating label values
    tokenized_tweets = clean_and_tokenize(train_data, label_list)

    # creating arff file for train set
    if label_list:
        write2file(tokenized_tweets,'train', label_list)
    else:
        print("Label list is empty")
        exit()

    # doing same steps for train set
    test_data = SMM.get__tweets(SMM, 'test')
    tokenized_tweets = clean_and_tokenize(test_data)
    write2file(tokenized_tweets,'test')


# TODO : add labeled test set version
def clean_and_tokenize(data, *args):

    tokenized_dataset = []  # consists tokinezed tweets
    tweet = ''  # a temporary list  for a single tweet

    adLine = True
    normalizr = Normalizr(language='en')
    pos_pattern = re.compile('\A[-]*[0-3]+')

    if (len(args) == 1):

        label_list = args[0]
        for line in data:
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

    # for test set , we don't need to look for labels
    else:
        for line in data:

            # clear numbers
            line = re.sub('\d', '', line)

            # clear punctutations, other symbols and stopwords
            line = normalizr.normalize(line)

            tokenized_dataset.append(line.split())

    return tokenized_dataset

def write2file(dataset, fout, label=None):
    """
    Creates arff file in the same directory with project from tokenized dataset and label values

    :param dataset: tokenized dataset
    :param fout: name of output file test / train
    :param label: label values, if label=None, this is test set, but weka requires label for it too, so we add 0 to it
    :return:
    """

    f = open(fout+'.arff', 'w')

    # special arff keywords
    arff_comments = '%This is preprocessed tweet dataset with labels\n' \
                    '%project: Dogal Afetler sonrasi onemli tweetlerin belirlenmesi ve ozetlenmesi\n' \
                    '%preprocessed by - Ilkin Huseynli\n' \
                    '%date - 25.11.16\n\n\n'

    arff_relation = '@RELATION tweets\n\n\n'

    arff_atributes = '@ATTRIBUTE tweet STRING\n' \
                     '@ATTRIBUTE label {1,0}\n\n\n'

    # writing special arff things to the files
    arff_data = '@DATA\n'
    for a in (arff_comments, arff_relation, arff_atributes, arff_data):
        print(a, file=f, end='')

    i = 0  # index of labels

    if label != None:
        for tweet in dataset:
            # weka recognizes strings with '. adding starting of each line
            print("'", end='', file=f)

            # writing words
            for word in tweet:
                if word:
                    # writing words to the files : comma-seperated
                    print(word, end=',', file=f)

            # adding ' end of each line
            print("'", end='', file=f)

            # writing label values to each file
            print(',' + str(label[i]), file=f, end='\n')
            i += 1
    else:
        for tweet in dataset:
            # weka recognizes strings with '. adding starting of each line
            print("'", end='', file=f)

            # writing words
            for word in tweet:
                if word:
                    # writing words to the files : comma-seperated
                    print(word, end=',', file=f)

            # adding ' end of each line
            print("'", end='', file=f)

            # writing label values to each file
            print(',0', file=f, end='\n')
            i += 1
