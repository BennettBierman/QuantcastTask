from cookie_counter import CookieCounter
import sys


file = sys.argv[1]
date = sys.argv[3]
counter = CookieCounter(file)
for cookie in counter.most_freq_cookies(date):
    print(cookie)