from lib.solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        skus = "AAABBCD"
        expected_total = 130 + 45 + 20 + 15

        assert checkout_solution.checkout(skus) == expected_total
    
    def test_illegal_input(self):
        skus = "ABZD"
        assert checkout_solution.checkout(skus) == -1