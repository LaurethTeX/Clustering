import numpy as np

def nedtoreg(file_name):

    """
    Input:
        -Format
            Text (ASCII) table - Bar Separated Values of Main Source table
        -Example
            nedtoreg('file.txt')
        -Input file generated from NED webpage
            http://ned.ipac.caltech.edu/forms/nearname.html
    Output:
        -Format
            DS9 Region File
        -File
            file_name + '_REGION'.reg
    Return:
        -Interger
            Number of drawn objects
    
    """
    
    #Extrating data from NED file
    data = np.genfromtxt(file_name,dtype=[('Object_Name','S15'),('RA_deg','f8'),('DEC_deg','f8'),('Type','S5')],delimiter="|",skip_header=24,missing_values='',filling_values=0.0,usecols={1,2,3,4},invalid_raise=False)
    
    #Create new REGION file
    region_file = open(file_name[0:-4]+'_REGION.reg','w')
    
    #Write default properties
    region_file.write('# Region file format: DS9 version 4.1\nglobal color=cyan dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5\n')
    
    """
    Current list of object types used in NED 30/July/2014 
    *	        Star or Point Source                                            Cross    Magenta
    **	        Double star                                                     Cross    Red
    *Ass	Stellar association
    *Cl	        Star cluster                                                    Circle   Blue
    AbLS	Absorption line system
    Blue*	Blue star
    C*	        Carbon star
    EmLS	Emission line source
    EmObj	Emission object
    exG*	Extragalactic star (not a member of an identified galaxy)
    Flare*	Flare star
    G	        Galaxy                        
    GammaS	Gamma ray source
    GClstr	Cluster of galaxies
    GGroup	Group of galaxies
    GPair	Galaxy pair
    GTrpl	Galaxy triple
    G_Lens	Lensed image of a galaxy
    HII	        HII region                                                      Circle Green
    IrS	        Infrared source
    MCld	Molecular cloud                                                 Circle Blue
    Neb	        Nebula
    Nova	Nova
    Other	Other classification (e.g. comet; plate defect)
    PN	        Planetary nebula                                                Circle Yellow
    PofG	Part of galaxy
    Psr	        Pulsar
    QGroup	Group of QSOs
    QSO	        Quasi-stellar object
    Q_Lens	Lensed image of a QSO
    RadioS	Radio source
    Red*	Red star
    RfN	        Reflection nebula                                               Circle White
    SN	        Supernova                                                       Diamond Cyan
    SNR	        Supernova remnant                                               Circle Cyan
    UvES	Ultraviolet excess source                                       Circle Magenta
    UvS	        Ultraviolet source                                              Cross Magenta
    V*	        Variable star
    VisS	Visual source
    WD*	        White dwarf                                                     Diamont White
    WR*	        Wolf-Rayet star
    XrayS	X-ray source                                                    Cross Cyan
    """
    #Asign simbols to each interstellar object and write in Region file
    for i in range(data.size):
        if data['Type'][i] == 'SNR':   
            region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # text={'+str(data['Object_Name'][i])+'} color = green\n')
        #elif data['Type'][i] == 'HII':
        #elif data['Type'][i] == '*Cl':
        #elif data['Type'][i] == 'XrayS':
        #elif data['Type'][i] == 'Radio':
        
        
        
        else:
            print data['Type'][i]
        
    region_file.close()		
    return 