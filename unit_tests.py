import unittest
import datetime

from src.College_Football_Scoreboard.methods import get_games_on_date
from src.College_Football_Scoreboard.models import Game

class test_get_games_on_date(unittest.TestCase):

    @unittest.expectedFailure
    def test_get_games_on_date_not_date(self):
        s = "string"
        get_games_on_date(s)

    @unittest.expectedFailure
    def test_get_games_on_date_bad_year(self):
        badDate = datetime.date(1999, 9, 15)
        get_games_on_date(badDate)


    def test_get_games_on_date_2022_national_championship(self):
        national_championship = datetime.date(2022, 1, 10)
        result = get_games_on_date(national_championship)
        expectedGame = Game(datetime.date(2022, 1, 10), True, False, None, True, "Georgia", "Alabama", 33, 18)
        self.assertEqual(expectedGame, result[0])


    # def test_get_games_on_date_2021_12_27(self):
    #     date = datetime.date(2021, 12, 27)
    #     result = get_games_on_date(date)