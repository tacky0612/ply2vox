
# coding: utf-8

# In[20]:


get_ipython().run_line_magic('matplotlib', 'inline')
from load_ply import load_ply
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[21]:


def plot3D(np_pc):
    #3D表示
    fig = plt.figure(1,figsize=(10, 10))
    ax = fig.add_subplot(1,1,1, projection='3d')
    ax.scatter(np_pc[:,0], np_pc[:,1], np_pc[:,2])
    ax.axis("equal")
    plt.show()


# In[22]:


def plot_trihedral_figure_vox(np_pc):
    #Voxel版三面図
    a = 1
    for i in range(3):
        if i == 2:
            a = -2
        plt.scatter(np_pc[:,i],np_pc[:,i+a],s=10)
        plt.xlim([-2,32]) 
        plt.ylim([-2,32]) 
        plt.gca().set_aspect('equal')
        plt.show()


# In[19]:


def plot_trihedral_figure(np_pc):
    #三面図
    a = 1
    for i in range(3):
        if i == 2:
            a = -2
        plt.scatter(np_pc[:,i],np_pc[:,i+a],s=2)
        plt.axis('equal')
        plt.show()

