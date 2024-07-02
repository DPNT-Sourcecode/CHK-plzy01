from lib.solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        cases = (
            ("AAABBCD", 130 + 45 + 20 + 15),
            ("BAAAACCD", 30 + 130 + 50 + 40 + 15)
        )

        for skus, expected_total in cases:
            assert checkout_solution.checkout(skus) == expected_total
    
    def test_illegal_input(self):
        skus = "ABZD"
        assert checkout_solution.checkout(skus) == -1
