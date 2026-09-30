import unittest
from vec import Vec


class TestVector(unittest.TestCase):

    # Test whether mean is calculated correctly
    def test_mean(self):
        v = Vec([2, 4, 6, 8])

        self.assertEqual(v.mean(), 5)

    # Test the property that the mean of equal values is the same value
    def test_mean_of_equal_values(self):
        v = Vec([5, 5, 5, 5])

        self.assertEqual(v.mean(), 5)

    # Test whether demean() correctly subtracts the mean from each element
    def test_demean(self):
        v = Vec([2, 4, 6, 8])

        result = v.demean()

        self.assertEqual(result.elements, [-3, -1, 1, 3])

    # Test the property that the mean of a de-meaned vector is zero
    def test_demean_mean_is_zero(self):
        v = Vec([2, 4, 6, 8])

        result = v.demean()

        self.assertAlmostEqual(result.mean(), 0)

    # Test whether standard deviation is calculated correctly
    def test_std(self):
        v = Vec([2, 4, 6, 8])

        self.assertAlmostEqual(v.std(), 2.23607, places=5)

    # Test the property that standard deviation is zero when all values are equal
    def test_std_of_equal_values(self):
        v = Vec([5, 5, 5, 5])

        self.assertEqual(v.std(), 0)


if __name__ == "__main__":
    unittest.main()