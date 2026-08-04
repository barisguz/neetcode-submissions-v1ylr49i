class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        atSeen = False
        plusEnabled = False
        addMail = ""

        for mail in emails:
            atSeen = False
            plusEnabled = False
            addMail = ""
            for letter in mail:
                if (letter == '@'):
                    atSeen = True
                    addMail += letter
                elif (letter == '.' and atSeen == False): 
                    continue
                elif (letter == '+' and atSeen == False):
                    plusEnabled = True
                elif (plusEnabled and atSeen == False):
                    continue
                else:
                    addMail += letter
            unique.add(addMail)

        return len(unique)

