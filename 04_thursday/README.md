# Introduction to Generative Art and Scientific Visualization (January@GSAS 2023)

## Thursday schedule

|   Time (ET)   |                   Topic                  | Instructor | Code/Slides | Software| Supplement |
|:-------------:|:----------------------------------------:|:----------:|:--------:|:--------:|:--------:|
|  10:00-10:10  |                   Recap                  |            |          |          |
|  10:10-10:40  |    Interactive coding in Processing I    |     Yue    | [00_processing_flocking.pdf](https://github.com/yue-sun/generative-art/blob/main/04_thursday/00_processing_flocking.pdf)<br>[01_hello_ellipse](https://github.com/yue-sun/generative-art/blob/main/04_thursday/01_hello_ellipse)<br>[01_hello_ellipse_mouse](https://github.com/yue-sun/generative-art/blob/main/04_thursday/01_hello_ellipse_mouse)<br>[01_hello_ellipse_trail](https://github.com/yue-sun/generative-art/blob/main/04_thursday/01_hello_ellipse_trail) |[Install Processing](#processing-installation-instructions)| [Additional examples](https://github.com/yue-sun/generative-art/blob/main/04_thursday/additional_examples)
|  10:40-11:10  |    Interactive coding in Processing II   |     Yue    | [02_flocking_exercise](https://github.com/yue-sun/generative-art/blob/main/04_thursday/02_flocking_exercise)<br>[02_flocking_solution](https://github.com/yue-sun/generative-art/blob/main/04_thursday/02_flocking_solution) |          |
| _11:10-11:20_ |         _Break/in-class activity_        |    _--_    |   _--_   |   _--_   |
|  11:20-11:50  |  Python scripting in animation software  |     Yue    |          |[Install Maya/Blender](#animation-software-installation-instructions)|
|  11:50-12:20  | Data visualization in animation software |     Yue    |          |          |
|  12:20-12:30  |                  Wrapup                  |            |          |          |

## Day 4: Tools for visualization

### Part 1: Introduction to Processing and flocking simulation (Yue)
Since its debut, [Processing](https://processing.org/) has become a popular programing language amongst artists to prototype ideas and generate interactive art. The simplicity of the language as well as its user interface/IDE has made it an attractive choice for creating coding, and, nowadays for scientific visualization. Given the limited time, we will only briefly introduce the language and how to start using it (though highly recommend learning via the YouTube channel). We will cover in class how to create geometric shapes, interactively move shapes based on mouse cursor location and keyboard inputs, create objects, and model a flocking simulation based on Craig Reynolds' [Boids](https://en.wikipedia.org/wiki/Boids) algorithm.

### Part 2: Python scripting and 3D data visualization in animation software (Yue)
We will introduce basic Python scripting in industry-standard animation software (Maya and/or Blender) to procedurally generate and animate objects. Time permitting, we will also briefly cover how to use built-in features to create physics-based animation. We will focus on visualizing 3D scientific data in animation software, i.e. using it as a texturing, lighting, staging and rendering tool. We will walk through how to render 3D fluid simulations with Python, from loading binary data to visualizing pathlines, assigning material textures, moving camera shots, lighting (with soft shadows), and rendering the final movie.

## Recommended readings/videos:
- More on the flocking simulation (or Boids):
    - [Boids website](https://www.red3d.com/cwr/boids/) by Craig Reynolds
    - [THE paper](https://dl.acm.org/doi/pdf/10.1145/37402.37406) (which introduced the three flocking rules)
- Additional resources to learn [Processing](https://processing.org/) (or [p5.js](https://p5js.org/)):
    - [_The Nature of Code_](https://natureofcode.com/) (book) by Dan Shiffman
    - [The Coding Train](https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw) (YouTube Channel)
- More tutorials on Python scripting in animation software:
    - [Python scripting in Maya](https://www.chadvernon.com/python-scripting-for-maya-artists/)
    - [Python for physical simulation in Blender](https://www.youtube.com/watch?v=KI0tjZUkb5A)

## Processing installation instructions

1. Download [Processing 4](https://processing.org/download) from the official website (free and open source!)
2. Enable [Python Mode](https://py.processing.org/) by clicking `"Manage Modes"` in the top-right drop down to install Python
    >This does not work if you're a Mac M1 user. A workaround is to open `"Tools > Manage Tools > Modes"` in the menu bar, then install `"Python Mode for Processing 4"`. Do not click `"Manage Modes"` at all! Or you'll need to quit and restart the software.
3. You can check out interactive code examples in  `"File > Examples..."` and double-click the example name to open the scripts

## Animation software installation instructions

1. Download Autodesk [Maya](https://www.autodesk.com/products/maya/overview) from the official website
    >Autodesk education & student access: "Students and educators can get free one-year educational access to Autodesk products and services, renewable as long as you remain eligible."
2. If Maya does not work out for the class, we will use Blender instead (free and open source!)
3. You can download [Blender](https://www.blender.org/download/) directly from the official website
