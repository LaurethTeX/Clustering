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

As you can see, this can be very helpul with any application, you get to see what has been done and what can be expect from our results.

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
