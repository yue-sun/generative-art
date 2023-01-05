# Introduction to Generative Art and Scientific Visualization (January@GSAS 2023)

## Tuesday schedule

|   Time (ET)   |           Topic           | Instructor | Notebook |
|:-------------:|:-------------------------:|:----------:|:--------:|
|  10:00-10:10  |           Recap           |            |          |
|  10:10-10:40  |       Voronoi art I       |   Jiayin   | [01_voronoi_delaunay_art.ipynb](https://github.com/yue-sun/generative-art/blob/main/02_tuesday/01_voronoi_delaunay_art_.ipynb) |
|  10:40-11:10  |       Voronoi art II      |   Jiayin   |          |
| _11:10-11:20_ | _Break/in-class activity_ |    _--_    |   _--_   |
|  11:20-11:50  |      Voronoi art III      |   Jiayin   |          |
|  11:50-12:20  |    Space-filling curves   |   Jovana   |          |
|  12:20-12:30  |           Wrapup          |            |          |

## Day 2: Voronoi diagram and its application, and more

### Part 1: Voronoi/Delaunay tessellation art (Jiayin)
We will start by introducing the concepts of Voronoi diagram, and its duality, Delaunay triangulation, in 2D. We will see their importance and application in different fields across sciences. Then, we will tessellate a geometry domain with both Voronoi tessellation and Delaunay triangulation. We will overlay the tessellations on an image. We will then fill each Voronoi cell/triangle with color, to create mosaic versions of the image. We will use Python to accomplish this. 

### Part 2: Space-filling curves (Jovana)
This session explores how we can generate continuous line drawings, inspired by the [captivating works of mathematician Robert Bosch](https://www2.oberlin.edu/math/faculty/bosch/tspart-page.html). However, we put a twist on Bosch’s traditional approach of solving a traveling salesman problem to construct the drawings using a space-filling curve, a type of fractal whose limit has infinite length but finite area.

## Recommended readings/videos:
- Two Voronoi papers and a C++ software
    - [Voronoi cell analysis: The shapes of particle systems](https://arxiv.org/pdf/2201.10842.pdf)
    - [An extension to Voro++ for multithreaded computation of Voronoi cells](https://arxiv.org/pdf/2209.11606.pdf)
    - [Voro++](https://math.lbl.gov/voro++/): 3D Voronoi tessellation library
- 3B1B video: [Fractal charm: Space filling curves](https://www.youtube.com/watch?v=RU0wScIj36o)
- Bosch’s “optimization art”: [_Mathematician creates intricate drawings using one continuous line_](https://mymodernmet.com/robert-bosch-optimization-art/) by Margherita Cole