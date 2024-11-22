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

## Implemented Solution ##

After testing different searching algorithms like Breadth First, Depth First, Uniform Cost Search, A* Search implemented in the aima-python Python Library, I found that the best solution is obtained with the Best First Search with an heuristic function implemented like:

- if the wizard has not a potion, there are creatures left in the grid and there are potions left in the grid:
  ### <h3>$D_M + (C+1)^2 + (M+2)^2$ ###  
  where $D_M$ is the minimum Euclidean Distance between the wizard and the potion.
- if the wizard has a potion, there are creatures left in the grid and there are potions left in the grid:
  ### $D_C+ (C+2)^2 + (M+1)^2$ ###
   where $D_C$ is the minimum Euclidean Distance between the wizard and the creature.
- if the wizard has not a potion, there are creatures left in the grid:
  ### $D_C+ (C+2)$ ###
  where $D_C$ is the minimum Euclidean Distance between the wizard and the creature.
- if there aren't any creature left in the grid:
  ### $D_P$ ###
  where $D_P$ is the Euclidean Distance between the wizard and the portal.

## State Representation ##

The state is represented as a tuple that contains:
	•	The grid configuration.
	•	The number of remaining creatures.
	•	A variable indicating whether the wizard possesses a potion.
	•	The accumulated cost (optional).

# Results #

The implemented solution permits to apply different searching algorithms as mentioned before. 

## Breadth First Search ##

|              | **n° Nodi** | **Tempo (s)** | **Costo** |
|--------------|:-----------:|:-------------:|:---------:|
| _input.txt_  |     2388    |     0,037     |     24    |
| _iwt01.txt_  |     2972    |     0,037     |     26    |
| _iwt02.txt_  |    16032    |     0,609     |     30    |
| _iwt03.txt_  |             |               |           |
| _iwt03a.txt_ |             |               |           |
| _iwt03b.txt_ |             |               |           |
| _iwt03c.txt_ |             |               |           |
| _iwt04.txt_  |             |               |           |
| _iwt04a.txt_ |             |               |           |
| _iwt05.txt_  |             |               |           |

## Depth First Search ##

|              | **n° Nodi** | **Tempo (s)** | **Costo** |
|:------------:|:-----------:|:-------------:|:---------:|
|  _input.txt_ |     261     |     0,002     |     72    |
|  _iwt01.txt_ |     249     |     0,002     |     68    |
|  _iwt02.txt_ |     1219    |     0,041     |    166    |
|  _iwt03.txt_ |     1692    |     0,108     |    326    |
| _iwt03a.txt_ |     9509    |     1,798     |    1562   |
| _iwt03b.txt_ |    40992    |     37,326    |    5232   |
| _iwt03c.txt_ |             |               |           |
|  _iwt04.txt_ |             |               |           |
| _iwt04a.txt_ |             |               |           |
|  _iwt05.txt_ |             |               |           |

## Uniform Cost Search ##

|              | **n° Nodi** | **Tempo (s)** | **Costo** |
|:------------:|:-----------:|:-------------:|:---------:|
|  _input.txt_ |     2375    |     0,075     |     24    |
|  _iwt01.txt_ |     2895    |     0,081     |     26    |
|  _iwt02.txt_ |    13814    |     1,397     |     30    |
|  _iwt03.txt_ |             |               |           |
| _iwt03a.txt_ |             |               |           |
| _iwt03b.txt_ |             |               |           |
| _iwt03c.txt_ |             |               |           |
|  _iwt04.txt_ |             |               |           |
| _iwt04a.txt_ |             |               |           |
|  _iwt05.txt_ |             |               |           |

## Best First Search ##

|              | **n° Nodi** | **Tempo (s)** | **Costo** |
|:------------:|:-----------:|:-------------:|:---------:|
|  _input.txt_ |      84     |     0,002     |     24    |
|  _iwt01.txt_ |     101     |     0,002     |     26    |
|  _iwt02.txt_ |     130     |     0,005     |     30    |
|  _iwt03.txt_ |     269     |     0,015     |     58    |
| _iwt03a.txt_ |     705     |     0,096     |    160    |
| _iwt03b.txt_ |     4643    |     3,055     |    386    |
| _iwt03c.txt_ |    17473    |     17,463    |    919    |
|  _iwt04.txt_ |    98585    |    232,098    |    3433   |
| _iwt04a.txt_ |    122795   |    182,115    |    4207   |
|  _iwt05.txt_ |    191225   |    410,773    |    2976   |

