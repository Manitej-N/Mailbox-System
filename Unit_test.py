import unittest
from MailboxAgent import *
from Mail import Mail
from Confidential import Confidential


class TestMailboxAgent(unittest.TestCase):

    def setUp(self):
        """Prepare a mailbox agent with sample emails."""
        self.mba = MailboxAgent([])

        # Create emails manually
        self.e1 = Mail("1", "a@gre.ac.uk", "b@gre.ac.uk", "2024/07/26", "Hi", "inbox", "Body one")
        self.e2 = Mail("2", "x@gre.ac.uk", "y@gre.ac.uk", "2025/08/19", "Update", "tag1", "Body two")
        self.e3 = Mail("3", "a@gre.ac.uk", "z@gre.ac.uk", "2025/06/25", "Meeting", "inbox", "Body three")
        self.e4 = Confidential("4", "bank@secure.com", "me@gre.ac.uk", "2023/03/15","Account", "conf", "Balance 11119")

        # Insert into mailbox
        self.mba._mailbox = [self.e1, self.e2, self.e3, self.e4]

    # FA.1 – get email
    def test_get_email_valid(self):
        result = self.mba.get_email("1")
        self.assertIsNotNone(result)
        self.assertEqual(result.m_id, "1")

    def test_get_email_invalid(self):
            result = self.mba.get_email("999")
            self.assertIsNone(result)

    # FA.3 – delete email
    def test_delete_email(self):
        self.mba.del_email("2")
        email = self.mba.get_email("2")
        self.assertEqual(email.tag, "bin")

    # FA.4 – filter
    def test_filter_sender(self):
        out = self.mba.filter("a@gre.ac.uk")
        self.assertEqual(len(out), 2)

    # FA.5 – confidential encryption
    def test_confidential_is_encrypted(self):
        # body should not match original plain text
        self.assertNotEqual(self.e4.body, "Top secret text")

    # FA.6 – add mail
    def test_add_general_mail(self):
        self.mba.add_email("h@gre.ac.uk", "i@gre.ac.uk", "2025/03/05","New", "tag1", "Test Body")
        last = self.mba._mailbox[-1]
        self.assertIsInstance(last, Mail)

    def test_add_confidential_mail(self):
        self.mba.add_email("p@gre.ac.uk", "q@gre.ac.uk", "2025/03/06","Hidden", "conf", "Some secret")
        last = self.mba._mailbox[-1]
        self.assertIsInstance(last, Confidential)
        self.assertNotEqual(last.body, "Some secret")  # encrypted

if __name__ == '__main__':
    unittest.main()

