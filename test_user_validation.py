import unittest
from User_Registration_Problem import UserValidator

class TestUserValidation(unittest.TestCase):
    def test_valid_email(self):
        valid_emails = [
            "user@example.com",
            "test.user@gamil.com"
        ]
        for email in valid_emails:
            self.assertTrue(UserValidator.is_valid_email(email))
    def test_invalid_emails(self):
        invalid_emails = [
            "userexample.com",
            "user@.com"
        ]
        for email in invalid_emails:
            self.assertFalse(UserValidator.is_valid_email(email))
    def test_valid_passwords(self):
        valid_passwords = [
            "Abc@1234",
            "Pass@123"
        ]
        for password in valid_passwords:
            self.assertTrue(UserValidator.is_valid_password(password))
    def test_invalid_passwords(self):
            invalid_passwords = [
                "abc123",
                "ABC@1234"
            ]
            for password in invalid_passwords:
                self.assertFalse(UserValidator.is_valid_password(password))
    if __name__ == "__main__":
        unittest.main()
