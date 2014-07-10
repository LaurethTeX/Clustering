# Clustering Methods

Since I found many ways of doing clustering with different tools and softwares I'm going to explain all off them
and show the results of each one, and later compare and discuss them.

## Color-Based Segmentation Using K-Means Clustering

I was surfing on the internet and I found [here](http://www.mathworks.com/help/images/examples/color-based-segmentation-using-k-means-clustering.html#zmw57dd0e2772) a way to do segmentation using a clustering technique so I decided to try it with my data.
To apply this technique the input data should be a RGB image, using the function [`mJPEG`](http://montage.ipac.caltech.edu/docs/mJPEG.html) of the Montage software. 
> For instructions of how to get Montage running click [here](https://github.com/LaurethTeX/Clustering/blob/master/Tools.md#montage)

### Chossing the images

We have 9 images at different wavelenghts, since we can only work with 3 we will choose:
* UV wide for the **BLUE** channel
* H-beta for the **GREEN** channel
* I-band (WFPC2 I) for the **RED** channel

> *The FITS files can be downloaded [here](http://archive.stsci.edu/prepds/wfc3ers/m83datalist.html).*

The total size of the images is 5000x8500 (x3) and we don't want to kill our 'standard' computer, to solve this I selected a sample area of 600x600 and created subimages from the original files with the Montage function [`mSubimage`](http://montage.ipac.caltech.edu/docs/mSubimage.html).
```
$ mSubimage -p uvwide.fits uvwideSample.fits 2300 3315 600 600
$ mSubimage -p hbeta.fits hbetaSample.fits 2300 3315 600 600
$ mSubimage -p iband.fits ibandSample.fits 2300 3315 600 600
```
The output message for all cases should be
```
[struct stat="OK", content="normal"]
```
> Remember that Montage commands should be executed in file directory. (i.e. `hyperion:WorkData Laureth$`)

Here is a preview of samples of the 3 images before being merged to one.

<html>
<body>

<img border="0" src="https://raw.githubusercontent.com/LaurethTeX/Clustering/master/uvwideSample.jpg" alt="uvwide" width="221" height="221">&nbsp;<img border="0" src="https://raw.githubusercontent.com/LaurethTeX/Clustering/master/hbetaSample.jpg" alt="hbeta" width="221" height="221">&nbsp;<img border="0" src="https://raw.githubusercontent.com/LaurethTeX/Clustering/master/ibandSample.jpg" alt="iband" width="221" height="221">
</body>
</html>

### [`mJPEG`](http://montage.ipac.caltech.edu/docs/mJPEG.html): Creating the RGB image with Montage

`mJPEG` generates a JPEG image file from a FITS file (or a set of three FITS files in color).
*Note: If creating a true color image, all input images must have identical WCS information (ie, same size, resolution, coordinate system, etc).*
```
$ mJPEG -t 2 -blue uvwideSample.fits 0s 99.999% gaussian -green hbetaSample.fits 0s 99.999% gaussian -red iband.fits 0s 99.999% gaussian -out RGBsample.jpg

[struct stat="OK", bmin=0.00369911, bminpercent=50.00, bmax=24.2607, bmaxpercent=100.00, gmin=0.00929061, gminpercent=50.00, gmax=4.66439, gmaxpercent=100.00, rmin=0.257658, rminpercent=50.00, rmax=35.1862, rmaxpercent=100.00]
```
And we get this RGB image,

<html>
<body>
<img border="0" src="https://raw.githubusercontent.com/LaurethTeX/Clustering/master/RGBsample.jpg" alt="uvwide" width="221" height="221">
<html>
<body>

Now we are ready to input on MATLAB our image.

### Read Image

### Convert Image from RGB Color Space to `L*a*b*` Color Space

### Classify the Colors in `a*b*` Space Using K-Means Clustering

### Label Every Pixel in the Image Using the Results from KMEANS

### Create Images that Segment the H&E Image by Color

### Segment the Nuclei into a Separate Image


...and I have now idea if this makes sense...
