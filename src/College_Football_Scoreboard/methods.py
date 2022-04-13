import datetime
from bs4 import BeautifulSoup
import requests


def get_games_on_date(date):
    if type(date) is not datetime.date:
        raise Exception("Data provided must be datetime.date")
    result = []
    season_divisions = get_season_divisions_number(date)
    game_date_url = date_number_add_leading_zero_to_string(date.month)+"%2F"+date_number_add_leading_zero_to_string(date.day)+"%2F"+str(date.year)
    hdr = {'User-Agent': 'Mozilla/5.0'}
    url = "https://stats.ncaa.org/season_divisions/"+season_divisions+"/scoreboards?utf8=✓&season_division_id=&game_date="+game_date_url
    r = requests.get(url, headers=hdr)
    soup = BeautifulSoup(r.content, features="html.parser")
    games_tbody = soup.find("table").find("tbody")
    games_tr = games_tbody.find_all("tr")

    for tr_g in games_tr:
        clean_game_tr(tr_g)

    #print(games_tr)

    return result

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

def date_number_add_leading_zero_to_string(num):
    if num < 10:
        return "0"+str(num)
    else:
        return str(num)

def clean_game_tr(tr_g):
    #print(tr_g)
    teams = tr_g.find_all("a", {"target": "TEAMS_WIN"})
    print(teams)
