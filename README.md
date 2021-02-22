# Brick Breaking Game

This game is the basic terminal version of the classic brick breaking game

Libraries used :

```bash
pip3 install colorama
```
## Execution

To play :

```bash
python3 main.py
```

## Controles

**b** - To release ball

**a** - To move the paddle left

**d** - To move the paddle right


## Features

* collision of bricks
* Catchable Powerup brick on collision of a brick
* Exand paddle 
* Shrink paddle
* Ball Multiplier
* Fast Ball
* Thru-Ball
* Paddle Grab
* Special Exploding of bricks adjacent or vertical to it

## Game Guide
* Collapse more bricks for more points. each collision of brick will give you 5 marks.Once you go down without hitting paddle, a life is lost.
* Grad powerups for more features. Each power up function will disapper automatically after 10 seconds. 

## Concepts Used

* Inheritance: Common attributes of the parent class inherited by the child classes. (Helps in avoiding redundant code)

	Used in bricks functionality. A common brick class is defined and colured bricks are inherited from it.

* Polymorphism: Utililizing the same function of a parent class for different functionalites of child classes based on the list of parameters passed

* Encapsulation: Every component on the board is an object of a class. This instantiation encapsulates the methods and attributes of the objects.

* Abstraction: The functions of each class hide the inner details of the function enabling users to use just the function name.

