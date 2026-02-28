import unittest
from models import Account


class TestAccount(unittest.TestCase):

    def test_deposit(self):
        acc = Account("João", "12345678901")
        acc.deposit(100)
        self.assertEqual(acc.balance, 100)

    def test_withdraw(self):
        acc = Account("João", "12345678901", 200)
        acc.withdraw(50)
        self.assertEqual(acc.balance, 150)

    def test_transfer(self):
        acc1 = Account("João", "12345678901", 300)
        acc2 = Account("Maria", "10987654321", 100)
        acc1.transfer(acc2, 100)
        self.assertEqual(acc1.balance, 200)
        self.assertEqual(acc2.balance, 200)


if __name__ == "__main__":
    unittest.main()