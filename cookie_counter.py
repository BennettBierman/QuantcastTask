import csv


class CookieCounter:

    def __init__(self, file):
        self.date_log = dict()
        DATE_LENGTH = 10
        with open(file, newline='') as csvfile:
            read = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for input in read:
                pivot = input[0].index(',')
                cookie = input[0][:pivot]
                date = input[0][pivot + 1:][:DATE_LENGTH]
                if date in self.date_log:
                    self.date_log[date].append(cookie)
                else:
                    self.date_log[date] = [cookie]

    def most_freq_cookies(self, date):
        cookies = self.date_log[date]
        cookie_log = dict()
        for cookie in cookies:
            if cookie in cookie_log:
                cookie_log[cookie] += 1
            else:
                cookie_log[cookie] = 1
        freq = max(cookie_log.values())
        return [key for key in cookie_log if cookie_log[key] == freq]