from flask import Flask 
app = Flask(__name__) 
@app.route("/") 
def home(): 
return "Hello, Docker!" 
if __name__ == "__main__":
