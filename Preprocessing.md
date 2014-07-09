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

Check out the pages of the institutes who made your instrument, look for published papers in online databases like [The SAO/NASA Astrophysics Data System](http://adsabs.harvard.edu/abstract_service.html) or [Astro-ph](http://arxiv.org/archive/astro-ph).


Generate PSF convolution kernels
----------------- 
The Space Telescope Science Institute provides a marvellous sofwtare called [Tiny Tim](http://www.stsci.edu/hst/observatory/focus/TinyTim), here you can select your specific data parameters like camera and filter and the software will generate the PSF kernel you need.

The image cube: Our analyzable database
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


Missing data
---------------
In our data, as you can see in the image bellow it's an image made by mosaics and in some parts we have missing data.


<a href="url"><img src="https://raw.githubusercontent.com/LaurethTeX/Clustering/master/unoN.jpg" align="left" height="170" width="100" ></a>

