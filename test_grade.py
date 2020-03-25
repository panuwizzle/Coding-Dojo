import unittest
from grade import grade

class TestGrade(unittest.TestCase):

    def test_point_zero_got_F(self):
        self.assertEqual(grade(0), 'F')

    def test_point_60_got_F(self):
        self.assertEqual(grade(60), 'F')

    def test_point_61_got_D(self):
        self.assertEqual(grade(61), 'D')

    def test_point_70_got_D(self):
        self.assertEqual(grade(70), 'D')

    def test_point_71_got_C(self):
        self.assertEqual(grade(71), 'C')

    def test_point_80_got_C(self):
        self.assertEqual(grade(80), 'C')

    def test_point_90_got_B(self):
        self.assertEqual(grade(90), 'B')

    def test_point_91_got_A(self):
        self.assertEqual(grade(91), 'A')

    def test_point_100_got_A(self):
        self.assertEqual(grade(100), 'A')

    def test_point_85_got_B(self):
        self.assertEqual(grade(85), 'B')