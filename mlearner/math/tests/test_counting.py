# Jaime Sendra Berenguer-2020
# MLearner Machine Learning Library Extensions
# Author:Jaime Sendra Berenguer<www.linkedin.com/in/jaisenbe>
#
# License: MIT


from mlearner.math import factorial
from mlearner.math import num_permutations
from mlearner.math import num_combinations


def test_factorial():
    assert(factorial(1) == 1)
    assert(factorial(3) == 6)


def test_num_combinations():
    assert(num_combinations(n=20, k=8, with_replacement=False) == 125970)
    assert(num_combinations(n=20, k=8, with_replacement=True) == 2220075)
    print(num_combinations(n=300, k=10))
    assert(num_combinations(n=300, k=10, with_replacement=False)
           == 1398320233241701770)


def test_num_permutations():
    assert(num_permutations(n=20, k=8, with_replacement=False) == 5079110400)
    assert(num_permutations(n=20, k=8, with_replacement=True) == 25600000000)