# Lab 0


This assessment contains materials that may be subject to copyright and other intellectual property rights. 

Modification, distribution or reposting of this document is strictly prohibited. Learners found reposting this document or its solution anywhere will be subject to the college’s Academic Integrity policy.

This lab is not worth any marks.

## Create a private repository for the course.


1. If you do not have a github account, please create one first:
    * [get your github id](https://github.com)
    * You will use the same github account throughout this course and beyond.  Pick a userid that you can be ok with professionally.
    * **Do not use private info like your student number in your github id.**
2. Create a **private** repository in your GitHub account.
3. Add your professor as a collaborator. In GitHub web page of your repository, go to `Setting` / `Collaborators and Teams` / `Add People`. Ask in class for your professor GitHub account.
4. In your repository create a folder named `lab-0`. Put in this folder all relevant files for your lab (see below what you have to accomplish). Use `lab0.md` for text and `lab0.py` for the python code.


## Coding in Python


* In the file lab0.py there is a declaration for a function named sum(num1,num2) which will return the sum of the two numbers passed into the function
* Write the program with a mistake in it (for example: return num_1 * num_2).
* You can test it locally by using the command: `python lab0_tester.py`.  At this point, the test should not pass.
* Run the test locally to verify that it works (the test should not pass).
* Fix the function by writing the function correctly.
* Run the test locally to verify that it works
* add, commit and push the file into your repo

## LaTex

In this course there will be times when you will need to write mathematical expressions.  For example, here is the ugly math version of the quadratic formula:

```
x = [ -b +/- sqrt(b^2-4ac) ]/2a
```

However, some of you may wish to make it look like an actual mathematical expression.  To do this, you can make use of LaTex.  LaTex is widely used for producing beautiful math.  It is also used in academic circles for writing papers.  To create a mathematical expression inline, delimit the expression with ```$```.  To put it by itself, delimit the expression with ```$$```.  For example:

Here is a sentence with the  quadratic formula $x = {-b \pm \sqrt{b^2-4ac} \over 2a}$ embbed inline.

The above was created with this in the markdown file:

```
Here is a sentence with the  quadratic formula $x = {-b \pm \sqrt{b^2-4ac} \over 2a}$ embbed inline.
```

This next bit, where the formula sits by itself:

$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$

was created using:

```
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$
```

### Task:

Write the formula for calculating the length of the hypothenus (c) given right angle triangle with side lengths a and b in LaTex.   

That is write the following formulas in latex: 

* hypotenus of a right angle triangle: c = sqrt(a^2 + b^2)
* geometric series: sum from i=0 to n (ar^i)
* arithmetic series closed form: sum from i = 1 to n (i) = 1 + 2 + 3 + 4...n=(n)(n+1)/2


#### References

* [Video about LaTex](https://www.youtube.com/watch?v=NXW4cbHBthY)
* and for those who really hate LaTex... word's equation editor can produce LaTex output of a formula entered into the equation editor... but its a bit flakey.


## Graphs

From time to time you may be asked to produce a graph as part of an assessment.  This graph will need to be correctly placed into your .md so that it is part of the text. 

### Task:

Create a simple graph showing a fake survey results on favorite icecream flavours using any spreadsheet program you wish

If you are using excel to create the graph:
- save the graph as an image
- in github, click into the lab0.md file where you want graphic to go
- click on pencil icon at top
- position cursor to place where you want image to go
- drag and drop image into browser window that has the file opened for editing
- give it a few seconds and you should see some an image link text ```![](https://somegithubusercontenturl)```
- move that around if it isn't in the correct place

If you are using googlesheets
- get a shared (non-interactive) link.
- in your lab0.md file add an image link using the url you got from the graph created by google sheet
- alternatively get image and follow the same instructions as that for excel.

## Reflection:

### Task: 

Write a short paragraph about what you found interesting about lab 0.  Tell us something about what you hope to learn and explore for the course.



## Submission:

After you have completed lab, submit the link to your lab0.md file into blackboard for lab 0.
