import xml.etree.ElementTree as ET

# create movies list
movies = []

# parse movies.xml and find root element
tree = ET.parse('xml/movies.xml')
root = tree.getroot()

# iterate through each child element, create instance of Movie object with parsed data
for child in root:
    title = child.find('title').text
    description = child.find('description').text
    img_url = child.find('img_url').text
    trailer_url = child.find('trailer_url').text
    movies.append()