# Known Regions

Before moving forward let's think about the objects in M83 that have been already studied and clasiffied, and for that NED survey will be our identified objects database, with this knowledge it will be more easier to interpret the results of the clustering algorithms.
Now what I did, was an idea a colleague suggested, from the NED survey identify the kind of object and according to their location in space translate this positions to a REGION file compatible with DS9. With this we are able to match our FITS images with the identified objects.

Now in order to do this correctly, first I download the list of objects you are interested in [here](http://ned.ipac.caltech.edu/forms/nearname.html), the selected characteristics for this particular example are:

* Object Name: **M83**
* Search Radius: **10.0 arc min**
* Format tabular data as: **Text (ASCII) table - Bar Separated Values of Main Source table**

Now, get your own list of NED objects, the one used in the example is [here](https://github.com/LaurethTeX/Clustering/blob/master/NEDtoREGION-FILE/M83-nearname-10.rtf), then download [this](https://github.com/LaurethTeX/Clustering/blob/master/NEDtoREGION-FILE/NEDtoreg.py) program adn open your terminal window.

```shell
$ ipython
>>> run NEDtoreg.py
>>> nedtoreg('yourSelectedList.txt')
```
The characteristics of the `nedtoreg()` funtion are listed below:
```
    Input:
        Format
            Text (ASCII) table - Bar Separated Values of Main Source table
        Example
            nedtoreg('file.txt')
        Input file generated from NED webpage
            http://ned.ipac.caltech.edu/forms/nearname.html
    Output:
        Format
            DS9 Region File
        File
            `file_name + '_REGION'.reg`
    Return:
        -Interger
            Number of drawn objects
```
The program can identify up to 25 different objects, and those that are not will be listed in your terminal. Feel free to add some more.

Finally, open your DS9, open your images, load the region file and succesfully we get out matched NED objects with our FITS images as we see in the next image.

![Screen](https://raw.githubusercontent.com/LaurethTeX/Clustering/master/NEDtoREGION-FILE/Screenshot%202014-08-05%2015.12.22.png)

As you can see, this can be very helpul with any application, you get to see what has been done and what can be expected from our cluseting test results. Particularly this RGB image correponds to this following wavelengths,

* RED: I-band
* Green: H-alpha
* Blue: UV wide


The details for every matched object in the region file can be accesed by `help(nedtoreg)`, and it will display the following:
```ipython
Current list of object types used in NED 30/July/2014 
    
    *	        Star or Point Source                                            Cross    Green
    **	        Double star                                                     Cross    Red
    *Ass	    Stellar association                                             Cross    White
    *Cl	        Star cluster                                                    Circle   Blue
    AbLS    	Absorption line system                                        
    Blue*   	Blue star                                                       Cross    Blue 
    C*	        Carbon star                                                     Cross    Yellow
    EmLS    	Emission line source
    EmObj	    Emission object
    exG*	    Extragalactic star (not a member of an identified galaxy)       Diamod   Green
    Flare*	    Flare star
    G	        Galaxy                                                          Diamond  Magenta
    GammaS	    Gamma ray source
    GClstr	    Cluster of galaxies                                             Diamond  Red
    GGroup  	Group of galaxies                                               Diamond  Blue
    GPair	    Galaxy pair                                                     Box      Blue
    GTrpl   	Galaxy triple
    G_Lens  	Lensed image of a galaxy
    HII	        HII region                                                      Circle    Green
    IrS	        Infrared source                                                 Box       Yellow
    MCld    	Molecular cloud                                                 Circle    White
    Neb	        Nebula                                                          Boxcircle Cyan
    Nova    	Nova
    Other   	Other classification (e.g. comet; plate defect)                 Diamond   Yellow
    PN	        Planetary nebula                                                Circle    Yellow
    PofG	    Part of galaxy                                                  X         White
    Psr	        Pulsar
    QGroup  	Group of QSOs
    QSO	        Quasi-stellar object
    Q_Lens  	Lensed image of a QSO
    RadioS	    Radio source                                                    Box        Red
    Red*	    Red star                                       
    RfN	        Reflection nebula                                               Circle     Red
    SN	        Supernova                                                       Cirle      Magenta
    SNR	        Supernova remnant                                               Circle     Cyan
    UvES	    Ultraviolet excess source                                       X          Magenta
    UvS	        Ultraviolet source                                              Cross      Magenta
    V*	        Variable star                                                   X          Red
    VisS    	Visual source                                                   Box        Green
    WD*	        White dwarf                                                     Diamont    White
    WR*	        Wolf-Rayet star
    XrayS   	X-ray source                                                    Cross      Cyan
```
# What can we see
As we look at the image we appreciate 1417 star clusters distributed mostly in the inner part of the galaxy, a huge halo of 286 ultraviolet sources in the outer part, 344 scatered HII regions located in the arms in the inner part, 62 supernova remnants and 195 X-ray sources near the inner center of the galaxy.

To be more precise:
```python
Objects found
SNR:    62
HII:    344
*Cl:    1417
SN:     6
G:      13
XrayS:  195
UvS:    286
VisS:   16
RadioS: 28
IrS:    1
GGroup: 1
UvES:   12
V*:     12
PofG:   3
Neb:    3
```
The total identified objects within a 10 ps radius are 2399.

# What is known about M83

M83 is one of the closest and brigthest barred spiral galaxies, it is visible with binoculars in the consellation of Hydra, due to its spiral arms is called the Southern Pinwheel, several supernova explosions have been recorded, a double circumnuclear ring was discovered at its centre where also newly formed stars and giant lanes of dark dist can be found, redish star forming regions are found near the edges and contains a lot of hot gas created by a sudden burst of massive star formation.

Interesting numbers about M83:
* Is 15 million light years away (~4.59892 M Parsecs)
* About 60 supernova remnants have been identified
* Is about 40,000 ligth years across (~12 263.7938 Parsecs)

Here is a nice picture of M83 where you will be able to appreciate better its beauty and characteristics.
![m83](https://raw.githubusercontent.com/LaurethTeX/Clustering/857a91c4858b558adb32016eeda8600fb1a88489/NEDtoREGION-FILE/m83_hubble_1280.jpg)

