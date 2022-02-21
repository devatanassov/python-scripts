import unittest
from generate_playlist import generate_playlist_by_path 

class TestCreatePlaylistScript(unittest.TestCase):

    def test_not_dir(self):
        self.assertFalse(generate_playlist_by_path('asd'), "Should return false if no dir is passed.")

if __name__ == '__main__':
    unittest.main()