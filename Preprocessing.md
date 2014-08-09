First Step: Data Pre-processing
=================

Why is this important?
-----------------
Imagine that you've got certain astronomical data, (for example purposes we will use [WFC3 ERS M83 Data Products](http://archive.stsci.edu/prepds/wfc3ers/m83datalist.html)) it is multi-wavelength data taken with different instruments which means that you will have a characteristic noise for each wavelength, differences on pixel size and resolutions, unnormalized data and maybe missing data in some areas... then how do you cluster that information?

First we must transform images to a common resolution, adjust pixel size. Then we must get rid of the noise, individually and at multi-wavelenght level.

Data pre-processing is often problem-independent, and should be carefully applied because the results of many data mining algorithms can be significantly affected by the input data.

Software available
-----------------
For this step I recommend [ImageCube](https://github.com/sophiathl/imagecube.git),
 which use packages like [Montage](http://montage.ipac.caltech.edu/index.html),
 [Sci-Kit Image](http://scikit-image.org/) and all of this is done in Python!
 
 Imagecube processes multi-wavelength astronomical imaging datasets, performing conversion to common flux units,
 registration to a common WCS, convolution to a common angular resolution, and regridding to a specified pixel size.
 
Find resolutions of all the FITS files (FWHM)
----------------- 
First of all, is recomendable to remind your knowledge about convolution and learn about PSF, [here](http://www.jstor.org/stable/pdfplus/10.1086/662219.pdf?acceptTC=true) you will find a helpful paper.

The strategy here is to look for your particular instrument information, in this case I'm looking for the WFC3 UVIS channel which is in [this](http://www.stsci.edu/institute/org/telescopes/Reports/ISR-TEL-2010-01) document.

*Where you look?*

Check out the pages of the instrument's handbook, in this case the Wide Field Camera 3 Instrument Handbookfor Cycle 22, specifically you can find the FWHM of each wavelenght [here](http://www.stsci.edu/hst/wfc3/documents/handbooks/currentIHB/c06_uvis07.html#391844).

Remember that we are looking for the poorest spatial resolution which means the largest FWHM, with our particular data this value corresponds to **0.083 arcsec/pixel.**


Generate PSF convolution kernels
----------------- 
The Space Telescope Science Institute provides a marvellous sofwtare called [Tiny Tim](http://www.stsci.edu/hst/observatory/focus/TinyTim), here you can select your specific data parameters like camera and filter and the software will generate the PSF kernel you need.

Another way is to generate a gaussian kernel, which is what you do when you don't find the appropiate kernel database or Tiny Tim is taking too longo to calculate your kernel. The way that you can calcute it is explained below,
```python
import from astropy.convolution import Gaussian2DKernel
native_pixelscale = 0.0396 # arcsec/pixel
fwhm_input = 0.083 # arcsec
sigma_input = (fwhm_input / (2* math.sqrt(2*math.log (2) ) * native_pixelscale))
gaus_kernel_inp = Gaussian2DKernel(width=sigma_input)
```

Convolve all images to the same spatial resolution
------------------
Since our images have different spatial resolution a convolution is necessary, with the help of Astropy this is a simple step,
```python
import from astropy.convolution import convolve
conv_result = convolve(data, gaus_kernel_inp)
```
And we should apply this step to all of our images, the code I used for this can be found [here](https://github.com/LaurethTeX/Clustering/blob/master/convolution.py), and as you can see below, the image on the left in an expample of the result you get after applying the convolution to the B-band image and the image on the right is the original image.
![CONV](https://raw.githubusercontent.com/LaurethTeX/Clustering/bce9a87a243002b553fdeafa3b8e92f105a3e513/conv.jpg)

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
