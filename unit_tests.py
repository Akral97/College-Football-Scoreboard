import unittest
import datetime

from src.College_Football_Scoreboard.methods import get_games_on_date

class test_get_games_on_date(unittest.TestCase):

    @unittest.expectedFailure
    def test_get_games_on_date_not_date(self):
        s = "string"
        get_games_on_date(s)

    @unittest.expectedFailure
    def test_get_games_on_date_bad_year(self):
        badDate = datetime.date(1999, 9, 15)
        get_games_on_date(badDate)
