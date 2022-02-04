# Greetings, traveler. 

Welcome to my Portfolio! I'm Nathaniel, my friends call me Ned, and I'm available at LinkedIn at [https://www.linkedin.com/in/nate-poland/](https://www.linkedin.com/in/nate-poland/). Please feel free to reach out with a message or connect with me there! 

# About me -- switching careers

I've been learning Python since Spring 2020, when I gave up my job as the lead baker/mentor at a small social enterprise sourdough bakery in Toronto. Over 5 years working there, I was involved in the restructuring of various workflows which improved quality of work for our staff; various improvements in product quality or specification; and the training and mentorship of people from diverse backgrounds and life experiences. We were financially successful, being the beneficiaries of grants towards the purchase of a new industrial oven and mixer. 

I could work every station in the place, and sometimes I worked more than one at a time, or for extended hours -- on long fridays I would work the ovens from early morning until late afternoon (and occasionally until midnight, packaging) -- scoring the bread, loading it inside using an apparatus which rolled up and down the front of the oven; and finally removing the fresh-baked loaves. My team relied on my ability, I actively tried to make their jobs easier, and they knew that if they needed something covered or had questions, that I was someone they could come to. Unfortunately, I developed tennis elbow as the byproduct of a serious back injury I sustained in my first year there.

# New Beginnings
Moving into a new career is something I've embraced whole-heartedly; I love the opportunity to learn more math; learn new "languages". I'm familiar with a keyboard; and believe I now have the skills I need to be a contributing (if novice) member of a team. In this portfolio I'll showcase some of the work I've been doing since the bootcamp ended. 

I graduated from the BrainStation Data Science and Analytics bootcamp at the end of Summer 2021. 
The bootcamp experience was intense, but I learned so much about different `machine learning modelling techniques` that it totally blew my mind; especially thinking about organizing workflows and automating processes -- but also just how amazing it is that the world around us can be represented through mathematics and visualization; that as humans we're getting closer to understanding the true nature of the world around us and ourselves.

I'm excited to learn more about ML, but **in the past five months I've been focused on developing my skills as a Python programmer; as well as learning critical infrastructure rules like version control with Git, file systems, and remote environments and servers.** My work this past fall took me down a road of learning in this new, invisible world of programming and data, where although you can't smell, touch, or taste your ingredients -- with the right technique, you might just be able to make them sing.


## Intro: about the process
-  `stock functions`;
	- using `json API` requests
	- conditional logic

- `algorithms`;
	- `function wrappers`
	- `memoization` and `tabulation`
	- 
- option-contract `class` object;
	- with `@property` and `@[property].setter` function wrappers
	- `__init__, __repr__, __new__,` (more to go, here!)

-  `Capstone-Rework` -- `streamlit` Dashboard class as a script, on a `Heroku remote server`:
-  
	- Heroku campaign app here : [https://dunnhumby-app.herokuapp.com/](https://dunnhumby-app.herokuapp.com/)
	
## Next Steps:
- Automate model fit/test/eval for `Capstone-Rework`
- showcase some of my past work in SQL, using S3 buckets or etc. and develop new ETL systems based in SQL.


# ENJOY

I know that data-based technologies will have a massive impact on the future, and, well -- I just love learning about stuff; languages and math, for one. Recognizing the underlying mathematical distributions of real-world events is one thing; capturing them as data is something altogether different. Representing those distributions and using them to empower others in our community -- I believe that that is where the true value of data-based technologies will eventually be realized. 

I'm not there yet, that's for dang sure; but I'm excited to earn an opportunity to learn from others in this fast-growing field by showcasing my work.

# CAPSTONE REWORK - THE COMPLETE JOURNEY

- Available at [https://github.com/np1919/Capstone-Rework](https://github.com/np1919/Capstone-Rework) (not in this repo)
- Extensive EDA and data-sleuthing/munging
- developing a Python-based package for ETL
- a rudimentary RecommenderSystem `class` object
- publishing a clean-data sales analysis of the products in 30 distinct advertising campaigns (before, during, and after), on `Heroku` using `streamlit`. 
 
 This rework is a huge project (to my experience thus far!), so if you're interested; please check it out. It's a WIP so that's all I'll say here. 

# FUNCTIONS for stock analysis

- json API batch requests 
- trend-reversal function
- conditional logic 

No-commission trading apps were coming in vogue before the beginning of the pandemic, and have been mainstream since. It was an easy jump, when the course finished, to try to apply what I had been learning to stock data.

## Time-series motivations

I actually wanted to learn more about timeseries -- maybe beat the market just a bit, right? but when I got to tensorflow, I realized that my technical knowledge needed to improve in order to get the most from that time -- even from a high level. This notebook is a conglomeration of functions, some more useful than others, which were the results of my work. 

I'm excited to learn more about window-related time-series modelling, but when I started defining how to make my own windows, I knew I had gone too far. There are platforms and packages which people far smarter than me have set up to perform precisely those tasks -- I just need to learn how to use them effectively. 

# ALGORITHMS using dynamic programming

- function wrapper
- _\_default__ dict(); the unbound `class` definition (?)
- big O notation; `time` and `space` complexity of computation.
    
This is a freecodecamp video available on youtube which I actually started working on to prepare for the bootcamp. Having some background Python knowledge allowed me to see so much potential (for iteration) in the simple model codes -- that we were exposed to (in terms of logistic and linear regression, at least). With my new knowledge of pandas and numpy, the tabulation section was a breeze.

- **WIP: `graph algorithms` with `queues` and `stacks`**
    - node structure using simple dictionaries 

# `class` OBJECTS AND INHERITANCE; portfolio, holdings, and option-contract objects

- leveraging yfinance to populate options spreads
- attempts at inheritance-based class definitions, evnetually using properties
- callable plotting functionality

Having learned a little bit about functions, I tried to apply that knowledge to some sort of inherited `class` structure; in this case, a [ strategy ]Portfolio creating ->[ STOCK ]Holdings objects -> [ STOCK ]Option Contracts. I still have a lot to learn about types and instances; polymorphism and inheritance; but I feel I made a good start with this work -- it uses @property decorators and @[ property ].setters. 
