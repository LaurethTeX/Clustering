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
    data = np.genfromtxt(file_name,dtype=[('Object_Name','S20'),('RA_deg','f8'),('DEC_deg','f8'),('Type','S6')],delimiter="|",skip_header=25,missing_values='',filling_values=0.0,usecols={1,2,3,4},invalid_raise=False)
    
    #Create new REGION file
    region_file = open(file_name[0:-4]+'_REGION.reg','w')
    
    #Write default properties
    region_file.write('# Region file format: DS9 version 4.1\nglobal color=cyan dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5\n')
    
    """
    Current list of object types used in NED 30/July/2014 
    *	        Star or Point Source                                            Cross    Green
    **	        Double star                                                     Cross    Red
    *Ass	Stellar association                                             Cross    White
    *Cl	        Star cluster                                                    Circle   Blue
    AbLS	Absorption line system                                        
    Blue*	Blue star                                                       Cross    Blue 
    C*	        Carbon star                                                     Cross    Yellow
    EmLS	Emission line source
    EmObj	Emission object
    exG*	Extragalactic star (not a member of an identified galaxy)       Diamod   Green
    Flare*	Flare star
    G	        Galaxy                                                          Diamond  Magenta
    GammaS	Gamma ray source
    GClstr	Cluster of galaxies                                             Diamond  Red
    GGroup	Group of galaxies                                               Diamond  Blue
    GPair	Galaxy pair                                                     Box      Blue
    GTrpl	Galaxy triple
    G_Lens	Lensed image of a galaxy
    HII	        HII region                                                      Circle    Green
    IrS	        Infrared source                                                 Box       Yellow
    MCld	Molecular cloud                                                 Circle    White
    Neb	        Nebula                                                          Boxcircle Cyan
    Nova	Nova
    Other	Other classification (e.g. comet; plate defect)                 Diamond   Yellow
    PN	        Planetary nebula                                                Circle    Yellow
    PofG	Part of galaxy                                                  X         White
    Psr	        Pulsar
    QGroup	Group of QSOs
    QSO	        Quasi-stellar object
    Q_Lens	Lensed image of a QSO
    RadioS	Radio source                                                    Box        Red
    Red*	Red star                                       
    RfN	        Reflection nebula                                               Circle     Red
    SN	        Supernova                                                       Cirle      Magenta
    SNR	        Supernova remnant                                               Circle     Cyan
    UvES	Ultraviolet excess source                                       X          Magenta
    UvS	        Ultraviolet source                                              Cross      Magenta
    V*	        Variable star                                                   X          Red
    VisS	Visual source                                                   Box        Green
    WD*	        White dwarf                                                     Diamont    White
    WR*	        Wolf-Rayet star
    XrayS	X-ray source                                                    Cross      Cyan
    """
    #Asign simbols to each interstellar object and write in Region file
    for i in range(data.size):
        #Circle
        if data['Type'][i] == 'SNR':   
            region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = cyan\n')

        elif data['Type'][i] == 'HII':
            region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = green\n')
            
        elif data['Type'][i] == '*Cl':
            region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = blue\n')
            
        elif data['Type'][i] == 'PN':
            region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = yellow\n')
            
        elif data['Type'][i] == 'MCld':
            region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = white\n')
            
        elif data['Type'][i] == 'RfN':
            region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = red\n')
            
        elif data['Type'][i] == 'SN':
            region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = magenta\n')
                
        #Diamond 
        elif data['Type'][i] == 'exG*':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=diamond color = green\n')

        elif data['Type'][i] == 'G':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=diamond color = magenta\n')
            
        elif data['Type'][i] == 'GClstr':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=diamond color = red\n')
        
        #Cross point(204.24799,-29.830171) # point=cross
        elif data['Type'][i] == '*':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = green\n')
            
        elif data['Type'][i] == '**':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = red\n')
            
        elif data['Type'][i] == '*Ass':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = white\n')
            
        elif data['Type'][i] == 'XrayS':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = cyan\n')
        
        elif data['Type'][i] == 'Blue*':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = blue\n')
        
        elif data['Type'][i] == 'C*':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = yellow\n')
        
        elif data['Type'][i] == 'UvS':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = magenta\n')
            
        #Box
        elif data['Type'][i] == 'VisS':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = green\n')
        
        elif data['Type'][i] == 'RadioS':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = red\n')
            
        elif data['Type'][i] == 'IrS':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = yellow\n')
        
        elif data['Type'][i] == 'GGroup':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = blue\n')
            
        #X
        elif data['Type'][i] == 'UvES':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=X color = magenta\n')
            
        elif data['Type'][i] == 'V*':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=X color = red\n')
            
        elif data['Type'][i] == 'PofG':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=X color = white\n')
            
        #Boxcirle
        elif data['Type'][i] == 'Neb':
            region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=boxcircle color = cyan\n')
            
        else:
            print data['Type'][i]
        
    region_file.close()		
    return 'Number of objects identified: '+str(data.size-1)