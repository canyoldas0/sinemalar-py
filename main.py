import requests
from bs4 import BeautifulSoup

# Replace 'url' with the URL of the website you want to scrape
url = "https://www.paribucineverse.com/vizyondakiler"
# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find elements based on HTML tags, classes, or IDs
    # For example, let's find all the <a> tags (links) in the webpage
    links = soup.find_all("a")
    specific_div = soup.find("div", id="movieListRow")

    if specific_div:
        # Get the contents inside the <div> (can be tags, strings, etc.)

        movie_divs = specific_div.find_all("div", {"data-movie-title": True})

        for movie_div in movie_divs:
            # Extract the value of the 'movie-name' attribute
            movie_name = movie_div.get("data-movie-title")

            movie_info = movie_div.find("div", class_="movie-info")

            movie_time = movie_info.find("p", class_="movie-time mb-0")
            movie_type = movie_info.find("p", class_="movie-type mb-0")

            print(movie_time.text)
            print(movie_type.text)
            print(movie_name)

        # Print the contents of the <div>
        # for content in div_contents:
        #     print(content)
else:
    print("Failed to fetch the web page")
