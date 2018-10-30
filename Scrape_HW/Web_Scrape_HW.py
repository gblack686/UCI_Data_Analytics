# coding UTF-8

from splinter import Browser
from bs4 import BeautifulSoup


def scrape():
	executable_path = {"executable_path": "/Users/gblac/Desktop/chromedriver"}
	browser = Browser("chrome",**executable_path, headless=False)

	final_scrape_data={}
	output = MarsArticle(browser)
	final_scrape_data['Mars_Article_Title'] = output[0]
	final_scrape_data['Mars_Article_Text'] = output[1]
	final_scrape_data['Featured_Image'] = FeaturedImage(browser)
	final_scrape_data['Mars_Stats'] = PandasHTML()
	final_scrape_data['Mars_Weather'] = TweepyMars()
	final_scrape_data['Mars_Hemispheres'] = MarsHemispheres(browser)

	return final_scrape_data



def MarsArticle(browser):
	# set URL
	newsurl = "https://mars.nasa.gov/news/"
	# visit browser in splinter
	browser.visit(newsurl)
	# retrieve html from browser
	html = browser.html
	# create soup
	soup = BeautifulSoup(newsurl,"html.parser")

	# retrieve items from soup
	article = soup.find("div",class_="list_text")
	articletext = "Placeholder_Text"
	articletitle = "Placeholder_Tilte"
	#articletext = soup.find("div",class_="article_teaser_body").text
	#articletitle = soup.find("div",class_="content_title").text

	# return items
	return [articletitle,articletext]

def FeaturedImage(browser):
	# set URL
	image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	# visit url with splinter
	browser.visit(image_url)
	# retrieve html
	html = browser.html
	# create soup
	soup = BeautifulSoup(html,"html.parser")

	# retrieve items
	img = soup.find("img",class_="thumb")['src']
	# add image endpoint to base URL
	featured_image_url = "https://www.jpl.nasa.gov/" + img
	return featured_image_url


def PandasHTML():
	# import Pandas
	import pandas as pd
	# set URL
	pandas_url = "https://space-facts.com/mars/"
	# read data table with pandas
	mars_data = pd.read_html(pandas_url)
	# convert table to DataFrame object
	mars_data = pd.DataFrame(mars_data[0])
	# convert DataFrame to html 
	mars_facts = mars_data.to_html(header=False,index=False)


def TweepyMars():
	# import tweepy and keys
	import tweepy
	from API_Config_Keys import Twitter_Consumer_API, Twitter_Consumer_API_Secret, Twitter_Access_Token, Twitter_Access_Token_Secret
	# initialize Tweepy
	auth = tweepy.OAuthHandler(Twitter_Consumer_API, Twitter_Consumer_API_Secret)
	auth.set_access_token(Twitter_Access_Token, Twitter_Access_Token_Secret)
	api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

	# set username
	target_user = "MarsWxReport"
	# find tweet
	tweet = api.user_timeline(target_user, count =1)
	# retrieve tweet text
	marsweather = tweet[0]['text']
	return marsweather

def MarsHemispheres(browser):
	# set URL
	hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
	# initialize splinter
	browser.visit(hemispheres_url)
	# set html
	html = browser.html
	# create soup
	soup = BeautifulSoup(html, "html.parser")

	# create list to append items
	hemisphere_image_urls = []
	# find results
	#results = soup.find("div",class_="result_list")
	# find hemisphere items
	hemisphere_items = soup.find_all("div",class_="item")

	# loop through the hemisphere items
	for x in hemisphere_items:
		# retrieve title, replace the word 'Enhanced'
	    title = x.find("h3").text
	    title = title.replace("Enhanced","")
	    # retrieve image endpoint
	    endpoint_image_link = x.find("a")['href']
	    image_link = "https://astrogeology.usgs.gov/" + endpoint_image_link
	    # visit with splinter
	    browser.visit(image_link)
	    # set HTML
	    html = browser.html
	    # create soup
	    soup = BeautifulSoup(html,"html.parser")
	    # find the download links
	    soup_downloads = soup.find("div",class_="downloads")
	    # find the links
	    image_url = soup_downloads.find("a")['href']
	    # append titles and links to dictionary
	    hemisphere_image_urls.append({"Title":title,"Image":image_url})
	return hemisphere_image_urls
















	# 









