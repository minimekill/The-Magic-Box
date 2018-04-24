# The-Magic-Box

Purpose:
The purpose of the project is to combine a simple game with a neural network. The game will be a 2d platform, with a box in the middle serving as the "player" of the game. It wont be able to move left or right, but will be able to jump. The only obstacle in the game will be another box, the enemy, moving from the right to the left. The goal will be for the player to jump over the enemy box without touching it. The controller of the player will be a neural network , that will need to be trained to be able to determain when to jump. 

Obstacles:
The method to have a neural network determain when to jump is on its own simple enough. During a game, for every frame of the game we will send the neural network the X position of the enemy box. And the output of the neural network will be wether or not to jump. So for each frame of the game the neural network will have to decide. The problem comes when we wanna train the network. One idea is during the training, to start the game and send the network for each frame, the x values, and get the value wether to jump or not back. However, we cant tell the network if the answer to a frame is correct or not, until the game is complete. This means thatthere will be many training sessions waiting for a callback from the game to see wether the result of the choice was good or not. 

Another issue will be how a choice is affected by the outcome of a game. For example, say we start the game, and the network starts jumping before the enemy box is even close. If it does succeed to jump over the enemy box, it will get rewarded for thoose random jumps to begin with.

Goal:
Be able to handle and train a neural network that are controlling an element in a game. To be able to feed it the right information and to determain how to proberly build it, and train it.
