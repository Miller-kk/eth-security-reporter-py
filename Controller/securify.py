import subprocess

class securify:
    state = False
    output = ""
    def __init__(self, filePath):
        try:
            self.output = subprocess.check_output(["java", "-jar" ,"/securify/build/libs/securify.jar", "-o", "./result_data/securify.json", "-fs" ,filePath])
            self.state = True
        except:
            self.state = False