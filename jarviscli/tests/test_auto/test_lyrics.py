import unittest
import os
from mock import call, patch
from packages.lyrics import lyrics

#TODO: add tests for PyLyricsClone
class Lyrics_Test(unittest.TestCase):

    def setUp(self):
        self.song_name = "everybody dies"
        self.artist_name = "ayreon"
        self.complete_info = "everybody dies-ayreon"
        self.wrong_info = "everybody dies-arebon"

    def test_lyrics_found_given_full_parameters(self):
        self.assertIsNotNone(lyrics.find(self.complete_info))

    def test_lyrics_not_found_given_incomplete_parameter(self):
        self.assertEqual(lyrics.find(self.song_name), ["you forgot to add either song name or artist name"])

    def test_lyrics_not_found_given_wrong_parameter(self):
        self.assertIsNone(lyrics.find(self.wrong_info))

    def test_split_works(self):
        self.assertEqual(lyrics.parse(self.complete_info), ["everybody dies", "ayreon"])
