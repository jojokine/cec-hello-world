import socket
import time
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    file = open('/mnt/hello-world-storage/logfile','r+')
    file.write("access from: "+socket.gethostname()+" at: "+time.ctime()+"\n")
    
    return "Hello World! Greetings from "+socket.gethostname()+"\n"+file.readlines()+"\n"

    file.close()
    
if __name__ == "__main__":
    application.run()
