import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# dataset
data = pd.read_csv('dataset_for_assignment_2.csv')
df = pd.DataFrame(data)

# Data preprocessing: One-hot encoding of categorical variables
X = df[["Age", "Activity Level", "App Sessions", "Distance Travelled (km)"]]
y = df["Calories Burned"]

# One-hot encoding is performed on the category features
preprocessor = ColumnTransformer(
    transformers=[
        ('activity_level', OneHotEncoder(), ['Activity Level']),
        ('age_distance_sessions', 'passthrough', ['Age', 'App Sessions', 'Distance Travelled (km)'])
    ])

# Defining model pipelines
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# fitting model
model.fit(X_train, y_train)

# Predict and evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print(f"error of mean square: {mse}")
