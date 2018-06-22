
# coding: utf-8

# In[1]:


# coding: UTF-8


# In[2]:


import sys
import math
import random
# from sympy import *


# In[3]:


def load_off(filename):
    # read OFF file
    with open(filename,"r") as handle:
        off = handle.read().rstrip().split("\n")

    #get params and faces
    params = list(map(int, off[1].split(" ")))
    n_vertices = params[0]
    n_faces = params[1]

    # read  Vertex coordinates
    vertices = []
    for n in range(n_vertices):
        coords = list(map(float, off[2+n].split()))
        vertices.append(coords)

    # read information of faces
    faces = []
    for n in range(n_faces):
        connects = list(map(int, off[2 + n_vertices + n].split(" ")))[1:]
        faces.append(connects)

    return vertices, faces


# $$
# S = \frac{1}{2} |(c-a)\times(b-a) |
# $$
# 

# In[4]:


def calc_vector_norm(a):
    norm = 0.0
    for el in a:
        norm += el *el
    return math.sqrt(norm)


# In[5]:


def calc_cross_product_3d(a,b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]


# In[6]:


def calc_triangle_area(a, b, c):
    ca = [c[0]-a[0], c[1]-a[1], c[2]-a[2]]
    ba = [b[0]-a[0], b[1]-a[1], b[2]-a[2]]
    cross = calc_cross_product_3d(ca, ba)
    return 0.5 * calc_vector_norm(cross)


# In[7]:


def calc_cumulative_areas(vertices, faces):
    cuma = 0.0
    cum_areas = []
    for fc in faces:
        cuma += calc_triangle_area(
            vertices[fc[0]], vertices[fc[1]], vertices[fc[2]])
        cum_areas.append(cuma)
    return cum_areas


# In[8]:


def random_select_face_id(cum_areas):
    rand_area = cum_areas[-1] * random.random()
    select_id = 0
    for n in range(len(cum_areas)):
        if rand_area <= cum_areas[n]:
            select_id = n
            break
    return select_id


# In[9]:


def gen_random_points(vertices, faces, n_points):
    cum_areas = calc_cumulative_areas(vertices, faces)
    points = []
    for n in range(n_points):
        fid = random_select_face_id(cum_areas)
        r1 = math.sqrt(random.random())
        r2 = random.random()
        a = vertices[faces[fid][0]]
        b = vertices[faces[fid][1]]
        c = vertices[faces[fid][2]]
        xp = (1 - r1) * a[0] + r1 * (1 - r2) * b[0] + r1 * r2 * c[0]
        yp = (1 - r1) * a[1] + r1 * (1 - r2) * b[1] + r1 * r2 * c[1]
        zp = (1 - r1) * a[2] + r1 * (1 - r2) * b[2] + r1 * r2 * c[2]
        points.append([xp, yp, zp])
    return points


# In[21]:


def print_pointcloud_ply(points):
    print("ply")
    print("format ascii 1.0")
    print("element vertex %d" % len(points))
    print("property float x")
    print("property float y")
    print("property float z")
    print("end_header")
    for pt in points:
        print("%f %f %f" % (pt[0], pt[1], pt[2]))


# In[40]:


def write_pointcloud_ply(filename,points):
    f = open(filename, 'w') 
    f.write("ply\n")
    f.write("format ascii 1.0\n")
    f.write("element vertex %d\n" % len(points))
    f.write("property float x\n")
    f.write("property float y\n")
    f.write("property float z\n")
    f.write("end_header\n")
    for pt in points:
        f.write("%f %f %f \n" % (pt[0], pt[1], pt[2]))
    f.close


# In[41]:


#filename = input()
#vertices, faces = load_off(filename)
#n_points = 1024
#points = gen_random_points(vertices, faces, n_points)
#print_pointcloud_ply(points)


# In[6]:


def main():
    vertices, faces = load_off(sys.argv[1])
    n_points = 1024
    points = gen_random_points(vertices, faces, n_points)
    print_pointcloud_ply(points)


# In[7]:


if __name__ == "__main__":
    main()

