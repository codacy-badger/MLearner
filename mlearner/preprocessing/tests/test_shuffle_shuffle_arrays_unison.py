# Jaime Sendra Berenguer-2020
# MLearner Machine Learning Library Extensions
# Author:Jaime Sendra Berenguer<www.linkedin.com/in/jaisenbe>
#
# License: MIT


import numpy as np
from mlearner.preprocessing import shuffle_arrays_unison


def test_shuffle_arrays_unison():
    X1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    y1 = np.array([1, 2, 3])

    X2, y2 = shuffle_arrays_unison(arrays=[X1, y1], random_seed=3)

    assert(X2.all() == np.array([[4, 5, 6], [1, 2, 3], [7, 8, 9]]).all())
    assert(y2.all() == np.array([2, 1, 3]).all())