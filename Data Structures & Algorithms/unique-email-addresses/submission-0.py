class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            name_flag = False
            n = len(email)
            valid_email = ''
            i = 0
            while i < n:
                if email[i] == '@':
                    if not name_flag and i < n - 1:
                        name_flag = True
                        i += 1
                        continue
                elif not name_flag and email[i] == '.':
                    i += 1
                    continue
                elif not name_flag and email[i] == '+':
                    while i < n and email[i] != '@':
                        i += 1
                    name_flag = True
                else:
                    valid_email += email[i]
                i += 1
            if name_flag:
                seen.add(valid_email)
        return len(seen)
