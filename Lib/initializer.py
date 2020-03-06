
import subprocess

def initFiles():
    files =["securify.json","slither.json","smartcheck"]
    for file in files:
        try:
            subprocess.check_output(["rm", "./result_data/"+file])
        except:
            continue

