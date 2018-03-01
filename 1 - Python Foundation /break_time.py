import webbrowser
import time

# timer to play a video for a study break after a duration of time
# Inputs - amount of breaks you want to take / duration of time before break

n = 0
breaks = 3 
print( "This program started at " + time.ctime())
while(n < breaks):
    time.sleep(5)
    print( "It is " + time.ctime() + " Time to take a break!\n")
    webbrowser.open("https://www.youtube.com/watch?v=dGFSjKuJfrI")
    n += 1
    