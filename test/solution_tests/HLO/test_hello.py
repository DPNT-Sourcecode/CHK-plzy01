from lib.solutions.HLO import hello_solution

class TestHello():
    def test_sum(self):
        name = "Jeff"
        assert hello_solution.hello(name) == name


