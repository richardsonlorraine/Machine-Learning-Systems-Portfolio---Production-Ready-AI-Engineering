from sklearn.ensemble import VotingClassifier
ensemble = VotingClassifier(estimators=[('m1', model1), ('m2', model2)], voting='hard')