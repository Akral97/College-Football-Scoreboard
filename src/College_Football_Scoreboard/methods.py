import datetime
from bs4 import BeautifulSoup
import requests

def get_games_on_date(date):
    if type(date) is not datetime.date:
        raise Exception("Data provided must be datetime.date")
    season_divisions = get_season_divisions_number(date)


def get_season_divisions_number(date):
    if datetime.date(2021, 7, 15) < date < datetime.date(2022, 7, 15):
        return "17721"
    elif datetime.date(2020, 7, 15) < date < datetime.date(2021, 7, 15):
        return "17180"
    elif datetime.date(2019, 7, 15) < date < datetime.date(2020, 7, 15):
        return "16920"
    elif datetime.date(2018, 7, 15) < date < datetime.date(2019, 7, 15):
        return "16680"
    elif datetime.date(2017, 7, 15) < date < datetime.date(2018, 7, 15):
        return "13542"
    elif datetime.date(2016, 7, 15) < date < datetime.date(2017, 7, 15):
        return "13040"
    elif datetime.date(2015, 7, 15) < date < datetime.date(2016, 7, 15):
        return "12580"
    elif datetime.date(2014, 7, 15) < date < datetime.date(2015, 7, 15):
        return "12301"
    elif datetime.date(2013, 7, 15) < date < datetime.date(2014, 7, 15):
        return "11420"
    elif datetime.date(2012, 7, 15) < date < datetime.date(2013, 7, 15):
        return "13354"
    elif datetime.date(2011, 7, 15) < date < datetime.date(2012, 7, 15):
        return "11300"
    elif datetime.date(2009, 7, 15) < date < datetime.date(2010, 7, 15):
        return "15972"
    elif datetime.date(2008, 7, 15) < date < datetime.date(2009, 7, 15):
        return "14652"
    elif datetime.date(2007, 7, 15) < date < datetime.date(2008, 7, 15):
        return "15968"

    raise Exception("Year is not supported")
