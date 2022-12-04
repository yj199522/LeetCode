class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = set()
        for e in emails:
            name, domain = e.split('@')
            name = name.split('+')[0].replace('.', '')
            d.add((name, domain))
        return len(d)
            
        