import subprocess
import sys
p1=subprocess.Popen([sys.executable,"License-Creator.py"])
p2=subprocess.Popen([sys.executable,"Readme.md-File-Creator.py"])
p1.wait()
p2.wait()
print("All process stopped.")
