
# The Magical Decision Maker Box

## What is this project about?

This project is called The Magical Decision Maker Box. This is an optimal solution finder application developed via Python which helps users make decisions based on management science principles. This is also the term project I had during my course -- [Fundamentals of Computer Science and Programming](https://www.cs.cmu.edu/~112/). The goal of this application is to gamify the boring algorithms so that users will easily learn how to make scientific decisions, because I believe that, lecture is not the only way to teach -- making algorithms interactive and gamified is also cool😎!!!

  
<!---👉🏼[Click here to see the simplified video demo of this project on Youtube.](https://www.youtube.com/watch?v=SCq7pKkoa50)--->

👉🏼Snapshot of the video demo:
<p align="center">
    <img src= "https://static.wixstatic.com/media/5a3935_94130e2adf2b4fbf82f9b82405c5fdc7~mv2.png/v1/fill/w_610,h_390,al_c,q_85,usm_0.66_1.00_0.01/videoSnap.webp" width = "610" height = "390">
<p>

## Why did I start this project?
This application is inspired by a course that I took in Fall 2018, called [Decision Analysis and Multi-criteria Decision Making](https://api.heinz.cmu.edu/courses_api/course_detail/94-833), taught by one of the best professors in Carnegie Mellon University. We were asked to calculate the results using paper and pencils to reproduce the methods taught in class. Many classmates of mine had huge trouble with this because the algorithms baffled them. Thus, I started to develop a computer program that allows step-by-step algorithm reproduction in drag-n-click style that allows uses to learn in their own pace. 

(😅Ironically, the computer program worked out so well that I now am getting obviously slower than before when I was manually solving the problems. lol.)

## How does this tool work?

### Input needed

This tool asks for following input: 

1. What decision does the user want to make? (aka. the decision subject)

2. What choices/candidates does the user have in mind? (aka the candidates that will be competing each other)

3. What are the attributes/features/parameters that the user care about when making this decision? 

4. What are the specifications of each attribute of each candidate? (aka. the specification metric)

5. What is the weight of each attribute in the user's mind? (aka. how important is each attribute, compared with each other)

6. What are the sweet spot directions of each attribute? (aka. for each attribute, does the user want the value to be the higher the better?)

### What algorithms/methods are used here?
In my Decision Analysis class, we were taught methods below:

1. [Swing Weights for Weighted Sum Model](http://miroslawdabrowski.com/downloads/MoV/The%20Simple%20Multi%20Attribute%20Rating%20Technique%20(SMART).pdf)

2. [TOPSIS](https://en.wikipedia.org/wiki/TOPSIS) (The Technique for Order of Preference by Similarity to Ideal Solution)

3. [AHP](https://en.wikipedia.org/wiki/Analytic_hierarchy_process) (Analytical Hierarchy Process)

4. Series of Rank Based Methods, including: 

    [Plurality Rules](https://en.wikipedia.org/wiki/Plurality_voting), [IRV](https://en.wikipedia.org/wiki/Instant-runoff_voting)(Instant Run-off Voting), [Borda Voting](https://en.wikipedia.org/wiki/Borda_count), and [Schulze’s Beatpath Method](https://en.wikipedia.org/wiki/Schulze_method).

### The general workflow of the Box

With the input above, the Box will be able to come up with a matrix with the given information, transform the matrix into a rank-based one, and present results reached from different algorithms in the back end. The result will be the winner candidate(s) for the user (sometimes there are several winners if there is a tie).

👇🏻Screenshot: User input matrix (left) and transformed rank-based matrix:
📍Users can hover the cursor onto the grid so that the highlight mapping shows how each cell is transformed.
<p align="center">
  <img src="https://static.wixstatic.com/media/5a3935_fe006b6eee9c499ba57ff055fd142e16~mv2.png/v1/fill/w_600,h_320,al_c,q_85,usm_0.66_1.00_0.01/matrix_PNG.webp" width="600" height="320">
</p>



👇🏻Screenshot: The candidate battle ground:
📍Users can drag the competing candidates to the main pathground, and easily arrange the positions at their own will. User actions: single click to select; drag to move nodes; double click to release nodes; drag and move to arrange positions.
<p align="center">
  <img src="https://static.wixstatic.com/media/5a3935_06323feca3b54c38892ca8d3d7cedd8c~mv2.png/v1/fill/w_600,h_400,al_c,q_85,usm_0.66_1.00_0.01/clickndrag_PNG.webp" width="600" height="400">
</p>




👇🏻Screenshot: Step-by-step beathpath relation:
📍Select any of the candidates, and click "Show One Way Path", users can examine all the one-way relations between this particular candidate and another.
<p align="center">
  <img src="https://static.wixstatic.com/media/5a3935_654db6db482e4d51b8c2ab722c060ca1~mv2.png/v1/fill/w_600,h_430,al_c,q_85,usm_0.66_1.00_0.01/Path1_PNG.webp" width="600" height="430">
</p>



👇🏻Screenshot: Detailed interactable calculations:
📍Select any of the score nodes here, users can check the calculation process of that particular beatpath.
<p align="center">
  <img src="https://static.wixstatic.com/media/5a3935_e6ac9cf2d9c045108e9976cb2a25591f~mv2.png/v1/fill/w_600,h_420,al_c,q_85,usm_0.66_1.00_0.01/calc_PNG.webp" width="600" height="420">
</p>



👇🏻Screenshot: Two-way paths for further explanation:
📍Select any of the score nodes here and click "Show Two Way Path", users can check the two-way beatpaths for supplemental information.
<p align="center">
  <img src="https://static.wixstatic.com/media/5a3935_bd2df179665f42e1949ace28eb4569f8~mv2.png/v1/fill/w_600,h_430,al_c,q_85,usm_0.66_1.00_0.01/two-way_PNG.webp" width="600" height="430">
</p>



👇🏻Screenshot: Find the winner -- the Smith Set:
📍Click "Show Smith Set", and the winner among the candidates will be highlighted in yellow/gold. Boom! The winner is here.
<p align="center">
  <img src="https://static.wixstatic.com/media/5a3935_94130e2adf2b4fbf82f9b82405c5fdc7~mv2.png/v1/fill/w_610,h_390,al_c,q_85,usm_0.66_1.00_0.01/videoSnap.webp" width="610" height="390">
</p>




<!---### A simple example -- Valerie doesn't know what car to purchase.

Here is a simple decision making process example that better explains the workflow of this tool.
Suppose Valerie wants to purchase a car. The input would be:

1. Decision subject: Valerie wants to purchase a car.
2. Candidates: Valerie currently has 4 cars in her mind -- Xelus 450, Cuara RDX, Stela Model X, and Dacillac XT6.
3. Attributes: Valerie takes 4 main aspects in the choice-making -- price, car length, mpg(miles per gallon), and cargo capacity.
4. Specifications: With a quick lookup online, Valerie has found the price, length, mpg, and capacity for the four models respectively.
5. Attribute priority: Valerie thinks the price of the car models is the most important, then the mpg, then the capacity, and finally length. After a swing weights test given by this application, the tool helped her quantify and normalize her attribute priority: she would give 0.63 for price (base weight is 1),  0.21 for mpg, 0.1 for capacity, and 0.06 for length.
6. Attribute pos/neg: Valerie wants the price to be the lower the better; mpg the higher the better; capacity to be high; and length to be low. Thus, for the price, length, mpg and capacity, the direction will be: neg, neg, pos, and pos. --->



    






<!---## Competitive Analysis

This is not a business software. It is an educational tool. It helps users to quickly make an algorithm-based decision, and teaches students who are interested in Management Science to solve multi-criteria decision making problems in a fun way. --->

## Technical Highlights🖖🏻

1. Minimal dependency on framework: The only framework used here is the built-in Python [tkinter](https://docs.python.org/3/library/tkinter.html).  tkinter is used only for the GUI. Other than that, this tool does not depend on any modules/frameworks. Users won't have to install extra packages.

2. Minimal dependency on data structures: As no extra modules are imported, this tool does not rely on data structures from Numpy or Pandas, like Numpy arrays or Pandas DataFrame. All the algorithms are reproduced via the simplest structures: sets, tuples, lists and dictionaries, including nested lists and dictionaries.

3. Minial dependecy on algorithms: I did not refer to any existing algorithms online -- I reproduced the whole process by applying what my professor has taught me in pencil and paper to the computer program. 
👉🏻Let me explain: As many decision-making problems are essentially graph theory problems in Mathematics, there are already instant algorithms written for computer programs, such as [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd–Warshall_algorithm) in time O(n ^ 3), [Kosaraju's algorithm](https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm) and [Tarjan's algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm) in time O(n ^ 2). However, as my initial intention was to enable my fellows to solve the problem by hand, the ready algorithms are not applicable.

4. Smart use of backtracking: As this project also serves as my term project for my computer science class, I was asked to have enough programming complexity. Thus, I used backtracking (a kind of recursion) to my program, which worked out pretty efficiently. I am very proud of using minimal data structures to reproduce these algorithms. 

5. Homemade UI widgets: As only tkinter was used (its UI components really suck, no offense), I have to hand code the very basic components on my own. Thus, I coded the click-n-drag, cursor hovering visual effects, intelligent two-way arrow pointing, and smart node spacing to guarantee the quality of the UI. 

6. UI/UX design: This is the very first project that requires myself to design the UI/UX. I think I did a great job in creating an intuitive and interactive experience for the users. I also had several users to test my app, which allowed me to tune and tweak the frontend through iterations.


<!---## Structural Plan

The Magic Decision Box has two basic foundations: the algorithms and the user interface.

Once the user inputs data, the algorithms will transform the unstructured data into matrices and dictionaries. With calculation, a user interface will be binded to the program and allow users to play around with matrices.

Each algorithm will be implemented in functions with the matrix passed as the argument. 

E.g. 

function for plularity rule, will be laid out as *pluralityElimination(matrix)*.

And the user interface will be implemented in a object-oriented way. 

E.g.

Clickable buttons will created via a Button class with class methods binded such as, ifClicked(self, *args), ifHovered(self, *args), etc.


These two parts will be developed separately and later the algorithm functions will be combined in a whole tkinter canvas.

Classes might be created in separate python files and later imported in the tkinter framework as the code quantity increases. --->


<!---## Algorithmic Plan

For the algorithms, there are already some developed algorithms out there -- such as for finding the smith set, there are  [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd–Warshall_algorithm) in time O(n ^ 3), [Kosaraju's algorithm](https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm) and [Tarjan's algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm) in time O(n ^ 2).

However, due to the limited complexity of a use's decision, normally, a student/consultant equipped with theoretical algothm knowledge will be able to manually calculated the results on a piece of a scratch paper. Therefore, all the algorithms in this box will be implemented independently by the developer using merely 2-D lists, 2-D dictionary and sets manipulation(no Numpy/Pandas involved). The entire manipulation process strictly recreates how a human being will solve the problem.

The tricky part will lie in the function building part. Since many methods involve repetitive steps, recursion is definitely going to be used. More specifically, [backtracking](https://en.wikipedia.org/wiki/Backtracking) is the critical part of the core algorithms here. Therefore, I created many [test boards](https://github.com/ValerieWang628/the-magic-desicion-maker-box/blob/master/TP_RankBased_TestBoard.py) with different scenerios for testing purposes. For example, scenerios with equivocal winners, scenerios with Condorcet criterion failure, scenerios with monotonicity criterion failure, scenerios with multiple ties, etc. The algorithms will try their best to cover all the edge cases. 

For the user interface, I set sequential stages and modes for the whole GUI(Graphic User Interface) that allows different interaction function to take place such as keyPressed, mouseTracker, mousePressed, etc. Thus, the algorithm files and corresponding algorithm-widget files are firm combinations.

The most difficult part will be a visualized stage where the box is able to come up with a furnished matrix and allows the user to play with the player/candidate/alternative nodes. In the canvas, a rectangle "playground" will be displayed with frame. Outside the playground, there are all nodes. A user will be able to drag nodes into the playground and press buttons to see how a node is connected to another. A user can also click another botton to clear connections. There is an important button that allows the user to instantly find the smith set.

This feature requires the button to activate the path finding functions. So the coordination of the algorithm functions and user interaface functions will be very important. 
--->

## How to run this program

All Python files here are linked internally. It is designed like a chain with one biting another's tail. Therefore, after downloading all the files in a folder, the [run.py](https://github.com/ValerieWang628/the-magic-desicion-maker-box/blob/master/Run.py) will serve as a trigger. Run this [run.py](https://github.com/ValerieWang628/the-magic-desicion-maker-box/blob/master/Run.py) file will be enough for users to get the whole program moving.

## Detailed how-to

1. Run the run.py file, you will see a welcome page. Type your name in and hit 'start'. 

2. Type whatever decision you are making, how many alternatives you have(the candidates that you have difficulty choosing), and how many attributes there are(the different aspects that you care about).

3. Quickly lookup the specifications online of each candidate.

4. Then, the app will convert your original specification matrix into a rank-based matrix. Within each attibute, the alternative with the best specification will be put in the first rank, and the second best alternative gets to be put at second, and so on. If you are confused with the rank base transformation, hover your cursor onto the cell on either matrix, and the other matrix will show where the corresponding cell is.

5. With the matrix done, you are now at the candidate playground. In this battle field, you get to see how one alternative beats another, and who is the final winner. The calculations are hidden in each score node. If you click the node, the matrix will come up and tell you how the score is derived.

6. For a quick answer, click the 'Show Smith Set' button. Winner(s) will be illuminated in a gold color.

## Future scope

I plan to further expand the algorithms and methods as there are still a lot of interesting decision-making systems out there.
