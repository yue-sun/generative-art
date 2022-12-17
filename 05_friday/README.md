# Introduction to Generative Art and Scientific Visualization (January@GSAS 2023)

## Friday schedule

|   Time (ET)   |           Topic           | Instructor | Notebook |
|:-------------:|:-------------------------:|:----------:|:--------:|
|  10:00-10:10  |           Recap           |            |          |
|  10:10-10:40  |       3D printing I       |   Jiayin   |          |
|  10:40-11:10  |       3D printing II      |   Jiayin   |          |
| _11:10-11:20_ | _Break/in-class activity_ |    _--_    |   _--_   |
|  11:20-11:50  |      3D printing III      |   Jiayin   |          |
|  11:50-12:20  |    GAN art and DALL-E 2   |  Nina, Yue |          |
|  12:20-12:30  |         Conclusion        |   Jovana   |          |

## Day 5: More tools and neural networks

### Part 1: 3D printing (Jiayin)
We will make a 3D model of a lamp, which you can print out after! It is inspired by a lamp I saw at Life Alive Organic Cafe at Harvard Square:

![3D printing idea](figs/3d_printing_idea.png)

Instead of a hanging lamp, we will create a standing lamp. We will create the bottom large piece, using parametric modeling with Mathematica. We will then use MeshMixer to process the bottom piece, and add a Voronoi tessellation pattern to it. We will create the smaller light cover piece with Mathematica too, where we will choose our geometry shape. We can explore the beauty of mathematical art. By exploiting the computing power of Mathematica, we can easily change the geometric parameters of the models, and everyone can design a unique lamp. We will use MeshMixer, MeshLab and NetFabb for post-processing of the model. If there is not enough time to cover the post-processing, a document will be provided for students to follow at home.

### Part 2: Generative art with neural networks (Nina and Yue)
While traditional generative algorithms use predefined rules to create patterns and images, generative neural networks learn these rules based on data, often enabling much more diverse and complex designs. In this session, we will create new generative art by implementing one popular generative model - the Generative Adversarial Network (GAN). We will also explore other neural network approaches, like neural style transfer to apply visual styles to other images, and the now-trending DALL-E 2 to generate images based on texts.

## Recommended readings/videos:
- More tutorials on 3D printing:
    - Jiayin will prepare a document for post-processing/fixing of the 3D models
- More on GANs and Pokémon:
    - [Generating art using GANs](https://blog.jovian.ai/generating-art-with-gans-352ceef3d51f)
    - [Monster GANs](https://medium.com/@yvanscher/using-gans-to-create-monsters-for-your-game-c1a3ece2f0a0)
- “Must-read” on neural style transfer:
    - The seminal paper ([Gatys et al. 2016](https://openaccess.thecvf.com/content_cvpr_2016/html/Gatys_Image_Style_Transfer_CVPR_2016_paper.html))
    - Interesting applications in fluid animation ([1](https://dl.acm.org/doi/10.1145/3355089.3356560), [2](https://www.youtube.com/watch?v=TyNlaBoP6oI), [3](https://cgl.ethz.ch/publications/papers/paperKim20a.php))
    - TensorFlow implementation ([code](https://www.tensorflow.org/tutorials/generative/style_transfer))
- More on DALL-E 2:
    - Official [website](https://openai.com/dall-e-2/) and [THE paper](https://arxiv.org/pdf/2204.06125.pdf)
    - Discussions on copyright issues ([1](https://www.technollama.co.uk/dall%C2%B7e-goes-commercial-but-what-about-copyright), [2](https://www.wired.com/story/openai-dalle-copyright-intellectual-property-art/), [3](https://kotaku.com/ai-art-dall-e-midjourney-stable-diffusion-copyright-1849388060))

## Work-in-progress: 3D printing software download instructions

Check back later!