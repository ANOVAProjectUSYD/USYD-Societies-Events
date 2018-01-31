# USYD-Societies-Events

This project seeks to scrape Facebook data regarding events from the top 20 biggest societies at USYD. From that, we then seek to analyse what are the factors that drive event attendance. Here, we seek to deploy models to analyse the casual relationships between event attendance and such factors such as the location of the event, timing during the semester and day, whether catering was provided, and more.

## Task for Tom
Hey Tom, thanks for agreeing to help out!

In a nutshell, I need your help with scraping data from the [FB Graph Api](https://developers.facebook.com/docs/graph-api/). I have already scraped data from USYD Website and FB of who the biggest societies at USYD are, that's listed in the final_data.csv file. I'll need you to scrape data on these top 20 societies via Facebook, I've provided their FB id's to help you. Basically, I need you to scrape all the events that these societies have held for past few years (as much as you can get). Alongside that, I'd like to collect information about the event including: number of people who attended, people who said maybe, people who said no, name of event, date of when event was held, location of event, description of event, number of people invited to event, start time of event, and anything else you find interesting. What we like to then do with this data is do some data science work on seeing what factors drive event's attendance at USYD. Afterwards, I'd like you to write everything out to a csv file, where since we will have multiple events for each society scraped, have it so that you also create a new field called Society so we know which society hosted which events, and the rest of the fields are just simply each piece of information you are able to scrape.

Here's a [good link](https://developers.facebook.com/tools/explorer/?method=GET&path=180DegreesConsulting&version=v2.12) of using FB Graph API explorer to look at things. You can use my token to access it which is in the file already.

Primarily I've started some things with facebook_final_scrape.py file so you can take a look there. You can look at facebook_initial_scrape.py on some ways I've used to interact with FB Graph API to scrape the initial data.

Thanks again!!!
## Requirements

All packages used are in the [requirements.txt](https://github.com/chrishyland/USYD-Societies-Events/blob/master/requirements.txt) file.

### Getting Started

 Files to read in order to follow along with the project.

1) usu_scrape.py scrapes the data from the USU website and collects information regarding the societies. Creates a socities_facebook.csv file.

2) facebook_pages_scrape.py then scrapes basic information from Facebook regarding these societies and creates a final_societies_facebook.csv file.

3) Most-Likes-Analysis explores the final_societies_facebook.csv file in depth and identifies top 20 societies. Then creates a final_data.csv file.

More to come!

## Built With

* BeautifulSoup

* Jupyter Notebook

* Care and Coffee

## Authors

The ANOVA Project - Chris Hyland

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgements

Amazing links that helped me get started:

* http://minimaxir.com/2015/07/facebook-scraper/

* https://github.com/minimaxir/facebook-page-post-scraper/blob/master/examples/how_to_build_facebook_scraper.ipynb

* Facebook Graph API

* And lots of coffee!
