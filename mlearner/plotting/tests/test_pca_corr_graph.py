import pytest
from mlearner.plotting import plot_pca_correlation_graph
from mlearner.data import iris_data
from sklearn.decomposition.pca import PCA


def test_pass_pca_corr():
    X, y = iris_data()
    plot_pca_correlation_graph(X, variables_names=['1', '2', '3', '4'])


def test_pass_pca_corr_pca_out():
    X, y = iris_data()
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    eigen = pca.explained_variance_

    plot_pca_correlation_graph(X, variables_names=['1', '2', '3', '4'],
                               X_pca=X_pca, explained_variance=eigen)


def test_X_PCA_but_no_explained_variance():
    with pytest.raises(
            ValueError,
            match='If `X_pca` is not None, the `explained variance` '
                  'values should not be `None`.'):

        X, y = iris_data()
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X)

        plot_pca_correlation_graph(X, variables_names=['1', '2', '3', '4'],
                                   X_pca=X_pca, explained_variance=None)


def test_no_X_PCA_but_explained_variance():
    with pytest.raises(
            ValueError,
            match='If `explained variance` is not None, the '
                  '`X_pca` values should not be `None`.'):

        X, y = iris_data()
        pca = PCA(n_components=2)
        pca.fit(X)
        eigen = pca.explained_variance_

        plot_pca_correlation_graph(X, variables_names=['1', '2', '3', '4'],
                                   X_pca=None, explained_variance=eigen)


def test_not_enough_components():
    s = ('Number of principal components must match the number of eigenvalues. Got 2 != 1')
    with pytest.raises(
            ValueError,
            match=s):

        X, y = iris_data()
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X)
        eigen = pca.explained_variance_

        plot_pca_correlation_graph(X, variables_names=['1', '2', '3', '4'],
                                   X_pca=X_pca,
                                   explained_variance=eigen[:-1])
        