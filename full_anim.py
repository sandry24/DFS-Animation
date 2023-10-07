import pygame
from graph_data import graph

radius = 30
speed = 1
grey = (100, 100, 100)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (50,50,160)
purple = (112,41,99)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
current_node = -1
edges = {}
visited = []

def run():
    for element in graph:
        element.extend([grey, black])
    build_edges()
    pygame.init()
    draw_graph()
    update()
    dfs(1)

def dfs(x, p=-1):
    global current_node
    visited.append(x)
    graph[x-1][2] = white
    graph[x-1][3] = purple
    current_node = x
    if p != -1:
        edges[(p, x)] = [(p, x), white]
    update()
    for i in graph[x-1][1]:
        if i not in visited:
            dfs(i, x)
    current_node = p
    update()

def build_edges():
    for n1, (_, adjacent, _, _) in enumerate(graph):
        for n2 in adjacent:
            eid = n1+1, n2
            if eid not in edges:
                edges[eid] = [(n1+1, n2), grey]

def draw_graph():
    global current_node
    screen.fill((0, 0, 0))
    for e in edges.values():
        (n1, n2), color = e
        pygame.draw.line(screen, color, graph[n1-1][0], graph[n2-1][0], 2)
    for n, (xy, _, lcolor, fcolor) in enumerate(graph):
        if n == current_node-1:
            fcolor = blue
        pygame.draw.circle(screen, lcolor, xy, radius)
        pygame.draw.circle(screen, fcolor, xy, radius - 2)

def update():
    draw_graph()
    pygame.display.update()
    clock.tick(speed)

if __name__ == "__main__":
    run()