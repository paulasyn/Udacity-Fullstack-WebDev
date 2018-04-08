# detect profanity in text
import urllib.request

def read_text():
    quotes = open("/Users/paulasyn/Desktop/Udacity-Fullstack-WebDev/1 - Python Foundation /profanity_alert/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.request.urlretrieve("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_text()

