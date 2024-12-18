# WizardTower AIMA Search Strategy Contest

This project implements a solution to the Wizard Tower problem (described in the file wizardstower.pdf file) using informed and uninformed search algorithms. 
The contest consists on modeling the problem as a state-space search and testing different algorithms to find the optimal solution while minimizing the total cost.

## Problem Description ##

The problem is set on a 2D grid representing a tower. In this grid:
- The wizard (X) can move in 4 directions (up, down, left, right).
- Creatures (C) must be defeated to complete the level.
- Potions (M) can be collected to defeat creatures.
- A portal (P) represents the final exit point.
- Walls (B) block movement.
  
<p align="center"> <img style="" src="https://github.com/user-attachments/assets/63a3c95e-cee0-455e-a227-08b82534cff2" alt="Grid Example" width="300"/></p>

The wizard’s objective is to:
1.	Collect a potion to be able to defeat a creature.
2.	Defeat all creatures present in the grid.
3.	Reach the portal to complete the level.

The problem is modeled with:
- States: A configuration of the grid, the number of remaining creatures, and whether the wizard possesses a potion.
- Actions: Movement (UP, DOWN, LEFT, RIGHT), potion collection (POTION), and creature defeat (KILL).
- Costs: Every movement action costs 1 and potion collection and creature defeat cost 0

## State Representation ##

The state is represented as a tuple that contains:
- The grid configuration.
- The number of remaining creatures.
- A variable indicating whether the wizard possesses a potion.
- The accumulated cost (optional).

# Python Script Usage #

The *wizard_tower.py* script provides functionality for solving and visualizing the solution of the problem. The usage of this script is:

```
usage: wizard_tower.py [-h] [-e] [-g] filename

positional arguments:
  filename    Name of the input file

options:
  -h, --help  Show this help message and exit
  -e          Execute the solution found
  -g          Display the heuristic graph
```

## Parameters ##

``` filename ```

Specifies the name of the input file inside the *instances/* folder.

``` -e ```

View the execution of the solution found.

``` -g ```

View the heuristic function graph.

## Examples ##

Running the script on the input.txt file without displaying the graph and without displaying the solution.
```
python3 wizard_tower.py input.txt
```

Running the script on the input.txt file and displaying the heuristic graph.
```
python3 wizard_tower.py -g input.txt
```

Running the script on the input.txt file and displaying the solution found and the heuristic graph.
```
python3 wizard_tower.py -e -g input.txt
```

# Implemented Solution #

After testing different searching algorithms like Breadth First, Depth First, Uniform Cost Search, A* Search implemented in the aima-python Python Library, I found that the best solution is obtained with the **Best First Search** with an heuristic function implemented like:

- if the wizard has not a potion, there are creatures left in the grid and there are potions left in the grid:
  ### <h3>$D_M + (C+1)^2 + (M+2)^2$ ###  
  where $D_M$ is the minimum Euclidean Distance between the wizard and the potion.
- if the wizard has a potion, there are creatures left in the grid and there are potions left in the grid:
  ### $D_C+ (C+2)^2 + (M+1)^2$ ###
   where $D_C$ is the minimum Euclidean Distance between the wizard and the creature.
- if the wizard has not a potion and there are creatures left in the grid:
  ### $D_C+ (C+2)$ ###
  where $D_C$ is the minimum Euclidean Distance between the wizard and the creature.
- if there aren't any creature left in the grid:
  ### $D_P$ ###
  where $D_P$ is the Euclidean Distance between the wizard and the portal.

# Results #

The implemented solution permits to apply different searching algorithms as mentioned before. 
I tested different algorithms with different heuristic functions until I find the best solution that minimize the parameters on most of the input files given.

## Breadth First Search ##

|              | **n° Nodi** | **Tempo (s)** | **Costo** |
|--------------|:-----------:|:-------------:|:---------:|
| _input.txt_  |     2388    |     0.037     |     24    |
| _iwt01.txt_  |     2972    |     0.037     |     26    |
| _iwt02.txt_  |    16032    |     0.609     |     30    |
| _iwt03.txt_  |             |               |           |
| _iwt03a.txt_ |             |               |           |
| _iwt03b.txt_ |             |               |           |
| _iwt03c.txt_ |             |               |           |
| _iwt04.txt_  |             |               |           |
| _iwt04a.txt_ |             |               |           |
| _iwt05.txt_  |             |               |           |
| _iwt05b.txt_ |             |               |           |

## Depth First Search ##

|              | **n° Nodi** | **Tempo (s)** | **Costo** |
|:------------:|:-----------:|:-------------:|:---------:|
|  _input.txt_ |     261     |     0.002     |     72    |
|  _iwt01.txt_ |     249     |     0.002     |     68    |
|  _iwt02.txt_ |     1219    |     0.041     |    166    |
|  _iwt03.txt_ |     1692    |     0.108     |    326    |
| _iwt03a.txt_ |     9509    |     1.798     |    1562   |
| _iwt03b.txt_ |    40992    |     37.326    |    5232   |
| _iwt03c.txt_ |             |               |           |
|  _iwt04.txt_ |             |               |           |
| _iwt04a.txt_ |             |               |           |
|  _iwt05.txt_ |             |               |           |
| _iwt05b.txt_ |             |               |           |

## Uniform Cost Search ##

|              | **n° Nodi** | **Tempo (s)** | **Costo** |
|:------------:|:-----------:|:-------------:|:---------:|
|  _input.txt_ |     2375    |     0.075     |     24    |
|  _iwt01.txt_ |     2895    |     0.081     |     26    |
|  _iwt02.txt_ |    13814    |     1.397     |     30    |
|  _iwt03.txt_ |             |               |           |
| _iwt03a.txt_ |             |               |           |
| _iwt03b.txt_ |             |               |           |
| _iwt03c.txt_ |             |               |           |
|  _iwt04.txt_ |             |               |           |
| _iwt04a.txt_ |             |               |           |
|  _iwt05.txt_ |             |               |           |
| _iwt05b.txt_ |             |               |           |

## A* Search ##

|              | **n° Nodi** | **Tempo (s)** | **Costo** |
|:------------:|:-----------:|:-------------:|:---------:|
|  _input.txt_ |      94     |     0.001     |     24    |
|  _iwt01.txt_ |     281     |     0.003     |     32    |
|  _iwt02.txt_ |     215     |     0.005     |     30    |
|  _iwt03.txt_ |     491     |     0.016     |     56    |
| _iwt03a.txt_ |     1503    |     0.131     |    152    |
| _iwt03b.txt_ |    21513    |     6.098     |    414    |
| _iwt03c.txt_ |             |               |           |
|  _iwt04.txt_ |             |               |           |
| _iwt04a.txt_ |             |               |           |
|  _iwt05.txt_ |             |               |           |
| _iwt05b.txt_ |             |               |           |

## Best First Search ##

|              | **n° Nodi** | **Tempo (s)** | **Costo** |
|:------------:|:-----------:|:-------------:|:---------:|
|  _input.txt_ |      84     |     0.002     |     24    |
|  _iwt01.txt_ |     101     |     0.002     |     26    |
|  _iwt02.txt_ |     130     |     0.005     |     30    |
|  _iwt03.txt_ |     269     |     0.015     |     58    |
| _iwt03a.txt_ |     705     |     0.096     |    160    |
| _iwt03b.txt_ |     4643    |     1.549     |    386    |
| _iwt03c.txt_ |    17473    |     9.688     |    919    |
|  _iwt04.txt_ |    98585    |    119.489    |    3433   |
| _iwt04b.txt_ |    122795   |    101.120    |    4207   |
|  _iwt05.txt_ |    191225   |    222.373    |    2976   |
| _iwt05b.txt_ |    50590    |     36.212    |    3272   |

