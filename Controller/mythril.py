import subprocess

class mythril:
    state = False
    output = ''
    def __init__(self, filePath):
        try:
            subprocess.call("myth -o /eth-security-reporter-py/result_data/mythril.json -i --workspace manticore --workspace.dir result_data "+ filePath, shell=True, check = True)
            self.state = True
        except:
            self.state = False
    
    def getState(self):
        return self.state
    
    def getOutput(self):
        return self.output