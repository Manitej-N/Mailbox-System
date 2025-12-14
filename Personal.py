#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Personal Class                                                                 ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Author:                                                                                   ###
###            <Manitej Narayanadasu>, SID<001448592>                                         ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES/SIGNATURES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *

# FB.5.a
class Personal(Mail):
    """Personal mail that adds simple text statistics to the message body."""
    # DO NOT CHANGE CLASS NAME OR METHOD NAMES/SIGNATURES
    # Add new method(s) as required in CW spec
    # Call parent class
    def __init__(self, m_id, frm, to, date, subject, tag, body):  # DO NOT MODIFY Attributes
        super().__init__(m_id, frm, to, date, subject, tag, body)  # Inherits attributes from parent class DO NOT MODIFY

        # Add text statistics to body
        self.add_text_stats()

    def add_text_stats(self):
        """Calculate and append basic statistics to the message body."""
        text = self.body
        num_chars = len(text)             # count characters
        num_words = len(text.split())     # count words
        num_sentences = text.count('.')   # count sentences (simple)

        stats = "\n\n--- Text Statistics ---\n"
        stats += "Characters: " + str(num_chars) + "\n"
        stats += "Words: " + str(num_words) + "\n"
        stats += "Sentences: " + str(num_sentences)

        self.body += stats

    # FB.5.b
    #
    def add_stats(self):
        """Replace 'Body' with sender UID and add simple stats."""
        # Get UID from sender email
        uid = self.frm.split('@')[0]

        # Replace 'Body' with UID
        self.body = self.body.replace("Body", uid)

        # Split body into words
        words = self.body.split()

        # Count words
        word_count = len(words)

        # Find average word length (0 if no words)
        if word_count == 0:
            avg_len = 0
            longest = 0
        else:
            lengths = [len(w) for w in words]
            avg_len = sum(lengths) // word_count
            longest = max(lengths)

        # Add stats at the end
        self.body += f" Stats: Word count:{word_count}, Average word length:{avg_len}, Longest word length:{longest}."
    #FB.5.c
    def show_email(self):
        """ """
        #
        print("PERSONAL")
        #
        print("From: "+str(self.frm))
        #
        print("Date: "+str(self.date))
        #
        print("Subject: "+str(self.subject))
        #
        print("Private: "+str(self.body))
        #
        print("Flagged?"+str(self.flag))