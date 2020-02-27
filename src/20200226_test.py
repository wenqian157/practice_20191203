from compas.datastructures import Network
from compas.datastructures import Mesh
import compas_rhino
from compas.datastructures import network_find_cycles
from compas_rhino.artists import MeshArtist
from compas.datastructures import mesh_smooth_centroid

# guids = compas_rhino.select_lines()
# lines = compas_rhino.get_line_coordinates(guids)
# network = Network.from_lines(lines)

# cycles = network_find_cycles(network, network.leaves())
# vertices = [network.node_coordinates(vkey) for vkey in network.nodes()]

# faces = cycles[1:]
# mesh = Mesh.from_vertices_and_faces(vertices, faces)
mesh = Mesh.from_obj('test6.obj')
fixed = list(mesh.vertices_where({'vertex_degree': 3}))
mesh_smooth_centroid(mesh, fixed=fixed)


artist = MeshArtist(mesh)
artist.draw_mesh()

