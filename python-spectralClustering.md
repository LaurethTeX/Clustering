## Spectral clustering

I found this technique programmed in Python [here](http://scikit-learn.org/stable/auto_examples/cluster/plot_lena_segmentation.html#example-cluster-plot-lena-segmentation-py), let's see what comes out from this.

This procedure (spectral clustering on an image) is an efficient approximate solution for finding normalized graph cuts.
There are two options to assign labels:
with ‘kmeans’ spectral clustering will cluster samples in the embedding space using a kmeans algorithm
whereas ‘discrete’ will iteratively search for the closest partition space to the embedding space.

The changes I made to the example program are these,
```python
import pyfits

lenaFITS = pyfits.open('/Users/Laureth/Documents/Papers/WorkData/hbetaSample.fits')
lenafloat32 = lenaFITS[0].data
lena1 = np.array(lenafloat32, dtype=np.int64)
lena = exposure.rescale_intensity(lena1, out_range=(0, 4096))
```
This was necessary because the data we wish to cluster is from FITS files, an intensity rescaling was required and it was modified just fro testing the data.

The output images were the following,
<html>
<body>

<img border="0" src="https://raw.githubusercontent.com/LaurethTeX/Clustering/master/clustertest1-1.png" alt="uvwide" width="360" height="292">&nbsp;<img border="0" src="https://raw.githubusercontent.com/LaurethTeX/Clustering/master/clustertest1-2.png" alt="hbeta" width="360" height="292">
</body>
</html>
