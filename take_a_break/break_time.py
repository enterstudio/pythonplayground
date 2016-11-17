import webbrowser
import time

total_breaks = 3
break_count = 0
play_count = 0

while break_count < total_breaks:
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    break_count = break_count+1
    play_count = play_count + 1
    print "The current time is " \
          + time.ctime() \
          + " and the play count is " \
          + str(play_count)

