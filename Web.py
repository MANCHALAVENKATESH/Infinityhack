import random
import time
import webbrowser
while True:
    sites = random.choice(['youtube.com','instagram.com'])
    visits = 'https://'.format(sites)
    webbrowser.open(visits)
    time.sleep(10)
