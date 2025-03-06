import unittest
from  movie_rating import *

class textMoiveRating(unittest.TestCase):
    def test_add_movie(self):
        result = get_add_movie()
        self.assertEqual(result, 'Inception')

    def test_rating_moive(self):
        result = get_rating_movie()
        self.assertEqual(result, 2.0)
        
    
    

if __name__== "__main__":
    unittest.main()
