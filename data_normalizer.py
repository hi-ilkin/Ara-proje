# ~~~~~~~~~~~~~~~~~~~~~ miniMax Normalization ~~~~~~~~~~~~~~~~~~~~~~~~~~~

import numpy as np
from sklearn import preprocessing

def minMax(train, local_max=1., local_min=0.):
    """Fit to data, then transform it.

           Fits transformer to X and y with optional parameters fit_params
           and returns a transformed version of X.

           Parameters
           ----------
           train: numpy array
                train set

           local_max: float
                    maximum value of normalizied set (default 1.)

           local_min: float
                    minimum value of normalizied set (default 0.)

           Returns
           -------
           trained: same shape numpy array with input
                    Normalizied set
           """

    trained = np.empty_like(train)      # creating empty copy of train dataset
    train_max = np.amax(train)          # maximum value of train set
    train_min = np.amin(train)          # minimum value of train set

    if train_min == train_max:
        return train

    else:
        denominator = train_min - train_max
        multiplier = (local_min - local_max)/denominator

        i = 0
        for line in train:
            for j in range(0, len(line)):
                normalized_value = (train[i][j] - train_min) * multiplier + local_min
                trained[i][j] = round(normalized_value, 3)
            i += 1
        return trained

def __test():
    X_train = np.array([[1., -1., 3., 4.],
                        [1., 0., 0., 4.],
                        [0., 1., -1., 3.]])

    print("+++++++++ Train Set +++++++++++")
    print(X_train)

    # print("\n+++++++++++++++ Their MinMax +++++++++++++++")
    min_max_scaler = preprocessing.MinMaxScaler()
    X_train_minmax = min_max_scaler.fit_transform(X_train)
    # print(X_train_minmax)

    # row,col = np.where(X_train == 3)
    # print(row,col)

    print("\n+++++++++ My MinMax +++++++++")
    print(minMax(X_train))

    # print ("\n++++++++++++++ Another test ++++++++++\n")
    # Y_train = np.array([1, -1, 3, 4])
    # print(myMinMax(Y_train))
