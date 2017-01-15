#############################################################################
#~~~~~~~~ COPMUTER PROJECT - Tweet classification and summarization ~~~~~~~~#
#############################################################################
#~~~~~~~~~~~~~~~~~~~~~ Author : Ilkin Huseynli ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#############################################################################
# References:
# 1 - https://www.tutorialspoint.com/python/python_reg_expressions.htm
# 2 - https://docs.python.org/3/howto/regex.html
# 3 - http://www.nltk.org/book/ch02.html
# 4 - http://www.cs.waikato.ac.nz/ml/weka/arff.html


import re
import numpy as np

# opening proper file


#~~~~~~~~~~~~~~~~~~~~~~~~ END of FOR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

print(str)


splitted_string = str.splitlines()  # split lines
splitted_len = len(splitted_string)  # length of splitted array

#################### MATCH vs SEARCH #########################################

# match checks for a match only at the beginning of the string, while search checks for a match anywhere in the string (this is what Perl does by default).

##############################################################################

url_similarity = np.zeros((splitted_len, splitted_len))

# url similarity:
# for line in splitted_string:
#     matchObj = re.search('http[s]*://[^\s]*', line, re.I)
#     if (matchObj):
#         for line_2 in splitted_string:
#             if(re.findall(matchObj.group(0),line_2) and line != line_2):
#                 print("Line ",splitted_string.index(line), ": ",line)
#                 print("Line ",splitted_string.index(line_2),": ",line_2,"\n")
#                 url_similarity[splitted_string.index(line)][                                                                splitted_string.index(line_2)]




# writing to a file
fo = open("splt.txt", "w")
for line in splitted_string:
    fo.write(line + "\n")
# print(st)
