## Spectral clustering

I found this technique programmed in Python [here](http://scikit-learn.org/stable/auto_examples/cluster/plot_lena_segmentation.html#example-cluster-plot-lena-segmentation-py), let's see what comes out from this.

This procedure (spectral clustering on an image) is an efficient approximate solution for finding normalized graph cuts.
There are two options to assign labels:
with ‘kmeans’ spectral clustering will cluster samples in the embedding space using a kmeans algorithm
whereas ‘discrete’ will iteratively search for the closest partition space to the embedding space.
