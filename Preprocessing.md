First Step: Data Pre-processing
=================

Why is this important?
-----------------
Imagine that you've got astronomical data, (for example purposes we will use [WFC3 ERS M83 Data Products](http://archive.stsci.edu/prepds/wfc3ers/m83datalist.html)) it is multi-wavelength data taked by diferent instruments which means that you will have a characteristic noise for each wavelength, differences on pixel size, unnormalized data and maybe missing data in some areas... then how do you cluster that information?

Firts we must get rid of the noise, adjust resolution and pixel size to all our images. Then we must get rid of the noise, individually and at multi-wavelenght level 

Software available
-----------------
For this step I recommend [ImageCube](https://github.com/sophiathl/imagecube.git),
 which use packages like [Montage](http://montage.ipac.caltech.edu/index.html),
 [Sci-Kit Image](http://scikit-image.org/) and all of this is done in Python!
 
 Imagecube processes multi-wavelength astronomical imaging datasets, performing conversion to common flux units,
 registration to a common WCS, convolution to a common angular resolution, and regridding to a specified pixel size.
 
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
