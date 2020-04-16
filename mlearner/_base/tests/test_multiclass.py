# Jaime Sendra Berenguer-2020
# MLearner Machine Learning Library Extensions
# Author:Jaime Sendra Berenguer<www.linkedin.com/in/jaisenbe>
#
# License: MIT

from mlearner._base import _MultiClass
import numpy as np


class BlankClassifier(_MultiClass):

    def __init__(self, print_progress=0, random_seed=1):
        self.print_progress = print_progress
        self.random_seed = random_seed


def test_default():
    y = np.array([0, 1, 2, 3, 4, 2])
    mc = BlankClassifier()
    expect = np.array([[1., 0., 0., 0., 0.],
                       [0., 1., 0., 0., 0.],
                       [0., 0., 1., 0., 0.],
                       [0., 0., 0., 1., 0.],
                       [0., 0., 0., 0., 1.],
                       [0., 0., 1., 0., 0.]], dtype='float')
    out = mc._one_hot(y=y, n_labels=5, dtype='float')
    np.testing.assert_array_equal(expect, out)


def test_oneclass():
    y = np.array([0, 0, 0])
    mc = BlankClassifier()
    out = mc._one_hot(y=y, n_labels=1, dtype='float')
    expect = np.array([[1.], [1.], [1.]])
    np.testing.assert_array_equal(expect, out)


def test_morelabels():
    y = np.array([0, 0, 1])
    mc = BlankClassifier()
    out = mc._one_hot(y=y, n_labels=4, dtype='float')
    expect = np.array([[1., 0., 0., 0.],
                       [1., 0., 0., 0.],
                       [0., 1., 0., 0.]])
    np.testing.assert_array_equal(expect, out)