
# Building Energy Prediction Model

This project aims to enhance building energy efficiency by predicting heating and cooling loads using Ridge Regression. By optimizing energy use, it contributes to more sustainable building designs, reducing environmental impacts. The model is coupled with a Flask API and an accessible front-end, and is deployed on AWS for broader applicability in real-world scenarios.


## Project Overview
The dataset consists of observations and features related to building design. The primary objective is to predict the Heating Load and Cooling Load based on these features. The project encompasses data preprocessing, exploratory data analysis, model building using Ridge Regression, and evaluation of model performance.
## Technologies Used
Python
Pandas, NumPy, Scikit-Learn
Matplotlib, Seaborn (for visualizations)
Flask (for API)
HTML/CSS (for front-end)
AWS (for deployment)
## Installation and Setup
Clone the repository: git clone [repository URL]
Install required packages: pip install -r requirements.txt
## Usage Guide
Start the Flask server: python app.py
http://ec2-34-207-176-184.compute-1.amazonaws.com:8080/
## Data Preprocessing and Analysis
Checked for null values, duplicates, and outliers.
Performed descriptive statistics using describe().
Analyzed feature correlations and multicollinearity using VIF.

## Model Building and Evaluation
Addressed multicollinearity while retaining essential features.
Applied Ridge Regression for robust prediction.
Evaluated the model using RMSE and R² (Heating: 3.12, 0.91; Cooling: 3.23, 0.89).
Visualized actual vs. predicted values and analyzed residuals to ensure no bias in predictions.

## API and Front-end Interface
Developed a Flask API to interact with the model.
Created a simple HTML/CSS front-end for demonstrating the model's predictions.

## Contributing
Contributions to the project are welcome. Please refer to the contributing guidelines for more information.

## License
This project is licensed under MIT.
