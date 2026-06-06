import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

df = pd.read_csv("churn_features.csv")

print("Shape:", df.shape)
print(df["CHURN_FLAG"].value_counts())



df = pd.get_dummies(
    df,
    columns=["INDUSTRY", "REGION", "PLAN"],
    drop_first=True
)

X = df.drop(
    columns=["CUSTOMER_ID", "CHURN_FLAG"]
)

y = df["CHURN_FLAG"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = XGBClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual:")
print(y_test.value_counts())

print("\nPredicted:")
print(pd.Series(predictions).value_counts())

from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, predictions))


accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"Accuracy: {accuracy:.2%}")


df["churn_probability"] = model.predict_proba(X)[:,1]

output = df[
    ["CUSTOMER_ID", "churn_probability"]
]

output.to_csv(
    "predicted_churn.csv",
    index=False
)



from sklearn.metrics import classification_report

print(classification_report(
    y_test,
    predictions
))


import pandas as pd

feature_importance = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
})

print(
    feature_importance
    .sort_values("importance", ascending=False)
    .head(10)
)

print(y.unique())



