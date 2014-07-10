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
> Full code can be found [here](https://github.com/LaurethTeX/Clustering/blob/master/TestMATLAB.m)

#### Read Image on MATLAB

Read in `RGBsample.jpg`, which is a sample of WFC3 ERS M83 Data Products with three wavelenghts.

```matlab
figure(1)
RGBsample = imread('RGBsample.jpg');
imshow(RGBsample),title('Messier-83');
text(size(RGBsample,2),size(RGBsample,1)+15,...
    'WFC3 ERS M83 DATA, http://archive.stsci.edu/prepds/wfc3ers/m83datalist.htm$
    'Fontsize',7,'HorizontalAlignment','right');
```
<html>
<body>
<img border="0" src="https://raw.githubusercontent.com/LaurethTeX/Clustering/master/fig1.png" alt="uvwide" width="510" height="458">
<html>
<body>
#### Convert Image from RGB Color Space to `L*a*b*` Color Space
The `L*a*b*` space consists of a luminosity layer `L*`, chromaticity-layer `a*` indicating where color falls along the red-green (in this particular case *Iband-Hbeta*) axis, and chromaticity-layer `b*` indicating where the color falls along the blue-yellow (*UVwide-Hbeta*) axis. All of the color information is in the `a*` and `b*` layers. You can measure the difference between two colors using the Euclidean distance metric.
```matlab
cform = makecform('srgb2lab');
lab_RGBsample = applycform(RGBsample,cform);
```
#### Classify the Colors in `a*b*` Space Using K-Means Clustering
Clustering is a way to separate groups of objects. K-means clustering treats each object as having a location in space. It finds partitions such that objects within each cluster are as close to each other as possible, and as far from objects in other clusters as possible.
Since the color information exists in the `a*b*` space, your objects are pixels with `a*` and `b*` values. Use kmeans to cluster the objects into three clusters using the Euclidean distance metric.
```matlab
ab = double(lab_RGBsample(:,:,2:3));
nrows = size(ab,1);
ncols = size(ab,2);
ab = reshape(ab,nrows*ncols,2);

nColors = 3;
% repeat the clustering 3 times to avoid local minima
[cluster_idx, cluster_center] = kmeans(ab,nColors,'distance','sqEuclidean', ...
                                      'Replicates',3);
```
#### Label Every Pixel in the Image Using the Results from KMEANS
For every object in your input, kmeans returns an index corresponding to a cluster. The `cluster_center` output from kmeans will be used later in the example. Label every pixel in the image with its `cluster_index`.
```matlab
pixel_labels = reshape(cluster_idx,nrows,ncols);
imshow(pixel_labels,[]), title('image labeled by cluster index');
```
<html>
<body>
<img border="0" src="https://raw.githubusercontent.com/LaurethTeX/Clustering/master/allcluster.png" alt="uvwide" width="510" height="458">
<html>
<body>

#### Create Images that Segment the RGB sample Image by Color
Using `pixel_labels`, you can separate objects in `RGBsample.jpg` by color, which will result in three images.
```matlab
segmented_images = cell(1,3);
rgb_label = repmat(pixel_labels,[1 1 3]);

for k = 1:nColors
    color = RGBsample;
    color(rgb_label ~= k) = 0;
    segmented_images{k} = color;
end

imshow(segmented_images{1}), title('objects in cluster 1');
imshow(segmented_images{2}), title('objects in cluster 2');
imshow(segmented_images{3}), title('objects in cluster 3');
```
<html>
<body>

<img border="0" src="https://raw.githubusercontent.com/LaurethTeX/Clustering/master/cluster1.png" alt="uvwide" width="510" height="458">&nbsp;<img border="0" src="https://raw.githubusercontent.com/LaurethTeX/Clustering/master/cluster2.png" alt="uvwide" width="510" height="458">&nbsp;<img border="0" src="https://raw.githubusercontent.com/LaurethTeX/Clustering/master/cluster3.png" alt="uvwide" width="510" height="458">

<body>

**...and I have now idea if this makes sense... :confounded:**
