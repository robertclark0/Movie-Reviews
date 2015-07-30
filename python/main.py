import python.media as media
import python.content as content
import xml.etree.ElementTree as ET

print('hello world')
# create movies list
movies = []

# parse movies.xml and find root element
tree = ET.parse('movies.xml')
root = tree.getroot()

# iterate through each child element, create instance of Movie object with parsed data
for child in root:
    title = child.find('title').text
    description = child.find('description').text
    img_url = child.find('img_url').text
    trailer_url = child.find('trailer_url').text
    movies.append(media.Movie(title, description, img_url, trailer_url))
    print(title)

content.open_movies_page(movies)