# Greetings, traveler. 

Welcome to my Portfolio! I'm Nathaniel, my friends call me Ned, and I'm available at LinkedIn at [https://www.linkedin.com/in/nate-poland/](https://www.linkedin.com/in/nate-poland/). Please feel free to reach out with a message or connect with me there! 

## Recent Work
-  stock functions;
	- using `json API` requests
	- conditional logic

- algorithms;
	- `function wrappers`
	- `memoization` and `tabulation`
	
- option-contract class object;
	- with `@property` and `@[property].setter` function wrappers
	- `__init__, __repr__, __new__,`

-  Capstone-Rework -- streamlit Dashboard class as a script, on a Heroku remote server:
-  
	- Heroku campaign app here : [https://dunnhumby-app.herokuapp.com/](https://dunnhumby-app.herokuapp.com/)
	
## Next Steps:
- Automate model fit/test/eval for `Capstone-Rework`
- showcase some of my past work in SQL, using S3 buckets or etc. and develop new ETL systems based in SQL.

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
- understanding the _\_default__  dict() in a class definition
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
I'm excited to learn more about ML, but **in the past five months I've been focused on developing my skills as programmer by learning critical infrastructure tools like version control with Git, file systems, and remote environments and servers.** I have also done some deeper investigations into Python, which I've been studying for almost two years now. My work with Python this past fall gave me a solid footing for my "spike" learning into this new, invisible world of programming and data. 

# Data Lor
I know that data-based technologies will have a massive impact on the future. Recognizing the underlying mathematical distributions of real-world events is one thing; capturing them as data is something altogether different. Representing those distributions and using them to empower others in our community -- I believe that that is where the true value of data-based technologies will eventually be realized. 

I'm excited to share my work, and to learn from others in this truly fascinating field. If you have any questions about my work or want to talk about data ; -science, -engineering; or MLOps or similar, please reach out!
- 
## ENJOY!


