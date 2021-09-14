import numpy as np
import math

#for Mn12-H & perfect graphene
#g = open("Graphene.txt", "r")
#mn = open("Mn12-H.txt", "r")
#comb = open('Comb.txt', 'w')

#for Mn12-CH3
g = open("Graphene.txt", "r")
mn = open("Mn12-CH3.txt", "r")
comb = open('Comb.txt', 'w')



#VARIABLES
rot_deg = -105          #in degrees, negative to the right (rotates graphene)
x = 5.05421                #translate Mn along x axis
y = 12.205135              #translate Mn along y axis
z = 6.45              #translate Mn along z axis
#g_z = 0                #DONT CHANGE translate Graphene along z axis


#convert rot_deg to radians
rot_rad = (rot_deg * math.pi)/180


#reads in atom counts and returns their sum
def add(line):
    i = 0
    x = ''
    sum = 0
    numFound = False
    while i < len(line):
        if line[i] != ' ' and line[i] != '\n':
            x += line[i]
            numFound = True
        elif numFound:
            sum = sum + float(x)
            x = ''
            numFound = False
        i += 1
    if i == len(line) and numFound:
        sum = sum + float(x)
    return(sum)


#reads in atom coordinates
def get_array(line):
    i = 0
    x = ''
    coordinate = np.array([])
    numFound = False
    while i < len(line):
        if line[i] != ' ' and line[i] != '\n':
            x += line[i]
            numFound = True
        elif numFound:
            coordinate = np.append(coordinate, [float(x)])
            x = ''
            numFound = False
        i += 1
    if i == len(line) and numFound:
        coordinate = np.append(coordinate,float(x))
    return(coordinate)


#reads and outputs first 7 lines of text file and outputs to a new file
l=0
G = ''
Mg = ''
while l < 8:
    G = g.readline()
    Mg = mn.readline()
    if l <= 4:
        if l == 0:
            Mg = Mg.rstrip('\n')
            comb.write(Mg + " + " + G)
        elif l == 2:
            length = add(Mg)
            comb.write(G)
        elif l == 4:
            comb.write(G)
        else:
            comb.write(G)
    if l == 5:
        comb.write(Mg)
    elif l == 6:
        #to get total amount of atoms in each molecule/structure
        GAtomNum = add(G)
        MgAtomNum = add(Mg)
        totalAtomNum = GAtomNum+MgAtomNum
        #to get individual atoms numbers
        Gcount = get_array(G)
        Mgcount = get_array(Mg)
        Mgcount[3] = Mgcount[3]+Gcount[0]
        
        comb.write(str(int(Mgcount[0]))+ '   ')
        comb.write(str(int(Mgcount[1]))+ '   ')
        comb.write(str(int(Mgcount[2]))+ '   ')
        comb.write(str(int(Mgcount[3]))+ '   ' + '\n')
    elif l == 7:
        comb.write(Mg)
    l += 1
    

    
#radius of Mn
r = length/2


#Prints Mn and Graphene together while rotating and translating
k = 0
while k < totalAtomNum:
    if k < MgAtomNum:
        Mg = mn.readline()
        coord_array = get_array(Mg)
        #subtract radius r from x and y component
        new_x = coord_array[0]-r
        new_y = coord_array[1]-r
        #if z == 0:
        #    new_z = coord_array[2]
        #else:
        #    new_z = z
        new_z = coord_array[2]-r
        #makes an array of the new coordinates
        coord_array = np.array([new_x,new_y,new_z])
        #rotation arrays around the z axis centered at x=0 and y=0
        rotate_x = np.array([math.cos(rot_rad),-math.sin(rot_rad),0])
        rotate_y = np.array([math.sin(rot_rad), math.cos(rot_rad), 0])
        rotate_z = np.array([0,0,1])
        #combines the rotation arrays and the atom array of coordinates to rotate the atom 
        #about the z axis at a given dergee of rotation
        coord_array = np.array([coord_array[0]*rotate_x[0]+coord_array[1]*rotate_x[1]+coord_array[2]*rotate_x[2],
                            coord_array[0]*rotate_y[0]+coord_array[1]*rotate_y[1]+coord_array[2]*rotate_y[2],
                            coord_array[0]*rotate_z[0]+coord_array[1]*rotate_z[1]+coord_array[2]*rotate_z[2]])
        #makes final rotated array of coordinates, centered back at original r
        coord_array = np.array([coord_array[0]+x,coord_array[1]+y,new_z+z])
        comb.write(str(coord_array[0])+'     '+str(coord_array[1])+'     '+str(coord_array[2]))
        comb.write('\n')
    else:
        G = g.readline()
        gArray = get_array(G)
        #gArray[2] += g_z
        for line in gArray:
            comb.write(str(line) + "    ")
        comb.write('\n')
    k+=1