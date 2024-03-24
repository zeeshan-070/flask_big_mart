import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, render_template, redirect, url_for


model=pickle.load(open(r'big_mart.pkl','rb'))
app = Flask(__name__, static_folder='static')


@app.route("/")
def f():
    return render_template("homepage.html")

@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method == "POST":
        
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        
        
        print(f"Name: {name}, Email: {email}, Subject: {subject}, Message: {message}")
        
        
        
        return redirect(url_for("thank_you"))
    
    
    return render_template("contact.html")

@app.route("/thank_you")
def thank_you():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Thank You!</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
            }
            .container {
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #fff;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
                text-align: center;
            }
            p {
                color: #666;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Thank You!</h1>
            <p>Thank you for contacting us! We will get back to you soon.</p>
        </div>
    </body>
    </html>
    """

@app.route("/predict")
def predict():
    return render_template("index.html")

@app.route("/home",methods=["GET","POST"])
def home():
    Weight = float(request.form['Weight'])
    FatContent = float(request.form['FatContent'])
    ProductVisibility  = float(request.form['ProductVisibility'])
    ProductType = float(request.form['ProductType'])
    MRP   = float(request.form['MRP'])
    Outlet = float(request.form['Outlet'])
    Outlet_Establishment_Year = float(request.form['Outlet_Establishment_Year'])
    Item_Identifier = float(request.form['Item_Identifier'])
    OutletSize = float(request.form['OutletSize'])
    LocationType = float(request.form['LocationType'])
    OutletType = float(request.form['OutletType'])

    X = [[Weight,FatContent,ProductVisibility,ProductType,MRP,Outlet,Outlet_Establishment_Year,Item_Identifier,OutletSize,LocationType,OutletType]]

    output = model.predict(X)

    return render_template('output.html',output = output)

if __name__ == "__main__" :
    app.run(debug=True)