
# Bezier Curve Visualization

![Demo](demo.gif)

## Description

This is a simple Python program using Pygame to visualize a smooth Bezier curve based on 4 control points. The user can enter the coordinates for the control points and interactively update the fourth control point using the mouse cursor to observe changes in the Bezier curve.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Features](#features)
- [License](#license)


## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/Aayush518/bezier-curve-visualization.git
```

2. Install the required packages using pip:

```
pip install pygame
```

## How to Use

1. Run the program:

```
python main.py
```

2. The program will prompt you to enter the coordinates for 4 control points. Each coordinate should be entered in the format `x, y`, where `x` and `y` are floating-point numbers.

3. After entering the control points, a window will open displaying the Bezier curve based on the control points.

4. You can interactively update the fourth control point by moving the mouse cursor. The curve will update accordingly.

5. Close the window to exit the program.

## Features

- Allows the user to input coordinates for 4 control points to define the Bezier curve.
- The Bezier curve is updated smoothly and interactively based on the control points and the position of the fourth control point.
- The program visualizes the Bezier curve, control points, and control polygon.


