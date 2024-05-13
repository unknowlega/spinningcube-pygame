'''
import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)

def rotate_point(point, angle):
    x, y = point
    x_new = x * math.cos(angle) - y * math.sin(angle)
    y_new = x * math.sin(angle) + y * math.cos(angle)
    return x_new, y_new

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_cube_vertices(size):
    vertices = [
        (-size, -size, -size),
        (-size, size, -size),
        (size, size, -size),
        (size, -size, -size),
        (-size, -size, size),
        (-size, size, size),
        (size, size, size),
        (size, -size, size)
    ]
    return vertices

def project(point, angle_x, angle_y):
    x, y, z = point
    x, z = rotate_point((x, z), angle_x)
    y, z = rotate_point((y, z), angle_y)
    scale = 200 / (200 + z)
    x = x * scale + WIDTH / 2
    y = y * scale + HEIGHT / 2
    return x, y

def draw_cube(surface, vertices, angle_x, angle_y, colors):
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    for edge in edges:
        start = project(vertices[edge[0]], angle_x, angle_y)
        end = project(vertices[edge[1]], angle_x, angle_y)
        pygame.draw.line(surface, colors[edge[0] // 2], start, end, 2)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Spinning 3D Cube")

    clock = pygame.time.Clock()

    cube_size = 100
    vertices = generate_cube_vertices(cube_size)
    colors = [random_color() for _ in range(6)]

    angle_x = random.uniform(0, 2 * math.pi)
    angle_y = random.uniform(0, 2 * math.pi)

    mouse_down = False
    last_mouse_pos = (0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_down = True
                    last_mouse_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_down = False

        screen.fill(BLACK)

        draw_cube(screen, vertices, angle_x, angle_y, colors)

        if mouse_down:
            mouse_pos = pygame.mouse.get_pos()
            dx, dy = (mouse_pos[i] - last_mouse_pos[i] for i in range(2))
            angle_x -= dx * 0.01
            angle_y -= dy * 0.01
            last_mouse_pos = mouse_pos
        else:
            angle_x += 0.01
            angle_y += 0.01

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
'''
# above is it with the mouse movement

import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)

def rotate_point(point, angle):
    x, y = point
    x_new = x * math.cos(angle) - y * math.sin(angle)
    y_new = x * math.sin(angle) + y * math.cos(angle)
    return x_new, y_new

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_cube_vertices(size):
    vertices = [
        (-size, -size, -size),
        (-size, size, -size),
        (size, size, -size),
        (size, -size, -size),
        (-size, -size, size),
        (-size, size, size),
        (size, size, size),
        (size, -size, size)
    ]
    return vertices

def project(point, angle_x, angle_y):
    x, y, z = point
    x, z = rotate_point((x, z), angle_x)
    y, z = rotate_point((y, z), angle_y)
    scale = 200 / (200 + z)
    x = x * scale + WIDTH / 2
    y = y * scale + HEIGHT / 2
    return x, y

def draw_cube(surface, vertices, angle_x, angle_y, colors):
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    for edge in edges:
        start = project(vertices[edge[0]], angle_x, angle_y)
        end = project(vertices[edge[1]], angle_x, angle_y)
        pygame.draw.line(surface, colors[edge[0] // 2], start, end, 2)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Spinning 3D Cube")

    clock = pygame.time.Clock()

    cube_size = 100
    vertices = generate_cube_vertices(cube_size)
    colors = [random_color() for _ in range(6)]

    angle_x = random.uniform(0, 2 * math.pi)
    angle_y = random.uniform(0, 2 * math.pi)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        draw_cube(screen, vertices, angle_x, angle_y, colors)

        angle_x += 0.01
        angle_y += 0.01

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
