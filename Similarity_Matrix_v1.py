import numpy as np
import data_normalizer as nz

class Similarity_Matrix:
    __term_level_sim = []  # term level similarity graph
    __semantic_sim = []  # semantic similarity graph
    __similarity_graph = [] # total similarity = term + semantic
    __tweets = []  # a list that keeps all tweets
    __normilize_max = 10
    __normilize_min = 0

    def initialize(self, tweet_count):
        self.__term_level_sim = np.zeros((tweet_count, tweet_count))
        self.__semantic_sim = np.zeros((tweet_count, tweet_count))
        # total similarity between tweets = term_level + semantic
        self.__similarity_graph = np.zeros((tweet_count, tweet_count))

    # ~~~~~~~~~~~~~ term level similarity ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get__term_level_sim(self, *args):

        # returns all similarity matrix
        if len(args) == 0:
            return self.__term_level_sim

        # returns list of similarity vaules with tweet row
        elif len(args) == 1:
            row = args[0]
            return self.__term_level_sim[row]

        # returns similarity value between tweets row and col
        elif len(args) == 2:
            row = args[0]
            col = args[1]
            return self.__term_level_sim[row][col]

        else:
            raise ValueError("get__term_level_sim is excpected at most 2 args but got {}.".format(len(args)))

    def set__term_level_sim(self, row, col, value):
        """ Sets value to the given index"""
        if value == -1:
            pass  # if value is -1, this means that we are passing these tweets
        elif not value.isNumeric():
            raise TypeError('Value must be numeric!')
        else:
            self.__term_level_sim[row][col] = value
            self.__term_level_sim = nz.minMax(self.__term_level_sim, self.__normilize_max, self.__normilize_min)

    def increase_term_level_sim(self, row, col, inc_value):
        """ Increases term level similarity value with given value.
            After all values added, normalizes all values

        :param row: row value in similarity matrix or row-th tweet
        :param col: col value in similarity matrix or col-th tweet
        :param inc_value: increment value
        """
        self.__term_level_sim[row][col] += inc_value
        # normalization version
        # if row == self.tweet_len() - 2 and col == self.tweet_len() - 1:
        #     self.__term_level_sim[row][col] += inc_value
        #     print("Before normilize ,{}-{}".format(row,col))
        #     self.printSlice(self.__term_level_sim, [250, 250, 255, 255])
        #     self.__term_level_sim = nz.minMax(self.__term_level_sim, self.__normilize_max, self.__normilize_min)
        #     print("\nAfter normilize ")
        #     self.printSlice(self.__term_level_sim, [250, 250, 255, 255])
        #
        # else:
        #     self.__term_level_sim[row][col] += inc_value

    # ~~~~~~~~~~~~~~~~~~~~ semantic similarity ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def get__semantic_sim(self, *args):

        # returns all similarity matrix
        if len(args) == 0:
            return self.__semantic_sim

        # returns list of similarity vaules with tweet row
        elif len(args) == 1:
            row = args[0]
            return self.__semantic_sim[row]

        # returns similarity value between tweets row and col
        elif len(args) == 2:
            row = args[0]
            col = args[1]
            return self.__semantic_sim[row][col]

        else:
            raise ValueError("get__semantic_level_sim is excpected at most 2 args but got {}.".format(len(args)))

    def set__semantic_sim(self, row, col, value):
        """ Sets value to the given index"""
        if value == -1:
            pass  # if value is -1, this means that we are passing these tweets
        elif not value.isNumeric():
            raise TypeError('Value must be numeric!')
        else:
            self.__semantic_sim[row][col] = value

    def increase__semantic_sim(self, row, col, inc_value):
        self.__semantic_sim[row][col] += inc_value

    def __isPrivate(self):
        print("You called a private func")

        # ~~~~~~~~~~~~~final similarity ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get__similarity_graph(self, *args):

        # returns all similarity matrix
        if len(args) == 0:
            return self.__similarity_graph

        # returns list of similarity vaules with tweet row
        elif len(args) == 1:
            row = args[0]
            return self.__similarity_graph[row]

        # returns similarity value between tweets row and col
        elif len(args) == 2:
            row = args[0]
            col = args[1]
            return self.__similarity_graph[row][col]

        else:
            raise ValueError("get__term_level_sim is excpected at most 2 args but got {}.".format(len(args)))

    def create_similarity_graph(self):
        self.__similarity_graph = self.__term_level_sim + self.__semantic_sim
    # ~~~~~~~~~~~~~~~~~~~~~~ Tweets ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def get__tweets(self, *args):

        if len(args) == 0:
            return self.__tweets

        elif len(args) > 1:
            raise ValueError("get_tweets expected at most 1 argument got {} .".format(len(args)))

        else:
            index = args[0]
            return self.__tweets[index]

    def tweet_len(self):
        return len(self.__tweets)

    # ~~~~~~~~~~~~~~~~~~ reading file ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def openFile(self, fin_name):
        # opening file
        try:
            fin = open(fin_name, 'r')
        except IOError as e:
            print("Something bad happened with files:\n", e)
            exit(-1)

        # reading all file to a list, so working on them will be easier
        for line in fin:
            line = line.lower()  # case fold all tweets
            line = line.strip()  # strip blank spaces from starting and end
            self.__tweets.append(line)

    def printSlice(self, matrix, coordinate=[0, 0, 99, 99], round_step=5):
        """
        Prints given part of matrix to the screen
        :param matrix: name of the matrix
        :param coordinate: print slice, first 2 top-left coordinate of slice, last 2 bottom-right coordinate
        :param round_step: rounds results with given step, default 5
        """
        print("\n>>>>>> Printing values between {},{} and {},{} <<<<<<\n".format(coordinate[0], coordinate[1], coordinate[2], coordinate[3]))

      #  print("Column> ", end='')
      #   for j in range(coordinate[1], coordinate[3]):
           # print("C{:3}".format(j), end='')
           # print("  ", end="")
        print()

        for i in range(coordinate[0], coordinate[2]):
            #print("R{:3}".format(i),end='')
            print('[',end='')
            for j in range(coordinate[1], coordinate[3]):
                print("{:7},".format(round(matrix[i][j], round_step)), end=' ')
            print(']',end='')
            print(",")

######################################################################################################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~  END of Summarize class  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
######################################################################################################