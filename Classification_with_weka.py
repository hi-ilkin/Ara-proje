# ~~~~~~~~~~ weka ~~~~~~~~~~~~~~~~~~~~~~~
import weka.core.jvm as jvm
from weka.classifiers import Classifier
from weka.core.converters import Loader
from weka.core.classes import split_options as split
import create_arff

def classify():

    create_arff.createArff()
    jvm.start()  # bunu UNUTMA !!!!

    # loading dataset -
    loader = Loader(classname="weka.core.converters.ArffLoader")

    data = loader.load_file("train.arff")
    test_data = loader.load_file("test.arff")

    data.class_is_last()
    test_data.class_is_last()

    # for J48
    # option = split(
    #     'weka.classifiers.trees.J48 -C 0.25 -M 2')
    # print(option)
    # cls = Classifier(classname=option[0], options=option[1:])
    #
    # # building classifier
    # cls.build_classifier(data)

    ######################################3
    # for SMO

    # cmdline ='weka.classifiers.meta.FilteredClassifier -F "weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -stopwords-handler weka.core.stopwords.Null -M 1 -tokenizer \"weka.core.tokenizers.WordTokenizer -delimiters \\\" \\\\r\\\\n\\\\t.,;:\\\\\\\'\\\\\\\"()?!\\\"\"" -W weka.classifiers.functions.SMO -- -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -V -1 -W 1 -K "weka.classifiers.functions.supportVector.PolyKernel -E 1.0 -C 250007" -calibrator "weka.classifiers.functions.Logistic -R 1.0E-8 -M -1 -num-decimal-places 4"'
    # cmdline = 'weka.classifiers.meta.FilteredClassifier -F "weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -stopwords-handler weka.core.stopwords.Null -M 1 -tokenizer \"weka.core.tokenizers.WordTokenizer -delimiters \\\" \\\\r\\\\n\\\\t.,;:\\\\\\\'\\\\\\\"()?!\\\"\"" -W weka.classifiers.bayes.NaiveBayes'
    cmdline = 'weka.classifiers.meta.FilteredClassifier -F \"weka.filters.unsupervised.attribute.StringToWordVector -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -stopwords-handler weka.core.stopwords.Null -M 1 -tokenizer \\\"weka.core.tokenizers.WordTokenizer -delimiters \\\\\\\" \\\\\\\\r\\\\\\\\n\\\\\\\\t.,;:\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\"()?!\\\\\\\"\\\"\" -W weka.classifiers.functions.SMO -- -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -V -1 -W 1 -K \"weka.classifiers.functions.supportVector.PolyKernel -E 1.0 -C 250007\" -calibrator \"weka.classifiers.functions.Logistic -R 1.0E-8 -M -1 -num-decimal-places 4\"'
    option =split(cmdline)

    cls = Classifier(classname=option[0], options=option[1:])
    cls.build_classifier(data)

    # calssification
    for index, inst in enumerate(test_data):
        pred = cls.classify_instance(inst)
        dist = cls.distribution_for_instance(inst)
        print(str(index+1) + ": label index=" + str(pred) + ", class distribution=" + str(dist))

    # print(data)

    jvm.stop()
