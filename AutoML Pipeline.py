# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

# Load the dataset
file_path = 'C:/Users/HP/Downloads/CA-1/ev_charging.csv'
data = pd.read_csv(file_path)

# Separate features and target variable
X = data[['Energy_consume', 'Charging_Duration']]
y = data['Cost']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features (necessary for SVR)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize models
lr_model = LinearRegression()
rf_model = RandomForestRegressor(random_state=42)
svr_model = SVR()

# Train the models
lr_model.fit(X_train, y_train)
rf_model.fit(X_train, y_train)
svr_model.fit(X_train_scaled, y_train)

# Make predictions
lr_pred = lr_model.predict(X_test)
rf_pred = rf_model.predict(X_test)
svr_pred = svr_model.predict(X_test_scaled)

# Evaluate models using Mean Squared Error (MSE)
lr_mse = mean_squared_error(y_test, lr_pred)
rf_mse = mean_squared_error(y_test, rf_pred)
svr_mse = mean_squared_error(y_test, svr_pred)

# Display the MSE results for comparison
print(f"Linear Regression MSE: {lr_mse}")
print(f"Random Forest Regressor MSE: {rf_mse}")
print(f"SVR MSE: {svr_mse}")