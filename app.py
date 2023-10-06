# https://youtu.be/bluclMxiUkA
"""
Application that predicts heart disease percentage in the population of a town
based on the number of bikers and smokers. 

Trained on the data set of percentage of people biking 
to work each day, the percentage of people smoking, and the percentage of 
people with heart disease in an imaginary sample of 500 towns.

"""

import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import pickle

#Create an app object using the Flask class. 
app = Flask(__name__)

#Load the trained model. (Pickle file)
model = pickle.load(open('models/model.pkl', 'rb'))

#Define the route to be home. 
#The decorator below links the relative route of the URL to the function it is decorating.
#Here, home function is with '/', our root directory. 
#Running the app sends us to index.html.
#Note that render_template means it looks for the file in the templates folder. 

#use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def home():
    return render_template('index.html')

#You can use the methods argument of the route() decorator to handle different HTTP methods.
#GET: A GET message is send, and the server returns data
#POST: Used to send HTML form data to the server.
#Add Post method to the decorator to allow for form submission. 
#Redirect to /predict page with the output
@app.route('/predict',methods=['POST'])
def predict():
    # Get input values from the HTML form and convert them to the appropriate data types
    bedrooms = float(request.form['number of bedrooms'])
    bathrooms = float(request.form['number of bathrooms'])
    square_footage = float(request.form['square footage'])
    house_type = request.form['idx']
    postal_code = request.form['idy']

    # Create a DataFrame with the input features
    input_data = pd.DataFrame({'beds': [bedrooms],
                               'baths': [bathrooms],
                               'sqft': [square_footage],
                               'idx': [house_type],
                               'idy': [postal_code]})

    # Make a prediction using the loaded model
    prediction = model.predict(input_data)

    # Convert the prediction back to its original scale (undo the log transformation)
    predicted_price = np.expm1(prediction)

    return render_template('index.html', prediction_text=f'Predicted house price: ${predicted_price[0]:,.0f}')



#When the Python interpreter reads a source file, it first defines a few special variables. 
#For now, we care about the __name__ variable.
#If we execute our code in the main program, like in our case here, it assigns
# __main__ as the name (__name__). 
#So if we want to run our code right here, we can check if __name__ == __main__
#if so, execute it here. 
#If we import this file (module) to another file then __name__ == app (which is the name of this python file).

if __name__ == "__main__":
    app.run()