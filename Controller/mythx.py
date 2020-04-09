import subprocess

class mythx:
    state = False
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJmNzNlZDFlNC0yZmJiLTQ3YTYtYjM5NS1iNGY4NDc0YmY0YjYiLCJpYXQiOjE1ODQzNjIzMDEuMzE3LCJpc3MiOiJNeXRoWCBBUEkiLCJleHAiOjE4OTk5MzgzMDEuMzExLCJ1c2VySWQiOiI1ZTZmNzMzMTYyN2MzMzAwMTFhYTFlYWQifQ.zh4eT30xc2JrUMoIt5KtKMIgxNOABsj7MZrmyTw64vQ"
    output = ""
    
    def __init__(self, filePath):
        try:
            self.output =subprocess.check_output(["mythx","--api-key", self.token,"--format", "json", "analyze","--solc-version", "0.4.24", filePath])
            self.state = True
        except:
            self.state = False
