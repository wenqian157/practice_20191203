from compas.geometry import convex_hull

from compas.utilities import flatten
from compas.datastructures import Mesh
from compas.datastructures import Network
from compas.datastructures import mesh_smooth_centroid
from compas.topology import unify_cycles
import compas_rhino
from compas_rhino.artists import MeshArtist
from compas.geometry import Vector
from compas.geometry import add_vectors
from compas.geometry import Plane
from compas.geometry import project_point_plane
from compas.geometry import angle_vectors
from compas.utilities import pairwise
from compas.geometry._transformations.transformations import mirror_point_plane

import rhinoscriptsyntax as rs
import copy
import math


def get_convex_hull_mesh(points):
    faces = convex_hull(points)
    vertices = list(set(flatten(faces)))

    i_index = {i: index for index, i in enumerate(vertices)}
    vertices = [points[index] for index in vertices]
    faces = [[i_index[i] for i in face] for face in faces]
    faces = unify_cycles(vertices, faces)

    mesh = Mesh.from_vertices_and_faces(vertices, faces)

    return mesh


guids = compas_rhino.select_lines()
lines = compas_rhino.get_line_coordinates(guids)

network = Network.from_lines(lines)
leafs = []
joints = []
for key in network.node:
    if network.is_leaf(key):
        leafs.append(key)
    else:
        joints.append(key)

pt_center = network.node_coordinates(joints[0])
pts = [network.node_coordinates(key) for key in leafs]

joint_width = 15
leaf_width = 7

convex_hull_mesh = get_convex_hull_mesh(pts)

mesh = Mesh()
for key in convex_hull_mesh.vertices():
    mesh.add_vertex(key)
    mesh.vertex[key].update(convex_hull_mesh.vertex[key])

descdent_tree = copy.deepcopy(convex_hull_mesh.halfedge)

for u, v in convex_hull_mesh.edges():
    descdent_tree[u][v] = {'jp': None, 'lp': None}
    descdent_tree[v][u] = {'jp': None, 'lp': None}

current_key = convex_hull_mesh.number_of_vertices()

for fkey in convex_hull_mesh.faces():
    f_centroid = convex_hull_mesh.face_centroid(fkey)
    vec = Vector.from_start_end(pt_center, f_centroid)

    # if the branches has a 'convex' corner,
    # flip the vec to the corresponding face.
    f_normal = convex_hull_mesh.face_normal(fkey)
    angle = angle_vectors(f_normal, vec, False)
    if angle > math.pi * 0.5:
        # vec.scale(-1)
        pln = Plane(pt_center, f_normal)
        pt_mirror = mirror_point_plane(f_centroid, pln)
        vec = Vector.from_start_end(pt_center, pt_mirror)

        # angle = math.pi - angle

    vec.unitize()
    # dist = joint_width / math.cos(angle)
    # vec.scale(dist)
    vec.scale(joint_width)

    pt = add_vectors(pt_center, vec)

    face = convex_hull_mesh.face[fkey]
    v_keys = face + [face[0]]
    for u, v in pairwise(v_keys):
        descdent_tree[u][v].update({'jp': current_key})

    mesh.add_vertex(current_key)
    mesh.vertex[current_key].update({'x': pt[0], 'y': pt[1], 'z': pt[2]})

    current_key += 1

for key in convex_hull_mesh.vertices():
    nbrs = convex_hull_mesh.vertex_neighbors(key)
    for nbr in nbrs:
        halfedge = (key, nbr)
        pt_joint_descendent = mesh.vertex_coordinates(descdent_tree[key][nbr]['jp'])

        vec_edge = Vector.from_start_end(pt_center, mesh.vertex_coordinates(key))
        pln_end = Plane(mesh.vertex_coordinates(key), vec_edge)
        pt = project_point_plane(pt_joint_descendent, pln_end)
        vec_leaf = Vector.from_start_end(mesh.vertex_coordinates(key), pt)
        vec_leaf.unitize()
        vec_leaf.scale(leaf_width)
        pt = add_vectors(mesh.vertex_coordinates(key), vec_leaf)

        descdent_tree[key][nbr].update({'lp': current_key})

        mesh.add_vertex(current_key)
        mesh.vertex[current_key].update({'x': pt[0], 'y': pt[1], 'z': pt[2]})
        current_key += 1

for key in convex_hull_mesh.vertices():
    nbrs = convex_hull_mesh.vertex_neighbors(key, ordered=True)
    v_keys = nbrs + [nbrs[0]]
    for a, b in pairwise(v_keys):
        face = [
            descdent_tree[key][a]['lp'],
            descdent_tree[key][a]['jp'],
            descdent_tree[key][b]['jp'],
            descdent_tree[key][b]['lp']
        ]
        mesh.add_face(face)

# mesh.to_json('mesh1.json', pretty=True)

artist = MeshArtist(mesh)
artist.draw_vertices()
artist.draw_faces()

# artist = MeshArtist(convex_hull_mesh)
# artist.draw_faces(color=(255, 0, 0))
# artist.draw_edges(color=(255, 0, 0))
