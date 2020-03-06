import subprocess

class slither:
    state = False
    output = ""
    def __init__(self, filePath):
        try:
            self.output = subprocess.check_output(["slither", "--json", "/eth-security-reporter-py/result_data/slither.json", filePath])
            self.state = True
        except:
            self.state = False
            
    def getState(self):
        return self.state
    
    def getOutput(self):
        return self.output