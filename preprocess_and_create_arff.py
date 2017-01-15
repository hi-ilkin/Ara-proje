""" ~~~~ Preprocess for classification: ~~~~~
# Steps : Clear all ;
# - punctuations
# - URL
# - Hashtags
# - usernames
# - rt
"""

import re

from nltk.corpus import stopwords
import tweet_preprocessor as twt_prep

# file names and pathes for easier access
path = "data/"
fname = "etiketli_tweet.txt"
class_name = "nagano_"
processed_path = 'processed_data/'

def main():

    filepath = path+class_name+fname
    openFile(filepath)

    print("DONE...")


def openFile(filename):
    """"Etiketli tvitlerin bulundugu dosyayi acar, tvitlerin hepsi kucuk harf olacak sekilde donusturur ve bir liste yazar """

    try:
        # to skip non printable ascii chars, use this
        # fp = open(filename, "r", encoding='utf-8-sig', errors='ignore')
        fp = open(filename, "r")
    except:
        print("File error!\n")
    else:
        # a list that contains all tweets
        dataset = list()
        for line in fp:
            dataset.append(line.lower())

            # preprocessing
        tokenizeTweet(dataset)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~ END of openFile function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


def tokenizeTweet(dataset,flabel='labels.txt',ftoken='token.txt',writeFile=True):
    '''Tokenizes data , splits label values after getting cleared data , writes file
    \n - dataset - dataset that tokenized
    \n - flabel - file name for labels
    \n - ftoken - file name for tokens - every word in a sentence
    \n - writeFile - default value True, write or do not write to a file
    '''


    pos_pattern = re.compile('\A[-]*[0-3]+')

    # label_file = open(flabel, 'w', encoding='utf-8-sig', errors='ignore')  # keeps label values
    label_file = open(flabel, 'w')
    # tokenized_file = open(ftoken, 'w', encoding='utf-8-sig', errors='ignore')  # keeps tokenized tweets
    tokenized_file = open(ftoken, 'w')

    tokenized_dataset = []  # consists tokinezed tweets
    tweet = ''  # a temporary list  for a single tweet
    label_list = []  # contains label information for tweets

    for line in dataset:
        line = twt_prep.clean(line)

        # checking if line is a tweet or label
        isLabel = re.match(pos_pattern, line)
        if isLabel and len(line) < 3:

            # appending tokinezed tweet to our dataset and reset temp tweet list
            tokenized_dataset.append(tweet)
            tweet = ''

            # add label to the label list
            temp = int(line)
            if temp > 0:
                label_list.append(1)  # positive label
            else:
                label_list.append(0)  # negative label

        else:

            tweet = line.split()
            # line = re.sub(neg_pattern, "", line)

    # writing to the file
    for a in label_list:
        print(a, file=label_file, end='\n')

    for b in tokenized_dataset:
        print(b, file=tokenized_file, end='\n')

    # next step - cleaning redundant characters
    tokenized_dataset = noiseCleaning(tokenized_dataset)

    # writing preprocessed data to a file
    if writeFile:
        write2file(tokenized_dataset, label_list)

    return tokenized_dataset

# ~~~~~~~~~~~~~~~~~~~~~~~~~~ END of tokenizeTweet function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


def noiseCleaning(dataset):
    """Tokenized edilmis tweetleri alarak, istenmeyen karakterleri ve sayilari siler"""

    # negatif pattern - karakter ve sayilari silmek icin
    neg_pattern = re.compile('\W+''|\d+')
    tokenized_dataset = []

    # tokenize edilmis tweetler icerisinden kelimeler bir-bir alinarak islemler uygulanir
    for tweet in dataset:
        i = 0
        # print("before: ", tweet)
        for word in tweet:
            word = re.sub(neg_pattern, '', word)  # fazla karakterlerin ve sayilarin silinmesi
            if word in stopwords.words('english'):  # stopword'lerin silinmesi
                word = ''

            tweet[i] = word  # son islemler sonrasi, veri setinin guncellenmesi
            i += 1
        # print("after: ", tweet)
        tokenized_dataset.append(tweet)

    # print(tokenized_dataset)
    # test print
    # for tweet in tokenized_dataset:
    #     print(tweet)

    return tokenized_dataset


def write2file(dataset, label):
    """tokenized edilmis veri setini etiket degerleri ile birlikte comma-seperated ve normal sekilde dosyaya yazilmasi"""

    processed_fname = processed_path+class_name+'processed_file.arff'
    processed_fname_comma = processed_path + class_name + 'processed_file_comma.arff'

    # processed_file_cs = open(processed_fname, 'w', encoding='utf-8-sig', errors='ignore')
    processed_file_cs = open(processed_fname, 'w')
    # processed_file_normal = open(processed_fname_comma, 'w', encoding='utf-8-sig', errors='ignore')
    processed_file_normal = open(processed_fname_comma, 'w')

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
    for f in (processed_file_cs, processed_file_normal):
        for a in (arff_comments, arff_relation, arff_atributes, arff_data):
            print(a, file=f, end='')

    i = 0  # index of labels
    for tweet in dataset:
        # weka recognizes strings with '. adding starting of each line
        print("'", end='', file=processed_file_cs)
        print("'", end='', file=processed_file_normal)

        # writing words
        for word in tweet:
            if word:
                # writing words to the files : comma-seperated and whitespace seperated
                print(word, end=',', file=processed_file_normal)
                print(word, end=' ', file=processed_file_cs)

        # adding ' end of each line
        print("'", end='', file=processed_file_cs)
        print("'", end='', file=processed_file_normal)

        # writing label values to each file
        print(str(label[i]), file=processed_file_normal, end='\n')
        print(',' + str(label[i]), file=processed_file_cs, end='\n')
        i += 1


if __name__ == "__main__": main()
