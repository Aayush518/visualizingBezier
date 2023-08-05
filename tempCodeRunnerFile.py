import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_COLOR = (255, 255, 255)

# Control point colors
CONTROL_POINT_COLOR = (255, 0, 0)
CONTROL_POINT_RADIUS = 5

# Bezier curve color and thickness
BEZIER_COLOR = (0, 0, 255)
BEZIER_THICKNESS = 2

# Control points (initial positions)
control_points = []

# Bezier curve points
bezier_points = []

# Shift the origin to the center of the window
ORIGIN_X, ORIGIN_Y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

# Scale factor for the coordinate system
SCALE_FACTOR = 20

# Pygame window setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bezier Curve Visualization")

# Font setup
font = pygame.font.Font(None, 36)

def draw_control_points():
    for point in control_points:
        pygame.draw.circle(screen, CONTROL_POINT_COLOR, (ORIGIN_X + point[0] * SCALE_FACTOR, ORIGIN_Y - point[1] * SCALE_FACTOR), CONTROL_POINT_RADIUS)

def draw_bezier_curve():
    for i in range(len(bezier_points) - 1):
        pygame.draw.line(screen, BEZIER_COLOR, (ORIGIN_X + bezier_points[i][0] * SCALE_FACTOR, ORIGIN_Y - bezier_points[i][1] * SCALE_FACTOR),
                         (ORIGIN_X + bezier_points[i + 1][0] * SCALE_FACTOR, ORIGIN_Y - bezier_points[i + 1][1] * SCALE_FACTOR), BEZIER_THICKNESS)

def draw_control_polygon():
    for i in range(len(control_points) - 1):
        pygame.draw.line(screen, (0, 0, 0), (ORIGIN_X + control_points[i][0] * SCALE_FACTOR, ORIGIN_Y - control_points[i][1] * SCALE_FACTOR),
                         (ORIGIN_X + control_points[i + 1][0] * SCALE_FACTOR, ORIGIN_Y - control_points[i + 1][1] * SCALE_FACTOR), 1)

def calculate_bezier_points():
    bezier_points.clear()
    for t in range(0, 101):
        x = (1 - t / 100) ** 2 * control_points[0][0] + 2 * (1 - t / 100) * (t / 100) * control_points[1][0] + (t / 100) ** 2 * control_points[2][0]
        y = (1 - t / 100) ** 2 * control_points[0][1] + 2 * (1 - t / 100) * (t / 100) * control_points[1][1] + (t / 100) ** 2 * control_points[2][1]
        bezier_points.append((int(x), int(y)))

def get_input_coordinates(prompt_text):
    input_text = ""
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    try:
                        x, y = map(float, input_text.split(","))
                        control_points.append((x, y))
                        return
                    except ValueError:
                        print("Invalid input. Please enter coordinates in the format 'x, y'")
                        input_text = ""
                elif event.key == K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill(SCREEN_COLOR)
        prompt_surface = font.render(prompt_text, True, (0, 0, 0))
        screen.blit(prompt_surface, (10, 10))
        input_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(input_surface, (10 + prompt_surface.get_width(), 10))
        pygame.display.update()

def main():
    get_input_coordinates("Control Point 1 (x, y): ")
    get_input_coordinates("Control Point 2 (x, y): ")
    get_input_coordinates("Control Point 3 (x, y): ")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Clear screen
        screen.fill(SCREEN_COLOR)

        # Get mouse position and update the second control point
        mouse_x, mouse_y = pygame.mouse.get_pos()
        control_points[1] = ((mouse_x - ORIGIN_X) / SCALE_FACTOR, (ORIGIN_Y - mouse_y) / SCALE_FACTOR)

        # Calculate the Bezier curve points
        calculate_bezier_points()

        # Draw axis lines
        pygame.draw.line(screen, (0, 0, 0), (ORIGIN_X, 0), (ORIGIN_X, SCREEN_HEIGHT), 1)
        pygame.draw.line(screen, (0, 0, 0), (0, ORIGIN_Y), (SCREEN_WIDTH, ORIGIN_Y), 1)

        # Draw control polygon, control points, and Bezier curve
        draw_control_polygon()
        draw_control_points()
        draw_bezier_curve()

        # Update the screen
        pygame.display.update()

if __name__ == "__main__":
    main()
