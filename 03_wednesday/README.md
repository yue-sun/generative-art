# Introduction to Generative Art and Scientific Visualization (January@GSAS 2023)

## Wednesday schedule

|   Time (ET)   |             Topic            | Instructor | Notebook |
|:-------------:|:----------------------------:|:----------:|:--------:|
|  10:00-10:10  |             Recap            |            |          |
|  10:10-10:55  | Elementary cellular automata |   Jovana   |  [01_cellular_automata.ipynb](https://github.com/yue-sun/generative-art/blob/main/03_wednesday/01_cellular_automata.ipynb)   |
| _10:55-11:00_ |   _Break/in-class activity_  |    _--_    |   _--_   |
|  11:00-11:45  |   Physical systems I: oscillators  |     Yue    | [02_physical_oscillators.ipynb](https://github.com/yue-sun/generative-art/blob/main/03_wednesday/02_physical_oscillators.ipynb) |
| _11:45-11:50_ |   _Break/in-class activity_  |    _--_    |   _--_   |
|  11:50-12:20  |  Physical systems II: reaction–diffusion  |     Nina    | [03_physical_reaction_diffusion.ipynb](https://github.com/yue-sun/generative-art/blob/main/03_wednesday/03_physical_reaction_diffusion.ipynb) |
|  12:20-12:30  |            Wrapup            |            |          |

## Day 3: Physical systems

### Part 1: Elementary cellular automata (Jovana)
Cellular automata are systems of discrete interacting cells whose state evolves according to a set of rules defined locally on a neighborhood. In this session, we observe how these simple systems can produce a remarkable array of patterns resembling biological and chemical phenomena. Cellular automata are a precursor to our later exploration of more complex pattern formation. We will also extend cellular automata to model discrete physical phenomena like diffusion-limited aggregation.

### Part 2: Physical systems I: Swarming and synchronization with oscillators (Yue)
In the first half of the physical systems, we will relax the constraint on discrete space and time and explore continuous physical systems. Specifically, we will implement the [Kuramoto model](https://en.wikipedia.org/wiki/Kuramoto_model) to simulate self-synchronization patterns of phase-coupled oscillators. Then we will extend the position constraint in the Kuramoto model to allow oscillators move freely in space, and simulate the [Swarmalator model](https://www.nature.com/articles/s41467-017-01190-3) to observe swarming and synchronization of oscillators. We will also animate the trail of oscillators to create some color-mixing patterns.

### Part 3: Physical systems II: Pattern formation with reaction–diffusion systems (Nina)
Reaction–diffusion systems are used to mathematically describe physical phenomena like spatial–temporal evolution of substance concentrations. But their solutions also include behaviors like self-organized patterns and traveling waves, often referred to as Turing patterns. In the second half of physical systems, we will focus on a two-component reaction–diffusion system, also known as the [Gray–Scott model](http://mrob.com/pub/comp/xmorphia/index.html). We will examine how different replenishment and depletion parameters lead to analogs of biological pattern formation, such as spots, stripes, and mazes.

## Recommended readings/videos:
- More on cellular automata:
    - [Cellular automaton](https://mathworld.wolfram.com/CellularAutomaton.html#:~:text=A%20cellular%20automaton%20is%20a,many%20time%20steps%20as%20desired.) on WolframAlpha
    - Game based on cellular automata: [Game of Life](https://playgameoflife.com/)
- More on physical systems:
    - Online interactive [Swarmalators](https://www.complexity-explorables.org/explorables/swarmalators/)
    - Prof. Steven Strogatz’s [2011 lecture](https://www.youtube.com/watch?v=5zFDMyQ8z8g) on coupled oscillators
    - Phillip Compeau’s [website](https://biologicalmodeling.org/prologue/) on the Turing model and reaction–diffusion
    - YouTube video: lecture on [modelling pattern formation in developmental biology](https://www.youtube.com/watch?v=Rv9NKugal3g)
    - Adobe [stock photos](https://stock.adobe.com/search?k=reaction%20diffusion) of reaction–diffusion art
- More on reaction–diffusion systems:
    - [Interactive RD visualization tool](https://www.karlsims.com/rdtool.html) by Karl Sims
    - [Reaction-Diffusion by the Gray-Scott Model: Pearson's Parametrization](http://mrob.com/pub/comp/xmorphia/index.html)
