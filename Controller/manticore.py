import subprocess

class manticore:
    state = ''
    output = ''
    def __init__(self, filePath):
        try:
            self.output = subprocess.check_output(["manticore","--workspace","manticore","--workspace.dir","result_data", filePath])
            self.state = True
        except:
            self.state = False
