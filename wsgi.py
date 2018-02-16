import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    file = open('/mnt/hello-world-storage/logfile','w')
    file.write("access from: "+socket.gethostname()+" at: "+time.ctime()+"\n") 
    
    return "Hello World! Greetings from "+socket.gethostname()+"\n"

if __name__ == "__main__":
    application.run()
