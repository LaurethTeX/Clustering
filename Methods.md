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

Here is a preview of samples of the 3 images before being merged to one. 

> *I got this images just by saving the JPG file in DS9, they are blue just because is my favourite colour there is no relation with the RGB color space.*
<html>
<body>

<img border="0" src="https://raw.githubusercontent.com/LaurethTeX/Clustering/master/uvwideBLUE.jpg" alt="uvwide" width="221" height="130">&nbsp;<img border="0" src="https://raw.githubusercontent.com/LaurethTeX/Clustering/master/hbetaBLUE.jpg" alt="hbeta" width="221" height="130">&nbsp;<img border="0" src="https://raw.githubusercontent.com/LaurethTeX/Clustering/master/ibandBLUE.jpg" alt="iband" width="221" height="130">
</body>
</html>

### [`mJPEG`](http://montage.ipac.caltech.edu/docs/mJPEG.html): Creating the RGB image with Montage

`mJPEG` generates a JPEG image file from a FITS file (or a set of three FITS files in color). A data range for each image can be defined, and the data can be stretched by any power of the log() function (including zero: linear). Pseudo-color color tables can be applied in single-image mode.
*Note: If creating a true color image, all input images must have identical WCS information (ie, same size, resolution, coordinate system, etc).*
The FITS files to be used are:
* UV wide
* H-beta
* I-band
