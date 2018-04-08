
def read_text():
    quotes = open("/Users/paulasyn/Desktop/Udacity-Fullstack-WebDev/1 - Python Foundation /profanity_alert/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()


read_text()