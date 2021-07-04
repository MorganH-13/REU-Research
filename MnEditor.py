import numpy as np
import math

#read in
mn = open("Mn12-H-cartesian.txt", "r")
#write to
f = open('Mg-POSCAR.vasp', 'w')

#change, rotate the molecule
rot_deg = -45 #in degrees, negative to the right


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
    numFound = False
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
j=0
content = ''
while j < 8:
    content = mn.readline()
    f.write(content)
    #finds the middle point of the molecule and divides in half to find radius, only with one vector 
    #because this is a cube
    if j == 2:
        r = add(content)/2
    #reads in the number of atoms and adds them together using the add function
    if j == 6:
        atomNum = add(content)
    j += 1
k = 0


#reads in the coordinates for each atom one at a time
while k < atomNum:
    content = mn.readline()
    coord_array = get_array(content)
    #subtract radius r from x and y component
    new_x = coord_array[0]-r
    new_y = coord_array[1]-r
    z = coord_array[2]
    #makes an array of the new coordinates
    coord_array = np.array([new_x,new_y,z])
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
    coord_array = np.array([coord_array[0]+r,coord_array[1]+r,z])
    
    #writes out array to new txt or vasp file
    f.write(str(coord_array[0])+'     '+str(coord_array[1])+'     '+str(coord_array[2]))
    f.write('\n')
    k+=1