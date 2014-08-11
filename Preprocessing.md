First Step: Data Pre-processing
=================

Why is this important?
-----------------
Imagine that you've got certain astronomical data, (for example purposes we will use [WFC3 ERS M83 Data Products](http://archive.stsci.edu/prepds/wfc3ers/m83datalist.html)) it is multi-wavelength data taken with different filters which means that you will have a characteristic noise for each wavelength, differences on pixel size and resolutions, unnormalized data and maybe missing data in some areas... then how do you cluster that information?

First we must transform images to a common spatial resolution, adjust pixel size. Then we must get rid of the noise, individually and at multi-wavelenght level.

Data pre-processing is often problem-independent, and should be carefully applied because the results of many data mining algorithms can be significantly affected by the input data.

What do we need you do to get our data ready for processing?
-----------------
* Find the FWHM for each image
* Transform images to the same spatial resolution
* Elimintate outliers and noise
* Organize the data in a way that the clustering algorithm can read it. (i.e. image cube, arrays)
 
Now ... in theory you're ready to test your algorithms and increase the probabilites of getting a good outcome from the clustering algorithms.

Software available
-----------------
To tackle this astornomy image processing problem there are many softwares available, or you can just create your own using Astropy, PyFITS and Montage, pernsonally I recommend [ImageCube](https://github.com/sophiathl/imagecube.git),
 which use packages before mentioned and does all the work, and you can concentrate on the processing part.
 
 Imagecube processes multi-wavelength astronomical imaging datasets, performing conversion to common flux units,
 registration to a common WCS, convolution to a common angular resolution, and regridding to a specified pixel size.
 
 Now let's get started with the data-preprocessing work!
 
Find resolutions of all the FITS files (FWHM)
----------------- 
First of all, is recomendable to remind your knowledge about convolution and learn about PSF, [here](http://www.jstor.org/stable/pdfplus/10.1086/662219.pdf?acceptTC=true) you will find a helpful paper.

**What is PSF (Point spread function) ?**

Applied to this specific problem, the PSF is a matrix that cointains the information about the way that light is spread on each light-source on an image. Images of an object appear in the detector as the convolution of the true object with the system PSF.
The PSF is shape of a star (or point source) as imaged by the telescope.

![conv](https://raw.githubusercontent.com/LaurethTeX/Clustering/c984066ad84abfbd090745092fdfa041ea9f5998/ConvolutionSimp_1.png)

As you can see in the illustration above an image is simply the intensity of the object weighted by the PSF.

For more information review [this](http://exoplanet.as.arizona.edu/~lclose/a302/lecture9/Lecture_9.html) webpage.

The strategy to find the FWHM is to look for your particular instrument information, in this case I'm looking for the WFC3 UVIS channel which is in [this](http://www.stsci.edu/institute/org/telescopes/Reports/ISR-TEL-2010-01) document.

**What if FWHM? (Full width at half maximum)**
The best way to explain this is with a picture, now imagine that the function that you see in the picture below is your PSF.

![fwhm](https://raw.githubusercontent.com/LaurethTeX/Clustering/9e5b09002afd67628b3780ac83ed9a1fd42562e1/360px-FWHM.png)

**Where you look?**

Check out the pages of the instrument's handbook, in this case the Wide Field Camera 3 Instrument Handbookfor Cycle 22, specifically you can find the FWHM of each wavelenght [here](http://www.stsci.edu/hst/wfc3/documents/handbooks/currentIHB/c06_uvis07.html#391844).

Remember that we are looking for the poorest spatial resolution which means the largest FWHM, with our particular data this value corresponds to **0.083 arcsec/pixel** which corresponds to 200nm in the UV wide filter.


Transform images to the same spatial resolution
----------------- 
**Find your native pixel scale**

For this particular image dataset the WFC3 UVIS mosaics have the native detector scale of 0.0396 arcsec/pixel, as you can see in the [webpage](http://archive.stsci.edu/prepds/wfc3ers/m83datalist.html) where you can download the images.

When this mumber in hidden from you and you can't find it anywhere, you can use `imagecube` and it will calculate this number for you.
```python

import imagecube
import pyfits

image = pyfits.open('yourfile.fits')
native_pixel_scale = get_pixel_scale(image[0].header):

```

**Calculate the convolution kernel**

The Space Telescope Science Institute provides a marvellous sofwtare called [Tiny Tim](http://www.stsci.edu/hst/observatory/focus/TinyTim), here you can select your specific data parameters like camera and filter and the software will generate the PSF kernel you need.

Another way is to generate a gaussian kernel, which is what you do when you don't find the appropiate kernel database or Tiny Tim is taking too long to calculate your kernel. The way is explained below,
```python
import from astropy.convolution import Gaussian2DKernel
native_pixelscale = 0.0396 # arcsec/pixel
fwhm_input = 0.083 # arcsec
sigma_input = (fwhm_input / (2* math.sqrt(2*math.log (2) ) * native_pixelscale))
gaus_kernel_inp = Gaussian2DKernel(width=sigma_input)
```

**Convolve all images to the same spatial resolution**

Since our images have different spatial resolution a convolution is necessary, with the help of Astropy this is a simple step,
```python
import from astropy.convolution import convolve
conv_result = convolve(data, gaus_kernel_inp)
```
And we should apply this step to all of our images, the code I used for this can be found [here](https://github.com/LaurethTeX/Clustering/blob/master/convolution.py), and as you can see below, the image on the left in an expample of the result you get after applying the convolution to the B-band image and the image on the right is the original image.
![CONV](https://raw.githubusercontent.com/LaurethTeX/Clustering/bce9a87a243002b553fdeafa3b8e92f105a3e513/conv.jpg)

Elimintate outliers and noise
-----------------
****

The imagecube: Our analyzable database
------------------
Since we have various images of the same target taken at different wavelenghts, we can append them into a single [FITS](http://fits.gsfc.nasa.gov/fits_wcs.html) file and get the database ready to be analized by the clustering algorithms. 
The image cube in this particular case will conitain a header that cointains the conventions defined to specify the physical, or world, coordinates to be attached to each pixel of an N-dimensional image and our multiwavelength data (5000x8500x9).

Get ImageCube running
-----------------
1. Clone in desktop the [ImageCube](https://github.com/sophiathl/imagecube.git) GitHub repository
2. Install [montage_wrapper](http://www.astropy.org/montage-wrapper/)

  ```
  pip install montage-wrapper
  ```
3. Make sure montage-wrapper runs properly

  ```
  ipython
  >>> import montage_wrapper as montage
  >>> montage.mArchiveList('2MASS', 'K', 'm31', 0.5, 0.5, 'm31.tbl')
  count : 18
  stat : OK
  ```
4. In your terminal go to,

  ```
   cd /../..*file location*../imagecube
  ```
5. Try typing

  ```
  ipython
  >>>  import imagecube
  ```
  
If nothing happens means everything is going alright but if you get a message like,

  ```
  ---------------------------------------------------------------------------
  ImportError                               Traceback (most recent call last)
  <ipython-input-1-1341f20e21c8> in <module>()
  ----> 1 import imagecube
  
  ImportError: No module named imagecube
  ```
  
means something went wrong, review the former steps, if you can't solve the problem post an issue at GitHub.

You must also make sure that you have already installed *Astropy*, *Numpy*, *SciPy* and *Matplotlib* if not review the section [Tools](https://github.com/LaurethTeX/Clustering/blob/master/Tools.md) of this repository.
