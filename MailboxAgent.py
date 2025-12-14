#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            MailboxAgent Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Author:                                                                                   ###
###            <Manitej Narayanadasu>, SID<001448592>                                         ###                                           ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *
from Confidential import *
from Personal import *

class MailboxAgent:
    """<This is the documentation for MailboxAgent. Complete the docstring for this class."""
    def __init__(self, email_data):                       # DO NOT CHANGE
        self._mailbox = self.__gen_mailbox(email_data)    # data structure containing Mail objects DO NOT CHANGE

    # Given email_data (string containing each email on a separate line),
    # __gen_mailbox returns mailbox as a list containing received emails as Mail objects
    @classmethod
    def __gen_mailbox(cls, email_data):                   # DO NOT CHANGE
        """ generates mailbox data structure
            :ivar: String
            :rtype: list  """
        mailbox = []
        for e in email_data:
            msg = e.split('\n')
            mailbox.append(
                Mail(msg[0].split(":")[1], msg[1].split(":")[1], msg[2].split(":")[1], msg[3].split(":")[1],
                     msg[4].split(":")[1], msg[5].split(":")[1], msg[6].split(":")[1]))
        return mailbox

# FEATURES A (Partner A)
    # FA.1
    # Through this method, we can access the mails which we require using the specific mail id
    def get_email(self, m_id):
        """
        -the method 'get_email' uses m_id to gather all the mails we require.
        -This method uses for loop to select the required mails from _mailbox.
        -It uses if conditional statement to match the entered email id and the email id present in _mailbox.
        - if there is no mail id which is matching, it prints "match not found".
             """
        for emails in self._mailbox:
            if emails.m_id == m_id:
                print("match found!")
                return emails
        print("no match found!")
        return None


    # FA.3
    # Using this method, we can delete the mails which we do not require using its mail id(m_id)
    def del_email(self, m_id):
        """
        -The method 'del_email' uses m_id to move the mentioned mail into bin.
        -This method uses if conditional statement to find the mentioned mail and move it to the bin.
        - if the entered mail id doesn't exist it prints "no mail found" and returns to mail
        """
        mail = self.get_email(m_id)
        if mail is None:
            print("no match found!")
            return None
        mail.tag = "bin"
        return mail



    # FA.4
    #This method helps us to look at all the mails we need from a specific user.
    def filter(self, frm):
        """
        - Firstly, this method needs an empty list to sort all the required mails into one list, which is 'output = []' here.
        - this method selects the mails using email addresses we received from.
        - this method uses for loop to select the required mails from _mailbox.
        - it uses if conditional statement to find the mentioned mail and move it to the list we created.
        """
        output = []
        for sort in self._mailbox:
            if sort.frm == frm:
                output.append(sort)

        return output

    # FA.5
    #Through this method, we can sort/arrange all the mails by the time they have been received
    def sort_date(self):
        """
        -This method is used to sort all the mails according to the date it was received on.
        -We use *nested functions* here to pick the date it was received from emails.
        -later, the emails get sorted according to the date it was received from emails.
        """

        def pick_date(email_item):
            # return date string directly; your format parser will work
            return email_item.date

        outcome = sorted(self._mailbox, key=pick_date, reverse=True)
        self._mailbox = outcome
        return outcome




# FEATURES B (Partner B)
    # FB.1
    # 
    def show_emails(self):
        """Pretty-print all emails in the mailbox using the Mail class attribute names."""
        print("\n--- Mailbox ---")
        for mail in self._mailbox:
            # Use _frm instead of _from (as per your error)
            frm = getattr(mail, "_frm", None)
            to = getattr(mail, "_to", None)
            date = getattr(mail, "_date", None)
            subject = getattr(mail, "_subject", None)
            tag = getattr(mail, "_tag", None)
            m_id = getattr(mail, "_m_id", None)
            body = getattr(mail, "_body", "")

            print(f"ID:{m_id} | From:{frm} -> To:{to} | Date:{date} | Subject:{subject} | Tag:{tag}")
            print(f"Body:{body}")
            print(f"Read:{getattr(mail, '_read', False)} | Flagged:{getattr(mail, '_flagged', False)}")
            print("-" * 40)

    # FB.2
    # 
    def mv_email(self, m_id, tag):
        """Move an email to a different folder (tag)."""
        for mail in self._mailbox:
            if mail._m_id == m_id:
                mail._tag = tag
                print(f"Email {m_id} moved to {tag}")
                return
        print(f"Email {m_id} not found")

    # FB.3
    # 
    def mark(self, m_id, m_type):
        """Mark an email as 'read' or 'flagged'."""
        for mail in self._mailbox:
            if mail._m_id == m_id:
                if m_type == "read":
                    mail._read = True
                elif m_type == "flagged":
                    mail._flagged = True
                else:
                    print("Invalid type. Use 'read' or 'flagged'.")
                    return
                print(f"Email {m_id} marked as {m_type.upper()}.")
                return
        print(f"Email {m_id} not found.")

    # FB.4
    # 
    def find(self, date):
        """Find and display emails received on a specific date (dd/mm/yyyy)."""
        outcomes = []
        for emails in self._mailbox:
            if emails.date == date:
                outcomes.append(emails)

        return outcomes

    # FB.5
    # 
    def sort_from(self):
        """  """
        """
        Return the sender field so Personal emails can be sorted by the 'from' value.
        """
        return self.sort_from


# FEATURE 6 (Partners A and B)
    # This method is used to add new emails.
    def add_email(self, frm, to, date, subject, tag, body):
        """
        - Add a new email to the mailbox.
        - Generates a unique m_id
        - Creates Confidential, Personal, or general Mail based on tag
        - Appends the object to self._mailbox
        - Returns the new m_id
        - Exact Format to be entered: add <from> <to> <date> <subject> <tag> %%<body>

        """
        # code must generate unique m_id
        new_m_id = str(len(self._mailbox)+1)
        match tag.lower():
            # FA.6
            case 'conf':     # executed when tag is 'conf'
                conf_mail=Confidential(new_m_id, frm, to, date,subject,tag, body)
                self._mailbox.append(conf_mail)
                return conf_mail
            # FB.6
            case 'prsnl':    # executed when tag is 'prsnl'
                personal_mail=Personal(new_m_id,frm, to, date, subject,tag, body)
                self._mailbox.append(personal_mail)
                return personal_mail
            # FA&B.6
            case _:          # executed when tag is neither 'conf' nor 'prsnl'
                reg_mail = Mail(new_m_id,frm, to, date, subject, tag, body)
                self._mailbox.append(reg_mail)
                return reg_mail


if __name__=="__main__":

    # test mailbox with all required fields to test sort_from() i.e F.A.5
    test = MailboxAgent([])  # create empty agent
    test._mailbox = [
        Mail(m_id=1, frm="xylo@gre.ac.uk", to="apple@gre.ac.uk", date="25/11/2026", subject="Subject A", tag="tag1",
             body="Body A"),
        Mail(m_id=2, frm="yatch@example.com", to="blink@example.com", date="08/11/2019", subject="Subject B", tag="tag2",
             body="Body B"),
        Mail(m_id=3, frm="zebra@example.com", to="cyan@example.com", date="24/12/2025", subject="Subject C", tag="tag3",
             body="Body C")
    ]

    sorted_emails = test.sort_date()

    print("Sorted Mailbox:")
    for mail in sorted_emails:
        print(f"{mail.to} <- {mail.date}")
