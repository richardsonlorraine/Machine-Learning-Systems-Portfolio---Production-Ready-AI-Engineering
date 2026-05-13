from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
preprocessor = ColumnTransformer([("num", StandardScaler(), numerical_features), ("cat", OneHotEncoder(), categorical_features)])