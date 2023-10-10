# Greetings, traveler. 

Welcome to my Portfolio! I'm Nathaniel, my friends call me Ned, and I'm available at LinkedIn at [https://www.linkedin.com/in/nate-poland/](https://www.linkedin.com/in/nate-poland/). Please feel free to reach out with a message or connect with me there! 

In my previous position as a Reporting Specialist with StackAdapt, I gained valuable real-world experience with Amazon RedShift/PostgreSQL databases; Tableau, Excel, and R. I'm happy to say I was also able to leverage the deep-dive I took into Python towards solving questions for my company and team, and working towards their specific needs and use cases.

In my free time, and then as one of two Team Leads for the department's new Python code base, I was able to develop a Python class to consolidate the typical data extraction process (from two Amazon RedShift databases, and a MySQL database, depending on the state of the requesting object), allowing for simplified code maintenance and extensibility through the use of child-scripts. 

The process was abstracted on a sql formula : metrics : required columns mapping file, in order to create a series of query statements to be executed at the appropriate database/table. Child scripts had a standardized .extract/.transform/.load/.run() methodology after implementing any additional steps in the child-specific \_\_init\_\_ phase.  I learned a lot in this process, and am excited to put everything I've learned about creating data pipelines, ETL, automated reporting, web APIs with real-world databases and cloud infrastructure to work at my next endeavor.  

## Summary of Portfolio

- Sudoku Game Solver
  	- class to solve Sudoku via human-readable logic (not random imputation)
   	- inheritance-based NineCell for Rows, Columns, and Nonograms
   	  
- Python Quiz Bot
  	- script-based quiz bot
  	- to practice list and dict indexing, before moving on to pandas etc. dataframe indexing
	- developed in my off-time while working as Python team lead
   
- FastAPI with SQLAlchemy ORM and Pydantic (dataclasses)
	- Defined database structure (SQLModel tables/SQLAlchemy declarative models) interacts cleanly 
   	 with the API transaction schemas defined by Pydantic and FastAPI. 
	 

-  stock functions (Nov 2021);
	- using `json API` requests
	- conditional logic

- algorithms (Nov-Dec 2021);
	- `function wrappers`
	- `memoization` and `tabulation`
	
- option-contract class object (Dec 2021);
	- with `@property` and `@[property].setter` function wrappers
	- `__init__, __repr__, __new__,`

-  DTCJ :
	- Sales data for purchases by 2500 households over 2 year span
	- Back-end API in Python project package
		- class-based SalesTable and RecommenderSystem wrapper objects
		- Visualizations (and cleaning) and Analysis in Pandas
	- Heroku campaign app here : [https://dunnhumby-app.herokuapp.com/](https://dunnhumby-app.herokuapp.com/)
	
## Next Steps:
- Automate model fit/test/eval for my 'deep dive' into class-based Data architecture and unit tests with Python and Pandas...[https://github.com/np1919/DTCJ](https://github.com/np1919/DTCJ)
- Revert the whole thing back to SQL.

# PROJECT DESCRIPTIONS
## FUNCTIONS for stock analysis

- `json API` batch requests 
- trend-reversal function
- conditional logic 

No-commission trading apps were coming in vogue before the beginning of the pandemic, and have been mainstream since. It was an easy jump, when the course finished, to try to apply what I had been learning to stock data.

### Time-series motivations

I actually wanted to learn more about timeseries -- maybe beat the market just a bit, right? but when I got to tensorflow, I realized that my technical knowledge needed to improve in order to get the most from that time -- even from a high level. This notebook is a conglomeration of functions, some more useful than others, which were the results of my work. 

I'm excited to learn more about window-related time-series modelling, but when I started defining how to make my own windows, I knew I had gone too far. There are platforms and packages which people far smarter than me have set up to perform precisely those tasks -- I just need to learn how to use them effectively. 

Update Feb 28 -- I've implemented a SalesTable object in my capstone which returns sales-over-timeseries for sales columns or section sales columns with appropriate aggregate information (rankings,labels, other features) attached by a common id key! I hope to use this (thin wrapper :)) class to improve the workflows of my data-related projects!

## ALGORITHMS using dynamic programming

- function wrapper
- understanding the _\_default_\_  dict() in a class definition (not to be confused with the defaultdict!)
- big O notation; `time` and `space` complexity of computation.
    
This is a freecodecamp video available on youtube which I actually started working on to prepare for the bootcamp. Having some background Python knowledge allowed me to see so much potential (for iteration) in the simple model codes that we were exposed to (in terms of logistic and linear regression, at least). With my new knowledge of pandas and numpy, the tabulation section was a breeze.

- **WIP: `graph algorithms` with `queues` and `stacks`**
    - node structure using simple dictionaries 

## `class` OBJECTS AND INHERITANCE; portfolio, holdings, and option-contract objects

- leveraging `yfinance` to populate options spreads
- inheritance-based class definitions, properties and setters
- plotting options contract spreads

Having learned a little bit about functions, I tried to apply that knowledge to some sort of inherited `class` structure; in this case, a [ strategy ]Portfolio creating ->[ STOCK ]Holdings objects -> [ STOCK ]Option Contracts. I still have a lot to learn about types and instances; polymorphism and inheritance; but I feel I made a good start with this work -- it uses @property decorators and @[ property ].setters. 

## CAPSTONE REWORK - THE COMPLETE JOURNEY

- Available at [https://github.com/np1919/Capstone-Rework](https://github.com/np1919/DTCJ) (not in this repo)
- grocery store sales data for 2500 households over 2 years.
- Extensive EDA and data-sleuthing/munging
- developing a Python-based package for cleaning, extracting, transforming, and testing data
- `SalesTable` object
- a rudimentary RecommenderSystem `class` object
- publishing a clean-data sales analysis of the products in 30 distinct advertising campaigns (before, during, and after), on `Heroku` using `streamlit`. 
 
 This rework is a huge project (to my experience thus far!), so if you're interested; please check it out. It's a WIP so that's all I'll say here. 
 
 
# About Me
I'm excited to learn more about ML, but **in the six months following my graduation from BrainStation's full-time data bootcamp, I focused on developing my skills as programmer by learning critical infrastructure tools like version control with Git, file systems, and remote environments and servers.** I have also done some deeper investigations into Python, which I've been studying since Spring 2020. My work with Python in fall 2021 gave me a solid footing for my "spike" learning into this new, ethereal world of programming and data. 

I know that data-based technologies will have a massive impact on the future. Recognizing the underlying mathematical distributions of real-world events is one thing; capturing them as data is something altogether different. Representing those distributions and using them to empower others in our community -- I believe that that is where the true value of data-based technologies will eventually be realized. 

I'm excited to share my work, and to learn from others in this truly fascinating field. If you have any questions about my work or want to talk about data ; -science, -engineering; or MLOps or similar, please reach out!
- 
## ENJOY!


