# String surgery. Given path = "/home/user/report.final.txt", produce ("report.final", ".txt") — the stem and the extension — using only str methods.


path = "/home/user/report.final.txt"

fielname= path.rsplit("/")[-1]

parts=fielname.rsplit(".",1)
parts[1]='.'+ parts[1]

print(tuple(parts))
