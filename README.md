# USYD-Societies-Events
This project seeks to scrape Facebook data regarding events from the top 10 biggest societies at USYD. From that, we then seek to analyse what are the factors that drive event attendance.

Amazing links:
http://minimaxir.com/2015/07/facebook-scraper/

This project seeks to scrape Facebook data regarding events from the top 20 biggest societies at USYD. From that, we then seek to analyse what are the factors that drive event attendance. Here, we seek to deploy models to analyse the casual relationships between event attendance and such factors such as the location of the event, timing during the semester and day, whether catering was provided, and more.

## Requirements

All packages used are in the requirements.txt file.

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
