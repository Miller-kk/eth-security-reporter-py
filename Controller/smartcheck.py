import subprocess

class smartcheck:
    state = ''
    output = ''
    def __init__(self, filePath):
        try:
            print(filePath)
            self.output = subprocess.check_output(["smartcheck", "-p", filePath])
            self.state = True
        except:
            self.state = False
    