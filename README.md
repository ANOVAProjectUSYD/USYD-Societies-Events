# USYD-Societies-Events

This project seeks to scrape Facebook data regarding events from the top 20 biggest societies at USYD. From that, we then seek to analyse what are the factors that drive event attendance. Here, we seek to deploy models to analyse the casual relationships between event attendance and such factors such as the location of the event, timing during the semester and day, whether catering was provided, and more.

The first step was required us to scrape all the societies at USYD from the [USU](http://www.usu.edu.au/Clubs-Societies.aspx) website. This was done in the usu_scrape.py file with the output being the usu_societies.csv file. After that, we then scraped the number of likes for each society as seen in the facebook_likes_scrape.py file which then gives us the output of final_societies_facebook.csv file. Then, running some simple data analysis in the Most-Likes-Analysis.ipynb, we were able to determine some interesting statistics and create a new dataset called final_data.csv which contains information regarding the top 20 societies. Finally, we scraped all the events hosted by the biggest societies in the facebook_events_scrape.py file which is then stored in the final_data_2.csv file. We can get further information about some events which is stored in final_data_3.csv.


## Data Science Task

The dataset we will be working with are final_data.csv, final_data_2.csv, and final_data_3.csv. final_data.csv contains information about the biggest 20 societies as a whole whilst final_data_2.csv scrapes as many events as possible from the societies. However, there are some fields missing from some events (e.g. location of event, time) and hence some events have much more information than others. Resultantly, the events that do contain more information are written into final_data_3.csv. Therefore, there are events which belong to both final_data_2.csv and final_data_3.csv whereby the extra information in final_data_2.csv are stored as a dictionary. Hence, the first task would most likely be joining these 2 datasets so that they are all in 1 file without any duplicates.

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
