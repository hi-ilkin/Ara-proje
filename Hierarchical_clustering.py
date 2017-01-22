# Ilkin Huseynli - 09.10.17
# Hierarchical_clustering

import numpy as np


def cluster(mat, sim_percent=0.7):
    """
    Single Linkage Hierarchical Clustering for given similarity matrix

    :param mat: numpy.ndarray , similarity matrix
    :param sim_percent: threshold percentage for clustering
    :return: returns list of labels. Each row demonstrates a cluster
    """

    label = []  # keeps clustered ids. Each row is a cluster
    sim_value = np.amax(mat)  # largest similarity value of the list
    threshold = sim_percent*sim_value # threshold is 70% percent of max value
    count = mat.shape[0]

    while sim_value >= threshold:
        # row and column value(s) of the list
        rows, cols = np.where(mat == sim_value)

        # if number of largest value is more than one
        for idx in range(len(rows)):
            index_of_Cluster1 = 0
            # print(rows[idx],cols[idx],">>",mat[rows[idx]][cols[idx]])
            # True if first value added to the list
            isFirstInList = False
            isSecondInList = False

            value1 = rows[idx]
            value2 = cols[idx]

            for line in label:

                # value1 is already in label list
                if value1 in line:
                    isFirstInList = True
                    # if value2 is in the same cluster with value 1
                    if value2 in line:
                        break           # don't do anything
                    else:
                        index_of_Cluster2 = 0
                        # check if value2 is in another cluster
                        for other_line in label:
                            if value2 in other_line:
                                label[index_of_Cluster1] += label[index_of_Cluster2]
                                del label[index_of_Cluster2]
                                isSecondInList = True
                                break
                            index_of_Cluster2 += 1

                    # value2 is not in the the list
                    if not isSecondInList:
                        # append value2
                        label[index_of_Cluster1].append(value2)

                index_of_Cluster1 += 1

            # first value is not in the list but we must check if second in the list
            if not isFirstInList:
                index_of_Cluster2 = 0
                isSecondInList = False
                for line in label:
                    if value2 in line:
                        label[index_of_Cluster2].append(value1)
                        isSecondInList = True
                        break
                    index_of_Cluster2 += 1

            # both values are not in the list
            if not isFirstInList and not isSecondInList:
                label.append([value1, value2])

            # changing max value to prevent double check
            mat[rows[idx]][cols[idx]] = -1.0
            # print(rows[idx],cols[idx],">>",mat[rows[idx]][cols[idx]])
        # next largest value of the list
        sim_value = np.amax(mat)

    # adding all remaining indexes as a 1 sample cluster
    for i in range(0, count):
        isAppended = False
        for line in label:
            if i in line:
                isAppended = True
        if not isAppended:
            label.append([i])

    return label
