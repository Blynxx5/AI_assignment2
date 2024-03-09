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

def is_valid_coloring(graph, color):
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

def run_experiment():
    global conflicts

    conflicts = 0


    rows = 5
    columns = 5
    num_colours = 3
    lattice_graph = create_lattice_graph(rows, columns)
    color_assignment = random_coloring(lattice_graph, num_colours)
    while not is_valid_coloring(lattice_graph, color_assignment):
        check_correct_colouring(lattice_graph, color_assignment)
    return conflicts

#running the experiment 20 times and printing the results
num_experiments = 20
conflicts_list = []

for i in range(1, num_experiments + 1):
    conflicts = run_experiment()
    conflicts_list.append(conflicts)
    print(f"Pass {i}: Conflicts - {conflicts}")

plt.figure(figsize=(10, 6))
plt.plot(range(1, num_experiments + 1), conflicts_list, marker='o', linestyle='-', color='b')
plt.title('Conflicts over 20 Passes with initial Random Colouring')
plt.xlabel('Pass')
plt.ylabel('Number of Conflicts')
plt.grid(True)
plt.show()


min_conflicts = min(conflicts_list)
max_conflicts = max(conflicts_list)
sum_conflicts = sum(conflicts_list)
len_conflicts = len(conflicts_list)
mean = sum_conflicts / len_conflicts

print(f"Range of Conflicts: {min_conflicts} to {max_conflicts}, and with a mean of {mean}")