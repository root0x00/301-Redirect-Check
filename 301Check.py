import requests

# List of URLs > Import the URL's you'd like to check in the array below.
urls = []

def check_redirects(url_list):
    with open("broken_urls.txt", "w") as file:  # Open file to write broken urls
        for url in url_list:
            try:
                response = requests.get(url, allow_redirects=True)
                # Check if redirect
                if response.history:
                    print(f"{url} was redirected to {response.url}")
                else:
                    print(f"{url} was not redirected")
            except requests.RequestException as e:
                print(f"Error with URL {url}: {e}")
                file.write(f"Error with URL {url}: {e}\n")  # Write broken url to txt

check_redirects(urls)
