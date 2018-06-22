# coding: UTF-8


import sys

def load_off(filename):
    # read OFF file
    with open(filename,"r") as handle:
        off = handle.read().rstrip().split("\n")

    #get params and faces
    params = list(map(int, off[1].split(" ")))
    n_vertices = params[0]
    n_faces = params[1]
    print(n_vertices,n_faces)

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


def main():
  vertices, faces = load_off(sys.argv[1])


if __name__ == "__main__":
  main()


def main():
    vertices, faces = load_off("bathtub_0107.off")
