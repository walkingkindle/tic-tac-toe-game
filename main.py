#TODO:Plan the game's structure and layout. Determine the different components basic design for the game.
#The center square will take minimal space and have a nice, green background,
#The first pop up will show selection for players and bots choice
#X will be blended with a nice red color and O blended with not sure yet color.

#TODO:Set up the project folder and files. Create a new folder for your project, and create subfolders for the various components of your game, such as the templates and static files.
#done
#TODO:Build the game board using HTML and CSS. Use HTML to create the basic structure of the game board, and then use CSS to style it.
#done
#TODO: Make the webpage more responsive.

#TODO:Create a Flask app. Set up a basic Flask app with a route for the home page that renders the HTML template for the game board.

#TODO:Implement the game logic. Create a function that handles the game logic and returns the updated game state. Use a data structure, such as a list or a dictionary, to keep track of the game board and the players' moves.
#TODO:Add interactivity with Flask routes. Use Flask routes to handle user clicks on the game board and update the game state accordingly. Use a function to check for winning combinations and display a winner or a tie.
#TODO:Test the game thoroughly. Play the game multiple times to ensure that it works as expected and there are no bugs or errors. Fix any issues that arise.
#TODO:Deploy the game. Host the game on a web server so that others can play it. Consider using a cloud hosting service, such as AWS or Heroku, to make deployment easier.
#TODO:Overall, creating a Tic-Tac-Toe game using Flask involves using a combination of HTML, CSS, and Flask routes to handle the game logic and user interaction. With prior experience in Flask, you should be able to quickly get started with building your game.

#---------------------------------------------------FLASK APP-----------------------------------------------------------
from flask import Flask, render_template, redirect, url_for, flash,g,abort,request
from flask_bootstrap import Bootstrap