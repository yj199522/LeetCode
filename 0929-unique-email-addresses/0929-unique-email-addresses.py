class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = []
        for email in emails:
            emailSplit = email.split('@')
            domainName = emailSplit[1]
            localName = emailSplit[0].replace('.','').split('+')[0]
            emailAdd = localName + '@' + domainName
            if emailAdd not in result:
                result.append(emailAdd)
        return len(result)
            
        