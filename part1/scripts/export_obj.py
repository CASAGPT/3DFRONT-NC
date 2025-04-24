import numpy as np
import json

def cuboids_to_obj(cuboid_array, filename="cuboids.obj"):
    """
    Generate an OBJ file from an array of cuboids.

    Args:
        cuboid_array: numpy array of shape (n, 8, 3) representing n cuboids, 8 vertices per cuboid and 3D coordinates for each vertex
        filename: output OBJ filename
    """
    vertices = []
    faces = []
    vertex_count = 0

    for cuboid_count in range(cuboid_array.shape[0]):
        v = cuboid_array[cuboid_count]
        # Add vertices to the list
        vertices.extend(v.tolist())
        # Define the 6 faces of the cuboid (1-based for OBJ format)
        cuboid_faces = [
            [vertex_count + 1, vertex_count + 2, vertex_count + 3, vertex_count + 4],  # bottom
            [vertex_count + 5, vertex_count + 6, vertex_count + 7, vertex_count + 8],  # top
            [vertex_count + 1, vertex_count + 2, vertex_count + 6, vertex_count + 5],  # front
            [vertex_count + 3, vertex_count + 4, vertex_count + 8, vertex_count + 7],  # back
            [vertex_count + 1, vertex_count + 4, vertex_count + 8, vertex_count + 5],  # left
            [vertex_count + 2, vertex_count + 3, vertex_count + 7, vertex_count + 6]   # right
        ]
        faces.extend(cuboid_faces)

        # Update the vertex count for the next cuboid
        vertex_count += 8

    # Write vertices and faces to an OBJ file
    with open(filename, 'w') as f:
        # Write vertices
        for vertex in vertices:
            f.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
        # Write faces
        for face in faces:
            f.write(f"f {face[0]} {face[1]} {face[2]} {face[3]}\n")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--sample_id", type=str, default='1c648cfd-6eca-4a84-af58-b62a3a4d173a')
    args = parser.parse_args()

    # Load cuboids data
    with open('./data/cuboids_dict.json', 'r') as f:
        cuboids_dict = json.load(f)
    print(f"Total number of samples: {len(cuboids_dict.keys())}")

    # Export to OBJ
    cuboids_to_obj(np.array(cuboids_dict[args.sample_id]), f"output_{args.sample_id}.obj")
