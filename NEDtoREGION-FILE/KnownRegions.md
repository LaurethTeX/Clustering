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
