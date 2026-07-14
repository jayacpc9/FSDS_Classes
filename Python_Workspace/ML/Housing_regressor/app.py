from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

ml_resources_path ="/Users/chandra/Desktop/FSDS_GenAI_Training/FSDS_Classes/Python_Workspace/ML/Housing_regressor/"

# Load models
model_names = [
    'LinearRegression', 'RobustRegression', 'RidgeRegression', 'LassoRegression', 'ElasticNet',
    'PolynomialRegression', 'SGDRegressor', 'ANN', 'RandomForest', 'SVM', 'LGBM',
    'XGBoost', 'KNN'
]

models = {name: pickle.load(open(f'{ml_resources_path+name}.pkl', 'rb')) for name in model_names}

# Load evaluation results
results_df = pd.read_csv(ml_resources_path+'model_evaluation_results.csv')

@app.route('/')
def index():
    return render_template('index.html', model_names=model_names)

@app.route('/predict_all', methods=['POST'])
def predict_all_models():
    model_name = request.form['model']
    input_data = {
        'Avg. Area Income': float(request.form['Avg. Area Income']),
        'Avg. Area House Age': float(request.form['Avg. Area House Age']),
        'Avg. Area Number of Rooms': float(request.form['Avg. Area Number of Rooms']),
        'Avg. Area Number of Bedrooms': float(request.form['Avg. Area Number of Bedrooms']),
        'Area Population': float(request.form['Area Population'])
    }
    input_df = pd.DataFrame([input_data])
    print("input_data = ",input_data," : model size = ",len(models))

    all_predictions=[]
    for model_name in model_names:

        if model_name in models:
                model = models[model_name]
                prediction = model.predict(input_df)[0].round(2)
                all_predictions.append({
                    "ModelName": model_name,
                    "Prediction" : prediction,
                })
        else:
            all_predictions.append({
                "ModelName": model_name,
                "Prediction" : 'error: Model not found : 400',
            }) 

    print("All Predictions : ",all_predictions)
    return render_template('results_all.html', prediction=prediction, model_name_all=all_predictions)
    


@app.route('/predict', methods=['POST'])
def predict():
    model_name = request.form['model']
    input_data = {
        'Avg. Area Income': float(request.form['Avg. Area Income']),
        'Avg. Area House Age': float(request.form['Avg. Area House Age']),
        'Avg. Area Number of Rooms': float(request.form['Avg. Area Number of Rooms']),
        'Avg. Area Number of Bedrooms': float(request.form['Avg. Area Number of Bedrooms']),
        'Area Population': float(request.form['Area Population'])
    }
    input_df = pd.DataFrame([input_data])
    
    if model_name in models:
        model = models[model_name]
        prediction = model.predict(input_df)[0]
        return render_template('results.html', prediction=prediction, model_name=model_name)
    else:
        return jsonify({'error': 'Model not found'}), 400


@app.route('/user_click', methods=['POST'])
def user_action_handler():
    clicked_button = request.form.get('action')
    print("clicked button = ",clicked_button)

    if( clicked_button == 'single'):
        return predict()
    elif clicked_button == 'all':
        return predict_all_models()
    
    return "Invalid Action Sent", 400

@app.route('/results')
def results():
    return render_template('model.html', tables=[results_df.to_html(classes='data')], titles=results_df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)