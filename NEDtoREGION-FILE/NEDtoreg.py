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
    class Label(object):
        def __init__(self,index):
            self.label = [0 for i in range(index)]
            self.nameType = ['NaN' for i in range(index)]
        def getname(self,name,index):
            self.nameType[index] = name
            
    lbl = Label(25)
    
    #Extrating data from NED file
    data = np.genfromtxt(file_name,dtype=[('Object_Name','S20'),('RA_deg','f8'),('DEC_deg','f8'),('Type','S6')],delimiter="|",skip_header=25,missing_values='',filling_values=0.0,usecols={1,2,3,4},invalid_raise=False)
    
    #Create new REGION file
    region_file = open(file_name[0:-4]+'_REGION.reg','w')
    
    #Write default properties
    region_file.write('# Region file format: DS9 version 4.1\nglobal color=cyan dashlist=8 3 width=1 font="helvetica 10 bold roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5\n')
    
    #Asign simbols to each interstellar object and write in Region file
    for i in range(data.size):
        #Circle
        if data['Type'][i] == 'SNR':
            if lbl.label[0]%5 == 0:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = cyan text = {Supernova remnant}\n')
                lbl.getname(data['Type'][i],0)
            else:    
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = cyan\n') 
            lbl.label[0]+=1

        elif data['Type'][i] == 'HII':
            if lbl.label[1]%5 == 0:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = green text = {HII region}\n')           
                lbl.getname(data['Type'][i],1)
            else:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = green\n')
            lbl.label[1]+=1
            
        elif data['Type'][i] == '*Cl':
            if lbl.label[2]%5 == 0:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = blue text = {Star cluster}\n')
                lbl.getname(data['Type'][i],2)
            else:   
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = blue\n')
            lbl.label[2]+=1
            
        elif data['Type'][i] == 'PN':
            if lbl.label[3]%5 == 0:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = yellow text = {Planetary nebula}\n')
                lbl.getname(data['Type'][i],3)
            else:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = yellow\n')
            lbl.label[3]+=1
            
        elif data['Type'][i] == 'MCld':
            if lbl.label[4]%5 == 0:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = white text = {Molecular cloud}\n')
                lbl.getname(data['Type'][i],4)
            else:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = white\n')
            lbl.label[4]+=1
            
        elif data['Type'][i] == 'RfN':
            if lbl.label[5]%5 == 0:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = red text = {Reflection nebula}\n')
                lbl.getname(data['Type'][i],5)
            else:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = red\n')
            lbl.label[5]+=1
            
        elif data['Type'][i] == 'SN':
            if lbl.label[6]%5 == 0:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = magenta text = {Supernova}\n')
                lbl.getname(data['Type'][i],6)
            else:
                region_file.write('circle('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+',1") # color = magenta\n')
            lbl.label[6]+=1
                
        #Diamond 
        elif data['Type'][i] == 'exG*':
            if lbl.label[7]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=diamond color = green text = {Extragalactic star}\n')
                lbl.getname(data['Type'][i],7)
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=diamond color = green\n')
            lbl.label[7]+=1

        elif data['Type'][i] == 'G':
            if lbl.label[8]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=diamond color = magenta text = {Galaxy}\n')
                lbl.getname(data['Type'][i],8)
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=diamond color = magenta\n')
            lbl.label[8]+=1
            
        elif data['Type'][i] == 'GClstr':
            if lbl.label[9]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=diamond color = red text = {Cluster of galaxies}\n')
                lbl.getname(data['Type'][i],9)
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=diamond color = red\n')
            lbl.label[9]+=1
        
        #Cross point(204.24799,-29.830171) # point=cross
        elif data['Type'][i] == '*':
            if lbl.label[10]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = green text = {Star}\n')
                lbl.getname(data['Type'][i],10)
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = green\n')
            lbl.label[10]+=1
            
        elif data['Type'][i] == '**':
            if lbl.label[11]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = red text = {Double star}\n')
                lbl.getname(data['Type'][i],11)
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = red\n')
            lbl.label[11]+=1
            
        elif data['Type'][i] == '*Ass':
            if lbl.label[12]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = white text = {Stellar association}\n')
                lbl.getname(data['Type'][i],12)
            else:    
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = white\n')
            lbl.label[12]+=1
            
        elif data['Type'][i] == 'XrayS':
            if lbl.label[13]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = cyan text = {X-ray source}\n')
                lbl.getname(data['Type'][i],13)
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = cyan\n')
            lbl.label[13]+=1
        
        elif data['Type'][i] == 'Blue*':
            if lbl.label[14]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = blue text = {Blue Star}\n')
                lbl.getname(data['Type'][i],14)
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = blue\n')
            lbl.label[14]+=1
        
        elif data['Type'][i] == 'C*':
            if lbl.label[15]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = yellow text = {Carbon star}\n')
                lbl.getname(data['Type'][i],15)
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = yellow\n')
            lbl.label[15]+=1
        
        elif data['Type'][i] == 'UvS':
            if lbl.label[16]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = magenta text = {Ultraviolet source}\n')
                lbl.getname(data['Type'][i],16)
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=cross color = magenta\n')
            lbl.label[16]+=1
            
        #Box
        elif data['Type'][i] == 'VisS':
            if lbl.label[17]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = green text = {Visual source}\n')
                lbl.getname(data['Type'][i],17)
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = green\n')
            lbl.label[17]+=1
        
        elif data['Type'][i] == 'RadioS':
            if lbl.label[18]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = red text = {Radio source}\n')
                lbl.getname(data['Type'][i],18)
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = red\n')
            lbl.label[18]+=1
            
        elif data['Type'][i] == 'IrS':
            if lbl.label[19]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = yellow color = {Infrared source}\n')
                lbl.getname(data['Type'][i],19)
            else:    
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = yellow\n')
            lbl.label[19]+=1
        
        elif data['Type'][i] == 'GGroup':
            if lbl.label[20]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = blue text = {Group of galaxies }\n')
                lbl.getname(data['Type'][i],20)
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=box color = blue\n')
            lbl.label[20]+=1
            
        #X
        elif data['Type'][i] == 'UvES':
            if lbl.label[21]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=X color = magenta text = {Ultraviolet excess source}\n')
                lbl.getname(data['Type'][i],21)
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=X color = magenta\n')
            lbl.label[21]+=1
            
        elif data['Type'][i] == 'V*':
            if lbl.label[22]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=X color = red color = {Variable star}\n')
                lbl.getname(data['Type'][i],22)
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=X color = red\n')
            lbl.label[22]+=1
            
        elif data['Type'][i] == 'PofG':
            if lbl.label[23]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=X color = white text = {Part of galaxy}\n')
                lbl.getname(data['Type'][i],23)
            else:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=X color = white\n')
            lbl.label[23]+=1
            
        #Boxcirle
        elif data['Type'][i] == 'Neb':
            if lbl.label[24]%5 == 0:
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=boxcircle color = cyan text = {Nebula}\n')
                lbl.getname(data['Type'][i],24)
            else:    
                region_file.write('point('+str(data['RA_deg'][i])+','+str(data['DEC_deg'][i])+') # point=boxcircle color = cyan\n')
            lbl.label[24]+=1
            
        else:
            print 'Object not considered  ',data['Type'][i]
     
    region_file.write('# text('+str(RA_text)+','+str(DEC_text)+') text={Identified objects in M83} color = black\n')
    region_file.write('# text('+str(RA_text)+','+str(DEC_text-0.008935)+') text={Main Information Table for NED objects within 10.000 arcmin} color = black\n')
         
    region_file.close()
    
    print 'Objects found'
    for i in range(25):
        print str(lbl.nameType[i])+":    "+str(lbl.label[i])
        
    return 'Number of objects identified: '+str(data.size-1)