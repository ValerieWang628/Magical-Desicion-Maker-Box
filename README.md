# CMU-15112-Term-Project -- The Magic Decision Box

## Project Description

This project is called The Magic Decision Box. This is a human-computer-interactive platform developed via Python which helps users to make decisions based on managment science principles.

This application is inspired by a course that I am taking this semester, called [Decision Analysis and Multi-criteria Decision Making](https://api.heinz.cmu.edu/courses_api/course_detail/94-833), taught by one of the greatest professors in Carnegie Mellon University. When I was taking this course, some of my classmates got confused by the concepts so I started to think about creating a computer program to solve the problems instead of doing it manually with paper and pencil. (Ironically, the computer program worked out so well that I now am getting obviously way more slower than before when I am manually approaching the problems. lol)

By inputting what decision a user wants to make, what available alternatives/options/candidates a user has, and how well each alternative is doing in terms of each attribute/feature/parameter(i.e. each feature specification of a given alternative), The Magic Desicion Box will use different algorithms to conclude a winner candidate for the user (and sometimes several if there is a tie).

Also, for users who only has a rough decision in his/her mind, the box will provide some keywords scraped through the google web as possible reference for a user if s/he cannot think of a reasonable parameter at once.


The algorithms this box will be implemented upon are multi-criteria decision making methods, 

1. [Swing Weights for Weighted Sum Model](http://miroslawdabrowski.com/downloads/MoV/The%20Simple%20Multi%20Attribute%20Rating%20Technique%20(SMART).pdf)

2. [TOPSIS](https://en.wikipedia.org/wiki/TOPSIS) (The Technique for Order of Preference by Similarity to Ideal Solution)

3. [AHP](https://en.wikipedia.org/wiki/Analytic_hierarchy_process) (Analytical Hierarchy Process)

4. Series of Rank Based Methods, including: 

    [Plurality Rules](https://en.wikipedia.org/wiki/Plurality_voting), [IRV](https://en.wikipedia.org/wiki/Instant-runoff_voting)(Instant Run-off Voting), [Borda Voting](https://en.wikipedia.org/wiki/Borda_count), and [Schulze’s Beatpath Method](https://en.wikipedia.org/wiki/Schulze_method).
    
Currently, the backend algorithms for plurality, IRV, Borda Voting and Schulze's Beatpath Method have been written and tested. Limited by the 15-112 project length, only the major part of the rank based method has been implemented on a visualized basis.

Later with more time, I will try to bind more features to this app, focusing more on the interaction part so that the swing weights, TOPSIS and AHP can be implemented.

## Competitive Analysis

This is not a business software. It is an educational tool. It helps naive users to quickly make an algorithm-based decision, and teaches students who are interested in Management Science to solve multi-criteria decision making problems.


## Structural Plan

The Magic Decision Box has two basic foundations: the algorithms and the user interface.

Once the user inputs data, the algorithms will transform the unstructured data into matrices and dictionaries. With calculation, a user interface will be binded to the program and allow users to play around with matrices.

Each algorithm will be implemented in functions with the matrix passed as the argument. 

E.g. 

function for plularity rule, will be laid out as pluralityElimination(matrix).

And the user interface will be implemented in a object-oriented way. 

E.g.

Clickable buttons will created via a Button class with class methods binded such as, ifClicked(self, *args), ifHovered(self, *args), etc.


These two parts will be developed separately and later the algorithm functions will be combined in a whole tkinter canvas.

Classes might be created in separate python files and later imported in the tkinter framework as the code quantity increases.


## Algorithmic Plan

For the algorithms, there are already some developed algorithms out there -- such as for finding the smith set, there are  Floyd–Warshall algorithm in time O(n ^ 3), Kosaraju's algorithm and Tarjan's algorithm in time O(n ^ 2).

However, due to the limited complexity of a use's decision, normally, a student/consultant equipped with theoretical algothm knowledge will be able to manually calculated the results on a piece of a scratch paper. Therefore, all the algorithms in this box will be implemented independently by the developer using merely 2-D lists, 2-D dictionary and sets manipulation(no Numpy/Pandas involved). The entire manipulation process strictly recreates how a human being will solve the problem.

The tricky part will lie in the function building part. Since many methods involve repetitive steps, recursion is definitely going to be used. Therefore, the developer created many test boards with different scenerios for testing purposes. For example, scenerios with equivocal winners, scenerios with Condorcet criterion failure, scenerios with monotonicity criterion failure, scenerios with multiple ties, etc. The algorithms will try their best to cover all the edge cases. 

For the user interface, the developer will set sequential stages and modes for the whole GUI(Graphic User Interface) that allows different interaction function to take place such as keyPressed, mouseTracker, mousePressed, etc.

The most difficult part will be a visualized stage where the box is able to come up with a furnished matrix and allows the user to play with the player/candidate/alternative nodes. In the canvas, a rectangle "playground" will be displayed with frame. Outside the playground, there are all nodes. A user will be able to drag nodes into the playground and press buttons to see how a node is connected to another. A user can also click another botton to clear connections. There is an important button that allows the user to instantly find the smith set.

This feature requires the button to activate the path finding functions. So the coordination of the algorithm functions and user interaface functions will be very important.

## Timeline Plan

Currently, the Smith Set Finder part works out very well.

Later, the developer will add more electorial methods, such as find condorcet winner, single elimination, etc.

## Version Control Plan

All the files, including static test matrices will be updated on Github: 

https://github.com/ValerieWang628/CMU-15112-Term-Project.git

This will store all the commits.

## Module List

For the algorithm part, no outside modules are used. Only 2-D lists, dictionaries, sets. Possibly, for convenience, some standard python modules might be used, such as math, collections, time, random, etc.

For the user interface part, only tkinter will be used.

For the webscraping-recommendation part, add-on modules will be used. These modules are,

JSON (used for converting scraped content into python dictionary)

urllib (used for url open)

bs4 (beautifulSoup4, used for webscraping)

nltk (natural language toolkit, used for user input text analysis)

re (regular expression, only used for puntuation removal)

numpy (only used for percentile calculation)


