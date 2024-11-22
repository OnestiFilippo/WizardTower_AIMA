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

  ![image](https://github.com/user-attachments/assets/63a3c95e-cee0-455e-a227-08b82534cff2)
  
<img src="[drawing.jpg](https://github.com/user-attachments/assets/63a3c95e-cee0-455e-a227-08b82534cff2)" alt="drawing" width="200"/>


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
  <p style="text-align:center;">$D_M + (C+1)^2 + (M+2)^2$</p>  
  where $D_M$ is the minimum Euclidean Distance between the wizard and the potion.
- if the wizard has a potion, there are creatures left in the grid and there are potions left in the grid:
  <p style="text-align:center;">$D_C+ (C+2)^2 + (M+1)^2$</p>
   where $D_C$ is the minimum Euclidean Distance between the wizard and the creature.
- if the wizard has not a potion, there are creatures left in the grid:
  <p style="text-align:center;">$D_C+ (C+2)$</p> 
  where $D_C$ is the minimum Euclidean Distance between the wizard and the creature.
- if there aren't any creature left in the grid:
  <p style="text-align:center;">$D_P$</p>
  where $D_P$ is the Euclidean Distance between the wizard and the portal.

## State Representation ##

The state is represented as a tuple that contains:
	•	The grid configuration.
	•	The number of remaining creatures.
	•	A variable indicating whether the wizard possesses a potion.
	•	The accumulated cost (optional).

 # Results #

Requirements

	•	Python 3.8+
