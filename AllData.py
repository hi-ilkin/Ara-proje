import numpy as np
import data_normalizer as nz
import write2Excel as we


class SimilarityMatrix:
    __UHU = []  # username, hashtag, url
    __cosine_similarity = []  # cosine similariry values
    __edit_distance = []  # edit distance values
    __term_level_sim = []  # term level similarity graph
    __semantic_sim = []  # semantic similarity graph
    __similarity_graph = []  # total similarity = term + semantic
    __tweets = []  # a list that keeps all tweets

    __raw_train = []
    __raw_test = []

    __ready_test = []
    __ready_train = []

    __positive_tweets = []

    __normilize_max = 10
    __normilize_min = 0

    __key_map = {'uhu': __UHU, 'cosine': __cosine_similarity, "ed": __edit_distance, 'semantic': __semantic_sim,
                 "similarity": __similarity_graph}
    """
    keeps mnemonics for all matrices - uhu, cosine, ed, semantic, similarity
    """

    __tweet_key_map = {'rawtrain': __raw_train, 'rawtest': __raw_test, 'train': __ready_train, 'test': __ready_test,
                       'positive': __positive_tweets}
    """
    keeps mnemonics for all tweet sets - rawtrain, rawtest, train, test, positive
    """

    def initialize(self):
        """
        initialize all matrices with 0

        """
        tweet_count = self.tweet_count()
        for key in self.__key_map:
            self.__key_map[key] = np.zeros((tweet_count, tweet_count))

    # #######################  ~~~~~~~ GETTER ~~~~~~~  ####################### #
    def get__value(self, key, *args):
        """
        returns value/row/all of given matrix

        :param key: mnemonic of the matrix (uhu, cosine, ed, semantic, similarity)
        :param args: no args - returns all values in the given matrix, 1 value  - row, 2 values -
                    a value in given row,col
        :return: all of matrix, a row in the given matrix or a value
        """
        # returns all similarity matrix
        if len(args) == 0:
            return self.__key_map[key]

        # returns list of similarity values with tweet row
        elif len(args) == 1:
            row = args[0]
            return self.__key_map[key][row]

        # returns similarity value between tweets row and col
        elif len(args) == 2:
            row = args[0]
            col = args[1]
            return self.__key_map[key][row][col]

        else:
            raise ValueError("get__term_level_sim is excpected at most 2 args but got {}.".format(len(args)))

    # #######################  ~~~~~~~ SETTER ~~~~~~~  ####################### #
    def set__value(self, key, row, col, value):
        """
        Sets value to the given index

        :param key: mnemonic of the matrix - uhu, cosine, ed, semantic, similarity
        :param row: row value in matrix
        :param col: column value in given matrix
        :param value: new value
        :return:
        """
        if value == -1:
            pass  # if value is -1, this means that we are passing these tweets
        elif not value.isNumeric():
            raise TypeError('Value must be numeric!')
        else:
            self.__key_map[key][row][col] = value

    # #######################  ~~~~~~~ INCREASE ~~~~~~~  ####################### #
    def increase_value(self, key, row, col, inc_value):
        """ Increases value of given matrix with given value.
            After all values added, normalizes all values

        :param key: mnemonic of the matrix - uhu, cosine, ed, semantic, similarity
        :param row: row value in similarity matrix or row-th tweet
        :param col: col value in similarity matrix or col-th tweet
        :param inc_value: increment value
        """
        self.__key_map[key][row][col] += inc_value

    # #####################  ~~~~~~~ CREATING SIMILARITY GRAPH ~~~~~~~  ##################### #
    def create_similarity_graph(self):
        # TODO: normilize before adding similarity graph
        # normalizing edit distance values between 0-10
        self.__key_map['ed'] = nz.minMax(self.__key_map['ed'], self.__normilize_max, self.__normilize_min)
        self.__key_map['semantic'] = nz.minMax(self.__key_map['semantic'], self.__normilize_max, self.__normilize_min)

        for key in self.__key_map:
            if key != 'similarity':
                self.__key_map['similarity'] += self.__key_map[key]

            # writing results to an excel workbook
            we.write2Excel(self.__key_map[key], key)
        we.write2Excel(self.__key_map['similarity'], 'similarity')

    # #######################  ~~~~~~~ RAW TWEETS ~~~~~~~  ####################### #
    def get__tweets(self, dataset_name, *args):
        """
        Returns raw tweet in the given index
        :param dataset_name: name of the dataset to return
        :param args: if nothing given, returns all tweets in dataset, else returns tweet in given line
        :return: raw or preprocess set of tweets
        """
        if len(args) == 0:
            return self.__tweet_key_map[dataset_name]

        elif len(args) > 1:
            raise ValueError("get_tweets expected at most 1 argument got {} .".format(len(args)))

        else:
            index = args[0]
            return self.__tweet_key_map[dataset_name][index]

    # #######################  ~~~~~~~ TWEET COUNT ~~~~~~~  ####################### #
    def tweet_count(self):
        return len(self.__tweets)

    # #####################  ~~~~~~~ OPENING FILE ~~~~~~~  ####################### #
    def openFile(self, fin_name, set_name, encodeWith=None):
        """
        Open's and writes all tweets to a set line by line

        :param raw_train:
        :param raw_test:
        :param fin_name: dataset name
        :param encodeWith: default none, encoding technique for given file
        """

        # opening file
        try:
            fin = open(fin_name, 'r', encoding=encodeWith)
        except IOError as e:
            print("Something bad happened with files:\n", e)
            exit(-1)

        if set_name == 'train':
        # reading all file to a list, so working on them will be easier
            for line in fin:
                line = line.strip()  # strip blank spaces from starting and end

                # appending to raw train list
                self.__tweet_key_map['rawtrain'].append(line+'\n')

                line = line.lower()  # case fold all tweets
                self.__tweet_key_map['train'].append(line)

            return self.__tweet_key_map['rawtrain']

        elif set_name == 'test':
            # reading all file to a list, so working on them will be easier
            for line in fin:
                line = line.strip()  # strip blank spaces from starting and end

                # appending to raw train list
                self.__tweet_key_map['rawtest'].append(line + '\n')

                line = line.lower()  # case fold all tweets
                self.__tweet_key_map['test'].append(line)

            return self.__tweet_key_map['rawtest']


            # #####################  ~~~~~~~ PRINT SLICE ~~~~~~~  ##################### #
    def printSlice(self, key, coordinate=[0, 0, 99, 99], round_step=5):
        """
        Prints given part of matrix to the screen
        :param key: mnemonic of the matrix - uhu, cosine, ed, semantic, similarity
        :param coordinate: print slice, first 2 top-left coordinate of slice, last 2 bottom-right coordinate
        :param round_step: rounds results with given step, default 5
        """
        print("\n>>>>>> Printing values between {},{} and {},{} <<<<<<\n\n".format(coordinate[0], coordinate[1],
                                                                                   coordinate[2], coordinate[3]))

        for i in range(coordinate[0], coordinate[2]):
            # print("R{:3}".format(i),end='')
            print('[', end='')
            for j in range(coordinate[1], coordinate[3]):
                print("{:7},".format(round(self.__key_map[key][i][j], round_step)), end=' ')
            print(']', end='')
            print(",")

######################################################################################################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~  END of Summarize class  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
######################################################################################################
