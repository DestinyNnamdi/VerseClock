import time
import pyttsx3

# Initialize the text to speech engine
engine = pyttsx3.init()

while True:
    # Get the current time
    localtime = time.localtime()
    hour = localtime.tm_hour
    minute = localtime.tm_min

    # Check if it is top of the hour.
    if minute == 0:
        engine.say(f"The time is {hour} o'clock")
        engine.runAndWait()
    # Wait for 60 seconds before checking the time again.
    time.sleep(60)
    