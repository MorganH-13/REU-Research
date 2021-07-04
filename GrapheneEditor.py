import numpy as np
import math

#change options
#scale of supercell
scale = 10
#lattice constant
latt_const = 2.47
#z axis spacing
z_change = 12
#degree of rotation around the z-axis
rot_deg = 0 #in degrees


#constants
#molecule name
molecule = 'Graphene'
#molecule species
a_species = 'C'
a_0 = '1'
#type of cooridnates, can choose either direct or cartesian
coords = 'cartesian'
#number of total atoms
atomNum = 2*scale*scale
#convert rot_deg to radians
rot_rad = (rot_deg * math.pi)/180



#base array, in columns
b_1 = np.array([latt_const*scale,0,0])
b_2 = np.array([latt_const*-.5*scale,latt_const*(math.sqrt(3)/2)*scale,0])
b_3 = np.array([0,0,z_change])

#rotates the vectors
if (rot_rad % 2 * math.pi != 0):
    r_1 = np.array([math.cos(rot_rad), -math.sin(rot_rad), 0])
    r_2 = np.array([math.sin(rot_rad), math.cos(rot_rad), 0])
    r_3 = np.array([0, 0, 1])
    
    b_2 = np.array([b_2[0]*r_1[0]+b_2[1]*r_2[0]+b_2[2]*r_3[0],
            b_2[0]*r_1[1]+b_2[1]*r_2[1]+b_2[2]*r_3[1],
            b_2[0]*r_1[2]+b_2[1]*r_2[2]+b_2[2]*r_3[2]])

    
#Writes the header of the file
f = open('Graphene.txt', 'w')
f.write(molecule + '\n')
f.write('   ' + a_0 + '\n')
for line in b_1:
     f.write(str(line) + '   ')
f.write('\n')
for line in b_2:
    f.write(str(line) + '   ')
f.write('\n')
for line in b_3:
    f.write(str(line) + '   ')
f.write('\n')
f.write('   ' + a_species + '\n')
f.write('    ' + str(atomNum) + '\n')
f.write(coords + '\n')
 
#calculations and matrix formations

for row in range(scale):
    for column in range(scale):
        #Generate coords
        a_1 = np.array([row/scale,column/scale,0])
            
        if coords.lower() == 'cartesian':
            #Change to cartesian
            a_2 = np.array([a_1[0]*b_1[0]+a_1[1]*b_2[0]+a_1[2]*b_3[0],
                            a_1[0]*b_1[1]+a_1[1]*b_2[1]+a_1[2]*b_3[1],
                            a_1[0]*b_1[2]+a_1[1]*b_2[2]+a_1[2]*b_3[2]])

        #Write to file
        if coords.lower() == 'direct':
            for line in a_1:
               f.write(str(line) + '   ')
            f.write('\n')
        elif coords.lower() == 'cartesian':
            for line in a_2:
               f.write(str(line) + '   ')
            f.write('\n')

        #Find pair atom
        a_1 = a_1+np.array([(2/3)/scale,(1/3)/scale,0])
        
        if coords.lower() == 'cartesian':
            #Change to cartesian
            a_2 = np.array([a_1[0]*b_1[0]+a_1[1]*b_2[0]+a_1[2]*b_3[0],
                            a_1[0]*b_1[1]+a_1[1]*b_2[1]+a_1[2]*b_3[1],
                            a_1[0]*b_1[2]+a_1[1]*b_2[2]+a_1[2]*b_3[2]])

        #Write to file
        if coords.lower() == 'direct':
            for line in a_1:
               f.write(str(line) + '   ')
            f.write('\n')
        elif coords.lower() == 'cartesian':
            for line in a_2:
               f.write(str(line) + '   ')
            f.write('\n')
        
        #Reset column
        column = 0

