from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the model
with open("BuildingEnergyModel.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input values from the form
        surface_area = float(request.form['surface_area'])
        roof_area = float(request.form['roof_area'])
        overall_height = float(request.form['overall_height'])
        glazing_area = float(request.form['glazing_area'])
        glazing_area_distribution = int(request.form['glazing_area_distribution'])

        # Create a DataFrame with the input values
        input_data = pd.DataFrame([[surface_area, roof_area, overall_height, glazing_area, glazing_area_distribution]],
                                  columns=['Surface_Area', 'Roof_Area', 'Overall_Height', 'Glazing_Area', 'Glazing_Area_Distribution'])

        # Make predictions
        predictions = model.predict(input_data)

        # Extract heating load and cooling load
        heating_load = predictions[0][0]
        cooling_load = predictions[0][1]

        return render_template('index.html', heating_load=heating_load, cooling_load=cooling_load)

if __name__ == '__main__':
    app.run(debug=True)

