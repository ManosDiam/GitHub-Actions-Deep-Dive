import unittest
from web_crawler import count_links


class TestWebCrawler(unittest.TestCase):
    def test_count_links(self):
        url = "https://www.example.com"
        result = count_links(url)
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)


if __name__ == "__main__":
    unittest.main()
