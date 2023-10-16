from flask import Flask

app = Flask(__name__)

@app.route("/") #app.get("/")
def hello_world():
    return "<p>Nu kan jag ändra allt, haha</p>"

#Fungerar det fortfarande?