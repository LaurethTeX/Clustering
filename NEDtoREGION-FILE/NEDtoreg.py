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
    #Index for coordinates
    RA_text = 204.23171
    DEC_text = -29.798166
    
    #Index for labels
    label = [0 for i in range(25)]
    
    
    #Extrating data from NED file
    data = np.genfromtxt(file_name,dtype=[('Object_Name','S20'),('RA_deg','f8'),('DEC_deg','f8'),('Type','S6')],delimiter="|",skip_header=25,missing_values='',filling_values=0.0,usecols={1,2,3,4},invalid_raise=False)
    
    #Create new REGION file
    region_file = open(file_name[0:-4]+'_REGION.reg','w')
    
    #Write default properties
    region_file.write('# Region file format: DS9 version 4.1\nglobal color=cyan dashlist=8 3 width=1 font="helvetica 12 bold roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5\n')
    
    #Asign simbols to each interstellar object and write in Region file
    for i in range(data.size):
        #Circle
        if data['Type'][i] == 'SNR':
            if label[0]%10 == 0:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = cyan text = {Supernova remnant}\n')
                label[0]+=1
            else:    
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = cyan\n') 

        elif data['Type'][i] == 'HII':
            if label[1]%10 == 0:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = green text = {HII region}\n')
                label[1]+=1
            else:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = green\n')
            
        elif data['Type'][i] == '*Cl':
            if label[2]%10 == 0:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = blue text = {Star cluster}\n')
                label[2]+=1
            else:   
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = blue\n')
            
        elif data['Type'][i] == 'PN':
            if label[3]%10 == 0:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = yellow text = {Planetary nebula}\n')
                label[3]+=1
            else:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = yellow\n')
            
        elif data['Type'][i] == 'MCld':
            if label[4]%10 == 0:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = white text = {Molecular cloud}\n')
                label[4]+=1
            else:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = white\n')
            
        elif data['Type'][i] == 'RfN':
            if label[5]%10 == 0:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = red text = {Reflection nebula}\n')
                lable[5]+=1
            else:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = red\n')
            
        elif data['Type'][i] == 'SN':
            if label[6]%10 == 0:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = magenta text = {Supernova}\n')
                label[6]+=1
            else:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = magenta\n')
                
        #Diamond 
        elif data['Type'][i] == 'exG*':
            if label[7]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=diamond color = green text = {Extragalactic star}\n')
                label[7]+=1
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=diamond color = green\n')

        elif data['Type'][i] == 'G':
            if label[8]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=diamond color = magenta text = {Galaxy}\n')
                label[8]+=1
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=diamond color = magenta\n')
            
        elif data['Type'][i] == 'GClstr':
            if label[9]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=diamond color = red text = {Cluster of galaxies}\n')
                label[9]+=1
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=diamond color = red\n')
        
        #Cross point(204.24799,-29.830171) # point=cross
        elif data['Type'][i] == '*':
            if label[10]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = green text = {Star}\n')
                label[10]+=1
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = green\n')
            
        elif data['Type'][i] == '**':
            if label[11]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = red text = {Double star}\n')
                label[11]+=1
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = red\n')
            
        elif data['Type'][i] == '*Ass':
            if label[12]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = white text = {Stellar association}\n')
                label[12]+=1
            else:    
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = white\n')
            
        elif data['Type'][i] == 'XrayS':
            if label[13]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = cyan text = {X-ray source}\n')
                label[13]+=1
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = cyan\n')
        
        elif data['Type'][i] == 'Blue*':
            if label[14]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = blue text = {Blue Star}\n')
                label[14]+=1
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = blue\n')
        
        elif data['Type'][i] == 'C*':
            if label[15]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = yellow text = {Carbon star}\n')
                label[15]+=1
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = yellow\n')
        
        elif data['Type'][i] == 'UvS':
            if label[16]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = magenta text = {Ultraviolet source}\n')
                label[16]+=1
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = magenta\n')
            
        #Box
        elif data['Type'][i] == 'VisS':
            if label[17]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = green text = {Visual source}\n')
                label[17]+=1
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = green\n')
        
        elif data['Type'][i] == 'RadioS':
            if label[18]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = red text = {Radio source}\n')
                label[18]+=1
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = red\n')
            
        elif data['Type'][i] == 'IrS':
            if label[19]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = yellow color = {Infrared source}\n')
                label[19]+=1
            else:    
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = yellow\n')
        
        elif data['Type'][i] == 'GGroup':
            if label[20]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = blue text = {Group of galaxies }\n')
                label[20]+=1
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = blue\n')
            
        #X
        elif data['Type'][i] == 'UvES':
            if label[21]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=X color = magenta text = {Ultraviolet excess source}\n')
                label[21]+=1
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=X color = magenta\n')
            
        elif data['Type'][i] == 'V*':
            if label[22]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=X color = red color = {Variable star}\n')
                label[22]+=1
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=X color = red\n')
            
        elif data['Type'][i] == 'PofG':
            if label[23]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=X color = white text = {Part of galaxy}\n')
                label[23]+=1
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=X color = white\n')
            
        #Boxcirle
        elif data['Type'][i] == 'Neb':
            if label[24]%10 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=boxcircle color = cyan text = {Nebula}\n')
                label[24]+=1
            else:    
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=boxcircle color = cyan\n')
            
        else:
            print data['Type'][i]
     
    region_file.write('# text('+str(RA_text)+','+str(DEC_text)+') text={Identified objects in M83} color = black\n')
    region_file.write('# text('+str(RA_text)+','+str(DEC_text-0.008935)+') text={Main Information Table for NED objects within 10.000 arcmin} color = black\n')
         
    region_file.close()		
    return 'Number of objects identified: '+str(data.size-1)