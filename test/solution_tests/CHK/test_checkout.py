from lib.solutions.CHK import checkout_solution
import pytest

class TestCheckout():
    # TODO: This should test the system rather than individual pricing and offers
    @pytest.mark.parametrize(
        "skus,expected_total",
        (
            ("AAABBCD", 130 + 45 + 20 + 15),
            ("BAAAACCD", 30 + 130 + 50 + 40 + 15),
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
            ("K", 70),
            ("KK", 120),
            ("L", 90),
            ("M", 15),
            ("N", 40),
            ("NNNM", 120),
            ("O", 10),
            ("P", 50),
            ("P" * 5, 200),
            ("Q", 30),
            ("Q" * 3, 80),
            ("R", 50),
            ("RRRQ", 150),
            ("S", 20),
            ("T", 20),
            ("U", 40),
            ("UUUU", 120),
            ("V", 50),
            ("VV", 90),
            ("VVV", 130),
            ("W", 20),
            ("X", 17),
            ("Y", 10),
            ("Z", 21),
            ("STX", 45),
            ("TXY", 45),
            ("XYZ", 45),
            ("YZS", 45),
            ("ZST", 45),
            ("ZXS", 45),
            ("ZXSSS", 45 + 20 + 17),

        )
    )
    def test_checkout(self, skus, expected_total):
        assert checkout_solution.checkout(skus) == expected_total

    @pytest.mark.parametrize("skus", ("ABZD", 1, True))
    def test_illegal_input(self, skus):
        assert checkout_solution.checkout(skus) == -1


