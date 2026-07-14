import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, SGDRegressor, HuberRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline #data leakages
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor
import lightgbm as lgb
import xgboost as xgb
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle

print("Housing Regression model")

pickle_file_folder_path ="/Users/chandra/Desktop/FSDS_GenAI_Training/FSDS_Classes/Python_Workspace/ML/Housing_regressor/"
#Load dataset
folder_path ="/Users/chandra/Desktop/FSDS_GenAI_Training/FSDS_Classes/Python_Workspace/ML/Housing_regressor/assets/"
file_name ="USA_Housing.csv"
full_path = folder_path+file_name
print("Full File Path = ",full_path)

data = pd.read_csv(full_path)
print(data.head())

# Preprocessing 
X = data.drop(['Price','Address'],axis=1)
y = data['Price']

# Split the test and train data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.2,random_state=0)

models={
    'LinearRegression': LinearRegression(),
    'RobustRegression': HuberRegressor(),
    'RidgeRegression': Ridge(),
    'LassoRegression': Lasso(),
    'ElasticNet': ElasticNet(),
    'PolynomialRegression':Pipeline([
        ('poly', PolynomialFeatures(degree=4)),
        ('linear',LinearRegression())
    ]),
    'SGDRegressor': SGDRegressor(),
    'ANN': MLPRegressor(hidden_layer_sizes=(100),max_iter=1000),
    'RandomForest':RandomForestRegressor(),
    'SVM':SVR(),
    'LGBM':lgb.LGBMRegressor(),
    'XGBoost':xgb.XGBRegressor(),
    'KNN':KNeighborsRegressor()
}

# Train and evaluate models
results=[]
print(results)

for name, model in models.items():
    model.fit(X_train,y_train)
    y_pred=model.predict(X_test)
    mae = mean_absolute_error(y_test,y_pred)
    mse = mean_squared_error(y_test,y_pred)
    r2=r2_score(y_test,y_pred)

    results.append({
        'Model' : name,
        'MAE': mae,
        'MSE':mse,
        'R2':r2
    })
    with open(f'{pickle_file_folder_path+name}.pkl','wb') as f:
        pickle.dump(model,f)

# conver results to Data Frame and save to CSV
results_df = pd.DataFrame(results)
results_df.to_csv(f'{pickle_file_folder_path}model_evaluation_results.csv',index=False)
print("Models have been traned and saved as pickle files, Evaluation results have been saved to model_evaluation.csv")