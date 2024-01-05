### Get to Da Choppa - Simulation

# Background

The original Get to Da Choppa game (written in pure JavaScript, HTML, and CSS) was hard... ***too*** hard. It was however, sufficiently complex so that tweaking one thing here or there at random wasn't enough to make it less hard. That's why I chose to build a simulation. The simulation allowed me to have the game play itself over hundreds of thousands of iterations... so I could figure out *why* it was **so hard**.

# Concept

In the main simulation, I've recreated -- as close as possible -- the original JS game. The main changes I've made are functions that allow the computer to "play" itself by automating turns, scoring, etc.

The second part of the simulation is the data analysis portion. In this portion, I examine the active player's ***Win-to-Loss Ratio*** and ***Win-to-Draw Ratio*** as well as a number of other metrics (e.g. how often each main *Boss* wins or how often the active player is even able to get to the main Boss).

The third part of the simulation involves the use of machine learning algorithms (mainly *random forests*) to assess feature importance. Namely, I wanted to see which aspects of the game contributed to game's outcome.
