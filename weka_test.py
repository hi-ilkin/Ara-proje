# import weka.core.jvm as jvm
#
# jvm.start()

from weka.core.converters import Loader

# data_dir = 'F:/Internet Explorer/Ders/Ara proje/Kodlama/processed_data'
# loader = Loader(classname="weka.core.converters.ArffLoader")
# data = loader.load_file(data_dir + "nagano_processed_file.arff")
# data.class_is_last()

# print(data)
# # print(vs)
# from sklearn import svm
#
# X = [[0, 0], [1, 1]]
# y = [0, 1]
# clf = svm.SVC()
# clf.fit(X, y)
# svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#     decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
#     max_iter=-1, probability=False, random_state=None, shrinking=True,
#     tol=0.001, verbose=False)
#
# clf.predict([[2., 2.]])
# array([1])