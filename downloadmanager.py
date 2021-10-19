import argparse
import requests


# Creates the parser and returns it
def get_args():
    # Creates the parser
    parser = argparse.ArgumentParser(prog="imagetoascii", description="Converts an image to ASCII art.")
    # Define the arguments.
    parser.add_argument("name", metavar="name", type=str, help="The name of the file downloaded.")
    parser.add_argument("url", metavar="url", type=str, help="The url to the file you want downloaded.")
    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    args = get_args()
    url: str = args.url
    filename: str = args.name

    request = requests.get(url, allow_redirects=True, stream=True)
    open(filename, 'wb').write(request.content)
