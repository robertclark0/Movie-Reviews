#!/usr/bin/python
#print "Content-type: text/html\n\n";

import os
os.chdir(os.path.dirname(__file__) + '/..') #FOR LOCAL USE
import media
import content
import xml.etree.ElementTree as ET


# create movies list
movies = []

# parse movies.xml and find root element
tree = ET.parse('xml/movies.xml')
root = tree.getroot()

# iterate through each child element, create instance of Movie object with parsed data
for child in root:
    title = child.find('title').text
    review = child.find('review').text
    img_url = child.find('img_url').text
    trailer_url = child.find('trailer_url').text
    rating = child.find('rating').text
    movies.append(media.Movie(title, review, img_url, trailer_url,rating))

content.open_movies_page(movies)