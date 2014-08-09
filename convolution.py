import math
import numpy as np
import pyfits as pf
import matplotlib.pyplot as plt
from astropy.convolution import convolve, Gaussian2DKernel

#Plot FWHM
#def plotFWHM():    
#    wvlght = [200,300,400,500,600,700,800,900,1000,1100]
#    fwhm_arcsec = [0.083,0.075,0.070,0.067,0.067,0.070,0.074,0.078,0.084,0.089]
#    ax = plt.axes()
#    ax.plot(wvlght,fwhm_arcsec)
#    ax.set_xlim(200,1100)
#    ax.set_ylim(0.060,0.095)
#    ax.set_xlabel('Wavelength (nm)')
#    ax.set_ylabel('FWHM (arcsec)')
#    ax.set_title('WFC3/UVIS PSF FWHM')

# Get Gaussian Kernel
def getkernel(fwhm_input):
    native_pixelscale = 0.0396 # arcsec/pixel
    sigma_input = (fwhm_input / (2* math.sqrt(2*math.log (2) ) * native_pixelscale))
    gaus_kernel_inp = Gaussian2DKernel(width=sigma_input)
    print 'Gausian Kernel Calculated'
    return gaus_kernel_inp

class imagelayer(object):
    native_pixelscale = 0.0396 # arcsec/pixel
    def __init__(self,name):  
        self.name = name
        fits = pf.open(name)
        self.rawdata = fits[0].data
        self.header = fits[0].header
        fits.close()
         
    def convolve(self,gaus_kernel_inp,fwhm_input):
        conv_result = convolve(self.rawdata, gaus_kernel_inp)
        self.header['FWHM'] = (fwhm_input,'FWHM value used in convolution, in pixels')
        hdu = pf.PrimaryHDU(conv_result,self.header)
        hdu.writeto(self.name[0:-5]+'_conv.fits', clobber=True)
        
def main():
    
    f = 0.083
    k = getkernel(f)
    
    print 'Initializing Convolutions'
    bb = imagelayer('bband.fits')
    bb.convolve(k,f)
    print 'B-band convolved'
    
    ha = imagelayer('halpha.fits')
    ha.convolve(k,f)
    print 'H-alpha convolved'
    
    hb = imagelayer('hbeta.fits')
    hb.convolve(k,f)
    print 'H-beta convolved'
    
    ib = imagelayer('iband.fits')
    ib.convolve(k,f)
    print 'I-band convolved'
    
    oi = imagelayer('oii.fits')
    oi.convolve(k,f)
    print 'OII convolved'
    
    oii = imagelayer('oiii.fits')
    oii.convolve(k,f)
    print 'OIII convolved'
    
    si = imagelayer('sii.fits')
    si.convolve(k,f)
    print 'SII convolved'
    
    ub = imagelayer('uband.fits')
    ub.convolve(k,f)
    print 'U-band convolved'
    
    uv = imagelayer('uvwide.fits')
    uv.convolve(k,f) 
    print 'UV wide convolved'
    
    return 'ALL IMAGES CONVOLVED'