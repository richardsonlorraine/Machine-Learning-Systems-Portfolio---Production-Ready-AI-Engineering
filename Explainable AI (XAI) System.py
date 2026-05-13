import shap
explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)