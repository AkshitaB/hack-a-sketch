# Hack-A-Sketch
Hackher413 hackathon project (2019)

# Introduction
Hack-a-Sketch is a web application that helps you learn how to draw, by letting you upload a picture (of whatever might catch your fancy), and then automatically generating steps (strokes) that make it easy for you to follow along!

When looking at the picturesque scenery, we are all inspired to pick up pencils and draw. The only problem is that some of us are really bad at drawing! Hack-A-Sketch is our attempt to make it easy for people like us to sketch something beautiful by following an easy, step-by-step guide.

![Hack-A-Sketch screenshot](https://github.com/AkshitaB/hack-a-sketch/blob/master/screenshots/screen3.png)

# Details

Hack-A-Sketch lets you upload pictures that you may have taken, to a server. The server processes the image and automatically detects contours and ranks them by ease-of-drawing (eg. larger contours first, smaller details later), and then presents them to you as step-by-step strokes that you can copy. Each step is highlighted in red color and repeatedly drawn on screen until you go to the next step. You can also see the eventual end result on the side.

# Team
Akshita Bhagia, Pracheta Boddavaram Amaranath, Seetha Chock, Amanda Neelapriyantha

# Requirements
python=3.6
flask
jQuery=3.2.1

# Installation and Use
1. Download and clone the git repo
2. Install Flask and necessary requirements.
3. Use the command to start flask on your local server - FLASK_APP=server.py flask run 
4. Follow the instructions on screen to begin drawing.
