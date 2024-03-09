import networkx as nx
import matplotlib.pyplot as plt
import random
def create_lattice_graph(rows, columns):
    G = nx.grid_2d_graph(rows, columns)
    return G

def draw_colored_graph(graph, color):
    pos = {(i, j): (j, -i) for i, j in graph.nodes()}
    node_colors = [color[node] for node in graph.nodes()]
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color=node_colors, font_color='black', font_size=8)
    plt.show()

def degree_based_coloring(graph):
    degree_dict = dict(graph.degree())
    color = {node: degree_dict[node] for node in graph.nodes()}
    return color

conflicts = 0
full_graph_completes = 0

def is_valid_coloring(graph, color):
    global full_graph_completes
    full_graph_completes = full_graph_completes + 1
    for node in graph.nodes():
        for neighbor in graph.neighbors(node):
            if color[node] == color[neighbor]:
                return False
    return True

def check_correct_colouring(graph, colour):
    global conflicts
    for node in graph.nodes():
        for neighbour in graph.neighbors(node):
            if colour[node] == colour[neighbour]:
                conflicts = conflicts + 1
                while colour[node] == colour[neighbour]:
                    colour[node] = random.randint(1, len(set(colour.values())))

rows = 6
columns = 6

lattice_graph = create_lattice_graph(rows, columns)
color_assignment = degree_based_coloring(lattice_graph)

print("Degree-Based Colors:")
print(color_assignment)
draw_colored_graph(lattice_graph, color_assignment)

while not is_valid_coloring(lattice_graph, color_assignment):
    check_correct_colouring(lattice_graph, color_assignment)
draw_colored_graph(lattice_graph, color_assignment)
print(conflicts)
print(full_graph_completes)