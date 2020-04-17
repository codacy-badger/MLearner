# Jaime Sendra Berenguer-2020
# MLearner Machine Learning Library Extensions
# Author:Jaime Sendra Berenguer<www.linkedin.com/in/jaisenbe>
#
# License: MIT

from .decision_regions import plot_decision_regions
from .learning_curves import plot_learning_curves
from .plot_confusion_matrix import plot_confusion_matrix
from .plot_sequential_feature_selection\
    import plot_sequential_feature_selection
from .plot_linear_regression import plot_linear_regression
from .remove_chartjunk import remove_borders
from .scatter import category_scatter
from .heatmap import heatmap
from .stacked_barplot import stacked_barplot
from .enrichment_plot import enrichment_plot
from .checkerboard import checkerboard_plot
from .ecdf import ecdf
from .scatterplotmatrix import scatterplotmatrix
from .pca_correlation_graph import plot_pca_correlation_graph


__all__ = ["plot_learning_curves",
           "plot_decision_regions",
           "plot_confusion_matrix",
           "plot_sequential_feature_selection",
           "plot_linear_regression",
           "remove_borders",
           "category_scatter",
           "heatmap",
           "stacked_barplot",
           "enrichment_plot",
           "checkerboard_plot",
           "ecdf",
           "scatterplotmatrix",
           "plot_pca_correlation_graph"]
