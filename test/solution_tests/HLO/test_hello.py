from lib.solutions.HLO import hello_solution

class TestHello():
    def test_hello(self):
        name = "Jeff"
        assert hello_solution.hello(name) == f"Hello World!"



