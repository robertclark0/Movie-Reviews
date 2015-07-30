import webbrowser
import os
import re


# Styles and scripting for the page
with open(os.path.dirname(__file__) + "/../html/head.html", "r") as my_file:
    main_page_head = my_file.read()


# The main page layout and title bar
with open(os.path.dirname(__file__) + "/../html/doc.html", "r") as my_file:
    main_page_content = my_file.read()


# A single movie entry html template
with open(os.path.dirname(__file__) + "/../html/movie-content.html", "r") as my_file:
    movie_tile_content = my_file.read()


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    # output_file = open('fresh_tomatoes.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    # output_file.write(main_page_head + rendered_content)
    # output_file.close()

    # open the output file in the browser
    # url = os.path.abspath(output_file.name)
    # webbrowser.open('file://' + url, new=2) # open in a new tab, if possible

    # For use on web server, will return html content instead of opening a local file
    print(main_page_head + rendered_content)