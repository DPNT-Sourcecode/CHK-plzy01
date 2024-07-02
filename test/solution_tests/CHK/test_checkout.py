from lib.solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        SKUs = "AAABBCD"
        expected_total = 130 + 45 + 20 + 15

        assert checkout_solution.checkout(SKUs) == expected_total
