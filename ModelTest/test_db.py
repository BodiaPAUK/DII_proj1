import unittest
import dataBase.db_access as db_access

class TestDatabase(unittest.TestCase):

    def test_save_and_get_user(self):
        db_access.save_user("test_user", "test_login", "test_password")
        user = db_access.get_user_by_login("test_login")
        self.assertIsNotNone(user)
        self.assertEqual(user[1], "test_user")
        self.assertEqual(user[2], "test_password")

    def test_save_and_get_user_result(self):
        db_access.save_user_result(1, 20, 40, 30, 100, "Good")
        results = db_access.get_user_results(1)
        self.assertTrue(len(results) > 0)

if __name__ == '__main__':
    unittest.main()
