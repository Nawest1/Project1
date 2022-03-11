# Project

The overall aim of the project was:

To create a web application that integrates with a database and demonstrates CRUD functionality.
To utilise containers to host and deploy your application.
To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy your application.

Complete guidelines for the project:
https://qa-community.co.uk/~/_/projects/practical--dfe-cloud


Working app
https://drive.google.com/file/d/1vAVDv1VMTpbiaMoRVc18f2D8k1dcV4wL/view?usp=sharing

Docker app 
https://drive.google.com/file/d/1MLOguDwiXPQerxXCO6zXNYCm2Nj9nJkx/view?usp=sharing



I decided to create a web app that allows the user to construct portfolios of stock holdings.

Must Have (T-shirts sizes in brackets)
1-(m)	The user needs to be able to create any number of unique portfolios. (Create)
2-(l)	The user needs to be able to add stocks to these portfolios. (Update)
3-(m)	The user needs to be able to view the holdings of any portfolio (Read)
4-(s)	The user needs to be able to delete portfolios (Delete)

Should Have
5-(s)	The user needs to be able to associate position sizes to the stock holdings.(Create)
6-(m)	The user needs to be able to amend stock position sizes (Update)
7-(m) 	The user needs to be able to delete individual stocks from the portfolio

Could Have
8-(s)	The user needs to be able to add an  entry price for the stock holdings.
9-(m)	The user needs to be able to know what date the stock holding was added to the portfolio.
10-(l)	The user needs to be able to know what date a position size was amended.

Won’t Have
11-(l)	The user needs to be able to associate a portfolio manager with a portfolio
12-(l)	The user needs to be able to associate an owner with a portfolio

13-(xl)	The user needs to be able to see his sector/style exposure for a portfolio.
14-(m)	The user needs to be able to add an exit price for the stock holdings.
15-(l)	The user needs to be able to add an entry/exit price for any position amendment.
16-(xl)	The user needs to be able to calculate the p&l on any position that has been exited


An Entity Relationship Diagram has been added into github to show how I planned to structure the database. (Portfolio Holdings.jpg)

Risk assessment table has been added to github

Outcome

In brief - work, travel, and internet access (mostly internet access) intervened and I did not complete the project fully.

I did develop a functioning web app, running on a VM but using a local database (sql lite):

The files for this web app are on the “main” branch of my github.The following link shows this webapp in operation.

https://drive.google.com/file/d/1vAVDv1VMTpbiaMoRVc18f2D8k1dcV4wL/view?usp=sharing

Functioning features - the web app allows features basic CRUD capability - 1 - 6 on the list above have been enabled.


“Bugs” 
Obvious issues that need fixing on app as implemented:
(Bug shown in video) When a user amends a stock position size if there is more than one stock in the portfolio it automatically amends the size of the last stock to be added not necessarily the one selected.
User can add multiple instances of the same stock to a portfolio - additional positions in the same stock  should increment to existing positions

Feature 7 would be a fairly crucial feature to add in the next sprint (ability to delete individual stocks).
Some basic modifications to the design of the page would make it visually much more appealing eg. making positions appear alongside stocks rather than beneath.
Many of the other features would actually be able to be added fairly quickly. I did initially spend too much time thinking about database design and what I would like the app to do, and getting way ahead of myself, that in the context of being pressed for time anyways was a serious mistake.

I then attempted to link to containerize this web app, using Docker and link to a My SQL database. This is not functioning correctly. Please see 2nd video link below:

https://drive.google.com/file/d/1MLOguDwiXPQerxXCO6zXNYCm2Nj9nJkx/view?usp=sharing

I tried various interations of this code and was at times able to get between two and all three containers running but there was always an issue between nginx and the database.  At this point I ran out of time.

The code for the Docker version of the app is on the “docker” branch on my github for viewing. I deliberately didn’t push to ‘main’ as the code is not working.

In summary 
As a result  of not having a functioning Docker web app and running out of time I have

Neither written nor carried out any testing
No Jenkins files or CI/CD pipeline
Not connected via docker swarm
My project tracking is virtually non-existent. I did initially set up a Jira scrum but I never linked to github and quickly ceased to use it as pressures mounted.
My use of github was flakey - I did consistently push code to git-hub but it wasn’t until I started on the Docker element of the project that I set up a developer branch
My use of commenting on my code was poor.



