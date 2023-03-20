import unittest
from freezegun import freeze_time
from mod3.correct_weekday import app

class TestCorrectWeekday(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    @freeze_time("2023-03-13")
    def test_can_get_correct_weekdate_tomorrow(self):
        username = "Matvey"
        greeting = "Хорошего понедельника!"
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(greeting in response_text)