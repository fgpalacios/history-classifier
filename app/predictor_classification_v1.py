
from flask import Response
import json

#Load ML Pkgs
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier


def run_predictor(input_text):
    filename = './app/model/classifications_v1.sav'
    loaded_model = joblib.load(filename)

    pred = {}
    itemProb = 0
    auxPred = [loaded_model.classes_.tolist(),loaded_model.predict_proba([input_text])[0].tolist()]
    for itemPredLabel  in auxPred[0]:
        pred[itemPredLabel]= auxPred[1][itemProb]
        itemProb += 1

    y_pred_dt = json.dumps(dict(sorted(pred.items(), key=lambda item: item[1],reverse=True)))

    return y_pred_dt
