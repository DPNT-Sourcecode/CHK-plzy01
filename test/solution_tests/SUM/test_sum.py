from lib.solutions.SUM import sum_solution
import pytest

class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_min(self):
        for values in ((-10, 1), (1, -10)):
            with pytest.raises(ValueError):
                sum_solution.compute(*values)


