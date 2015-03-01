import unittest
import flask
import photolog
from photolog import app


class MyTests(unittest.TestCase):

    def test_check_if_running(self):
        with app.test_request_context("/"):
            result = photolog.index()
            self.assertIn("Bem-vindo", result)

    def test_if_result_is_html(self):
        with app.test_request_context("/"):
            result = photolog.index()
            first_line = result.split("\n")[0]
            self.assertIn("html", first_line.lower())

if __name__ == '__main__':
    unittest.main()
