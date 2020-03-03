import subprocess

class mythx:
    state = False
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI5MTcwMDJlZi1lMTYyLTRkNzMtODQ4Ny1hODkyM2ZjYTc4MDIiLCJpYXQiOjE1ODIxMTc5OTEuNzMsImlzcyI6Ik15dGhYIEFQSSIsImV4cCI6MTg5NzY5Mzk5MS43MjQsInVzZXJJZCI6IjVjZWIwMTQ5MmY4YWRmMDAxOGY1YzcxNyJ9.L-xvd9rxqGsmVCWOMNAlKh_NGfjk7go3s0hG4ksvsDU"
    output = ""
    originPath = "/Users/millerk/eth-security-reporter-py"
    
    def __init__(self, filePath):
        try:
            subprocess.check_output(["mythx", "--access-token", self.token,"--format", "json", "analyze", filePath])
            self.state = True
        except:
            self.state = False
