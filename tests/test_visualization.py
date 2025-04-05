# tests/test_visualization.py

import matplotlib.pyplot as plt
from matplotlib.testing.decorators import check_figures_equal
from src.visualization import visualize

@check_figures_equal()
def test_plot_function(fig_test, fig_ref):
    # Reference plot
    ax_ref = fig_ref.subplots()
    ax_ref.plot([0, 1], [0, 1], label="Reference")
    ax_ref.legend()

    # Test plot
    ax_test = fig_test.subplots()
    visualize.plot_function(ax=ax_test)
