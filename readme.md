# Judgement the game

This application aims to provide a simulator to play Judgement and provide a full breakdown of an optimal way to play the game. A GUI with buttons will be present to start the game and execute actions as each player, a chart of best plays will be available.

## Graphical feature list
- GUI with list of cards in hand and already played with game state information
- Buttons which allow you to play a card

## Statistical features
- Based on current game state (trump, cards played in the round, cards played in this turn, player guess, and cards in hand) highlight which card would get closest to achieving your guess
- Algorithm/model to find the minimum difference between expected hands won and aimed hands won
- Game trees to calculate expected hands won for each card

## Current considerations
- Create proper project structure which allows the testing files to read the src module and will allow to scale up to being a GUI application
- Create docker image/ conda dependencies list
- Creating a shell GUI which will scale to have more buttons available
- Continue creating the game logic such as defining user guesses and creating turn logic for and tracking player wins and scores
