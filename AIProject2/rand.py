import networkx as nx
import matplotlib.pyplot as plt
import random


def create_lattice_graph(rows, columns):
    G = nx.grid_2d_graph(rows, columns)
    return G


def draw_colored_graph(graph, color):
    pos = {(i, j): (j, -i) for i, j in graph.nodes()}
    node_colors = [color[node] for node in graph.nodes()]
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color=node_colors, font_color='black',
            font_size=8)
    plt.show()


def random_coloring(graph, num_colors):
    color = {node: random.randint(1, num_colors) for node in graph.nodes()}
    return color


conflicts = 0
total_conflicts = []


def is_valid_coloring(graph, color):
    global conflicts
    total_conflicts.append(conflicts)
    conflicts = 0
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


rows = 5
columns = 5
num_colors = 3

lattice_graph = create_lattice_graph(rows, columns)
color_assignment = random_coloring(lattice_graph, num_colors)

print("Randomly Assigned Colors:")
print(color_assignment)
draw_colored_graph(lattice_graph, color_assignment)

check_correct_colouring(lattice_graph, color_assignment)

while not is_valid_coloring(lattice_graph, color_assignment):
    check_correct_colouring(lattice_graph, color_assignment)
draw_colored_graph(lattice_graph, color_assignment)

print(total_conflicts)

plt.plot(range(len(total_conflicts)), total_conflicts, marker='o')
plt.xlabel('Folds')
plt.ylabel('Conflicts')
plt.title('Total Conflicts Over Folds for 5x5 2d Lattices Graph')
plt.show()