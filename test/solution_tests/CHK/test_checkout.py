from lib.solutions.CHK import checkout_solution
import pytest

class TestCheckout():
    
    @pytest.mark.parametrize(
        "skus,expected_total",
        (
            # ("AAABBCD", 130 + 45 + 20 + 15),
            # ("BAAAACCD", 30 + 130 + 50 + 40 + 15),
            ("ABCDE", 50 + 30 + 20 + 15 + 40),
            ("AAABACAA", 200 + 50 + 30 + 20),
            ("A" * 9 + "BBBEE", 380 + 45 + 40 + 40),
            ("EEB", 80),
            ("EEEB", 120),
            ("EEEEBB", 160),
            ("FF", 20),
            ("FFF", 20),
            ("FFFF", 30),
            ("FFFFF", 40),
            ("FFFFFF", 40),
            ("G", 20),
            ("H", 10),
            ("H" * 5, 45),
            ("H" * 10, 80),
            ("H" * 16, 80 + 45 + 10),
            ("I", 35),
            ("J", 60),
            ("K", 80),
            ("KK", 150),
            ("L", 90),
            ("M", 15),
            ("N", 40),
            ("NNNM", 120),
            ("O", 10),
            ("P", 50),
            ("P" * 5, 200),
            
        )
    )
    def test_checkout(self, skus, expected_total):
        assert checkout_solution.checkout(skus) == expected_total

    @pytest.mark.parametrize("skus", ("ABZD", "", 1, True))
    def test_illegal_input(self, skus):
        assert checkout_solution.checkout(skus) == -1

