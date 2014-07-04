First Step: Data Pre-processing
=================

Why is this important?
-----------------
Imagine that you've got certain astronomical data, (for example purposes we will use [WFC3 ERS M83 Data Products](http://archive.stsci.edu/prepds/wfc3ers/m83datalist.html)) it is multi-wavelength data taken with different instruments which means that you will have a characteristic noise for each wavelength, differences on pixel size and resolutions, unnormalized data and maybe missing data in some areas... then how do you cluster that information?

First we must transform images to a common resolution, adjust pixel size. Then we must get rid of the noise, individually and at multi-wavelenght level.

Software available
-----------------
For this step I recommend [ImageCube](https://github.com/sophiathl/imagecube.git),
 which use packages like [Montage](http://montage.ipac.caltech.edu/index.html),
 [Sci-Kit Image](http://scikit-image.org/) and all of this is done in Python!
 
 Imagecube processes multi-wavelength astronomical imaging datasets, performing conversion to common flux units,
 registration to a common WCS, convolution to a common angular resolution, and regridding to a specified pixel size.
 
Find resolutions of all the FITS files (FWHM)

**Sure Andrea... this section is WRONG!**
----------------- 
We must calculate the [Full width at half maximum](http://mathworld.wolfram.com/FullWidthatHalfMaximum.html) (FWHM) value for each image, since the standard deviation is needed we use the [numpy.std](http://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html#numpy-std) function.
  ```python
import numpy as np
import pyfits

bband = pyfits.open('/.../bband.fits')
halpha = pyfits.open('/.../halpha.fits')
hbeta = pyfits.open('/.../hbeta.fits')
iband = pyfits.open('/.../iband.fits')
oii = pyfits.open('/.../oii.fits')
oiii = pyfits.open('/.../oiii.fits')
sii = pyfits.open('/.../sii.fits')
uband = pyfits.open('/.../uband.fits')
uvwide = pyfits.open('/.../uvwide.fits')

fwhm = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

fwhm[0] = np.std(np.array(bband[0].data),dtype=np.float64)*2.355
fwhm[1] = np.std(np.array(halpha[0].data),dtype=np.float64)*2.355
fwhm[2] = np.std(np.array(hbeta[0].data),dtype=np.float64)*2.355
fwhm[3] = np.std(np.array(iband[0].data),dtype=np.float64)*2.355
fwhm[4] = np.std(np.array(oii[0].data),dtype=np.float64)*2.355
fwhm[5] = np.std(np.array(oiii[0].data),dtype=np.float64)*2.355
fwhm[6] = np.std(np.array(sii[0].data),dtype=np.float64)*2.355
fwhm[7] = np.std(np.array(uband[0].data),dtype=np.float64)*2.355
fwhm[8] = np.std(np.array(uvwide[0].data),dtype=np.float64)*2.355

print "The FWHM values for WFC3 ERS M83 Data"
for x in range(0, 8):
    print "Band[%d] = %f" % (x,fwhm[x])
  ```
Therefore, the results are
  ```
The FWHM values for WFC3 ERS M83 Data
Band[0] = 0.576949
Band[1] = 0.216682
Band[2] = 0.101427
Band[3] = 1.355655
Band[4] = 0.301944
Band[5] = 0.193643
Band[6] = 0.152420
Band[7] = 0.367107
  ```
Since these values are **not** equal the next step will be to convolve so we can get images with common PSF.

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
