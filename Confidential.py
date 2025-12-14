#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Confidential Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Author:                                                                                   ###
###            <Manitej Narayanadasu>, SID<001448592>                                         ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *

# FA.5.a
#Through this class we can encrypt,secure our text and show the mails which are confidential
class Confidential(Mail):
    """
    - we use the constructor method here i.e __init__.
    - instance reference: self
    - Parameters used:m_id,frm,to,date,subject,tag,body.
    - we use super() for parent class implementation to call Mail class.
    """
    # DO NOT CHANGE CLASS NAME OR METHOD NAMES/SIGNATURES
    # Add new method(s) as required in CW spec

    def __init__(self, m_id,frm,to,date,subject,tag,body):    # DO NOT MODIFY Attributes
        super().__init__(m_id,frm,to,date,subject,tag,body)   # Inherits attributes from parent class DO NOT MODIFY
        private = self.encrypt(body)
        self._body = private


    # FA.5.b
    #
    def encrypt(self, body):
        """
        -This method is used to encrypt the text.
        -Firstly, the word length is checked.
        -Then, if we have alphabets, each alphabet get a unicode (integer) using ord() function and is subtracted by 56 and multiplied by word_count.Finally adds to results list.
        -Secondly, if we have numbers they are added by 56 and added to result list
        -Lastly all these encrypted digits are joined to result.
        """
        word_count = len(body.split())
        result = []
        for enc in body:
            if enc.isalpha():
                alpha_pos = ord(enc.lower()) - 56
                multiplies = alpha_pos * word_count
                result.append(str(multiplies))
            elif enc.isdigit():
                num = int(enc)
                letter_is = chr(num + 56)
                result.append(letter_is)
            elif enc == '.':
                result.append(".")
            else:
                result.append(enc)
        return"".join(result)

    # FA.5.c
    def show_email(self):
        """This method is used to show all the Confidential emails. """
        #
        print("CONFIDENTIAL")
        #
        print("From: "+str(self.frm))
        #
        print("Date: "+str(self.date))
        #
        print("Subject: "+str(self.subject))
        #
        print("Encrypted Body: "+str(self.body))
        #
        print("Flagged?"+str(self.flag))

