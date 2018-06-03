<center><h1>The-Magic-Box</h1></center>


## Purpose:
The purpose of the project is to combine a simple game with a Machine learning module. The game will be a 2d platform, with a box in the middle serving as the "player" of the game. It wont be able to move left or right, but will be able to jump. The only obstacle in the game will be another box, the enemy, moving from the right to the left. The goal will be for the player to jump over the enemy box without touching it. The controller of the player will be a neural network or a decision tree , that will need to be trained to be able to determain when to jump.

## Setup:
Once this program has been downloaded from the git. You will need to install pygame in order to make the program run. 

on top of the Game class in the main file, in the init method, there are some values that can be changed in order to set the mode of the program.
The "mode" determains which machine learning module to use, by either writing 'neural_network' or 'decision_tree'. The learning value you can either write yes or no, to tell the neural network wether it should update its network, or not.


## What is going on:
The program is pretty much divided into 3 parts. 

The first part is the game it self, run from the main. We use the PyGame module to build the game-world with. The game contains 3 key parts: Sprites, where we have the classes for the game objects, ready for instantiation. Then we have the Settings, where we set various properties, used in the game. Lastly we have the Main, where all things combine. Main is constructed by 5 key methods, new: where we instantiate our class objects and PyGame dependencies - lastly starts the game loop, run: where our gameloop is defined, update: where we can reset things during the game, events: where the box actually jumps and enemies move. Its also possible to control box by keyboard, arrows and space, draw: here all sprites get added and game is shown to the viewer. 

The second part is the decision tree, which is som rather simple methos that figur out, wether it should jump or not. The way it works is we have a decision tree controller in which we say wether we want to jump at the lowest, highest or most optimal x value. X value being the distance from the jumping box to an obstacle. Before we can use decision_tree_middle(dtm), the most optimal jumping distance, we'll need to train it using decision_tree_lower(dtl) and decision_tree_upper(dtu). They work the same way, except dlt tries to jump as late as possible, where dtu tries to jump as early as possible. If they hit an obstacle they look at it's hight. If they have not encountered it before, then they create a new parameter in their corresponding jumpingParameter. They take the obstacle's hight at uses it as a key. If it's dtl then the value x is set to 0, if it's dtu then it's set to 100. If they have encountered the obstacle before, then dtl adds 1 to the value and dtu minus 1. When both dtl and dtu is trained, then we can use dtm. It simply minuses dtu parameters with dtl parameters, to find the middle.  

Finally the neural network makes up the last part. At the game start a neural network is created with random weights and stored in the game class in the network value. Every frame of the game, the distance to the enemy box is made, and divided by the total space between the enemybox and the player box. This number is then sent to the neural network along with the actual network which the game holds to the feed forward function in the magic_box_brain module, and a output array is returned. This array is the outputs of all the neurons, but we are only interested in the final neuron output. Then we determain wether this value is closer to 1.0 or 0.0 and turn that into wether to jump or not. If the game class learning value is set to yes, then after each time we ask the neural network, we store the result to the memory value. If the box fails to jump over the enemy box, we call the backprogate function in magic_box_brain module and give it the memory value along, to update the network and hopefully make it better at jumping.




## Obstacles:
The method to have a neural network determain when to jump is on its own simple enough. During a game, for every frame of the game we will send the neural network the X position of the enemy box. And the output of the neural network will be wether or not to jump. So for each frame of the game the neural network will have to decide. The problem comes when we wanna train the network. One idea is during the training, to start the game and send the network for each frame, the x values, and get the value wether to jump or not back. However, we cant tell the network if the answer to a frame is correct or not, until the game is complete. This means thatthere will be many training sessions waiting for a callback from the game to see wether the result of the choice was good or not. 

Another issue will be how a choice is affected by the outcome of a game. For example, say we start the game, and the network starts jumping before the enemy box is even close. If it does succeed to jump over the enemy box, it will get rewarded for thoose random jumps to begin with.

## Goal:
Be able to handle and train a neural network and a decision tree that are controlling an element in a game. To be able to feed it the right information and to determain how to proberly build it, and train it.






## The intelligent jumping box, exam agenda:
- Short intro  about Machine Learning
- About Machine Learning in python
- Our approach on our jumping box game
- Presentation of the game

