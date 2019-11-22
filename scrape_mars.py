#scrape the Mars sites 

from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import datetime as dt
import pymongo

# Set Executable Path & Initialize Chrome Browser
executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

# Create Mission to Mars global dictionary that can be imported into Mongo
mars_info = {}

def scrape_news():
    try:
        news_url = "https://mars.nasa.gov/news/"
        browser.visit(news_url)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")

        #find text for title and teaser
        article =soup.find_all("div", class_="list_text")
        #print(len(article))
        #print(article)

        #find title and teaser
        news_title = soup.article("div", class_="content_title")
        news_p = soup.article("div", class_ ="article_teaser_body")  
        
        # Dictionary entry from MARS NEWS
        mars_info['news_title'] = news_title
        mars_info['news_paragraph'] = news_p
    
        return mars_info
    
    finally:
        browser.quit()
#print("---first")
# JPL Images scraping 
# def scrape_pics():
#     try:
#         executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
#         browser = Browser("chrome", **executable_path)
#         jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
#         browser.visit(jpl_url)

#         # Ask Splinter to Go to Site and Click Button with Class Name full_image
#         # <button class="full_image">Full Image</button>
#         full_image_button = browser.find_by_id("full_image")
#         full_image_button.click()

#         # Find "More Info" Button and Click It
#         browser.is_element_present_by_text("more info", wait_time=1)
#         more_info_element = browser.find_link_by_partial_text("more info")
#         more_info_element.click()

#         # Parse Results HTML with BeautifulSoup
#         html = browser.html
#         image_soup = BeautifulSoup(html, "html.parser")
#         img_url = image_soup.select_one("figure.lede a img").get("src")
#         #img_url

#         # Use Base URL to Create Absolute URL
#         img_url = f"https://www.jpl.nasa.gov{img_url}"
#         #print(img_url)

#         # Dictionary entry from FEATURED IMAGE
#         mars_info['featured_image_url'] = img_url 
        
#         return mars_info
    
#     finally:
#         browser.quit()
# print("----second")
# def scrape_weather():
#     try:

#         # Visit the Mars Weather Twitter Account
#         executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
#         browser = Browser("chrome", **executable_path, headless=False)
#         url = "https://twitter.com/marswxreport?lang=en"
#         browser.visit(url)

#         # Parse Results HTML with BeautifulSoup
#         html = browser.html
#         weather_soup = BeautifulSoup(html, "html.parser")

#         # Find a Tweet with the data-name `Mars Weather`
#         mars_weather_tweet = weather_soup.find("div", 
#                                        attrs={
#                                            "class": "tweet", 
#                                             "data-name": "Mars Weather"
#                                         })

#         # Search Within Tweet for <p> Tag Containing Tweet Text
#         mars_weather = mars_weather_tweet.find("p", "tweet-text").get_text()
#         #print(mars_weather)

#         # Dictionary entry from WEATHER TWEET
#         mars_info['weather_tweet'] = mars_weather
        
#         return mars_info
#     finally:

#         browser.quit()
# print("---thrid")
# def scrape_facts():
#     # Visit the Mars Facts Site Using Pandas to Read
#         mars_df = pd.read_html("https://space-facts.com/mars/")[0]
#         #print(mars_df)
#         mars_df.columns=["Description", "Value"]
#         mars_df.set_index("Description", inplace=True)
#         #mars_df

#         # Save html code to folder Assets
#         data = mars_df.to_html()

#         # Dictionary entry from MARS FACTS
#         mars_info['mars_facts'] = data

#         return mars_info

# print("--fourth")
# def scarpe_hemis():
#     try:
#         # Visit the USGS Astrogeology Science Center Site
#         executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
#         browser = Browser("chrome", **executable_path, headless=False)
#         url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
#         browser.visit(url)

#         hemisphere_image_urls = []

#         # Get a List of All the Hemispheres
#         links = browser.find_by_css("a.product-item h3")
#         for item in range(len(links)):
#             hemisphere = {}
    
#                 # Find Element on Each Loop to Avoid a Stale Element Exception
#             browser.find_by_css("a.product-item h3")[item].click()
                
#             # Find Sample Image Anchor Tag & Extract <href>
#             sample_element = browser.find_link_by_text("Sample").first
#             hemisphere["img_url"] = sample_element["href"]
            
#             # Get Hemisphere Title
#             hemisphere["title"] = browser.find_by_css("h2.title").text
            
#             # Append Hemisphere Object to List
#             hemisphere_image_urls.append(hemisphere)
            
#             # Navigate Backwards
#             browser.back()

#         mars_info['urls'] = hemisphere_image_urls

        
#         # Return mars_data dictionary 

#         return mars_info
#     finally:

#         browser.quit()

scrape_news()
print(mars_info)
#Add data to Mongo DB 

# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)

# db = client.mars_data
# collection = db.mars_info
# collection.insert_many(mars_info)
