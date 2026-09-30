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

    # Test mean when the vector contains negative values
    def test_mean_with_negative_values(self):
        v = Vec([-2, 0, 2, 4])

        self.assertEqual(v.mean(), 1)

    # Test mean of a single-element vector
    def test_mean_single_element(self):
        v = Vec([10])

        self.assertEqual(v.mean(), 10)

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

    # Test that demeaning does not change the number of elements
    def test_demean_length(self):
        v = Vec([2, 4, 6, 8])

        result = v.demean()

        self.assertEqual(len(result), len(v))

    # Test whether standard deviation is calculated correctly
    def test_std(self):
        v = Vec([2, 4, 6, 8])

        self.assertAlmostEqual(v.std(), 2.23607, places=5)

    # Test the property that standard deviation is zero when all values are equal
    def test_std_of_equal_values(self):
        v = Vec([5, 5, 5, 5])

        self.assertEqual(v.std(), 0)

    # Test standard deviation of a single-element vector
    def test_std_single_element(self):
        v = Vec([10])

        self.assertEqual(v.std(), 0)

    # Test standard deviation with negative and positive values
    def test_std_with_negative_values(self):
        v = Vec([-2, 0, 2])

        self.assertAlmostEqual(v.std(), 1.63299, places=5)


if __name__ == "__main__":
    unittest.main()