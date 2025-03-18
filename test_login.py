import unittest
def login (username, password):
    valid_user= {"user@example.com":"password123"}
    return valid_user.get(username) == password
class TestLogin(unittest.TestCase):
    def test_valid_login(self):
        self.assertTrue(login("user@example.com", "password123"))
    def test_invalid_login(self):
        self.assertFalse(login("user@example.com", "wrongpassword"))
    if __name__ == "__main__":
        unittest.main()    