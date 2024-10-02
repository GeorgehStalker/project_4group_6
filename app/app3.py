from flask import Flask, render_template, redirect, request, jsonify
import pickle
import pandas as pd
# from modelHelper import ModelHelper
# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# modelHelper = ModelHelper()      
# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    # Return template and data
    return render_template("about_us.html")

@app.route("/tableau_1")
def tableau():
    # Return template and data
    return render_template("tableau_1.html")

@app.route("/tableau_2") 
def tableau2():
    # Return template and data
    return render_template("tableau_2.html")

@app.route("/prediction")
def prediction():
    # Return template and data
    return render_template("prediction.html") 

@app.route("/Predictions", methods=["GET"])
def get_predictions():
    return(jsonify({"ok": True}))
     

def makePredictions(sex_flag, age, fare, familySize, p_class, embarked, has_cabin):
    # create dataframe of one row for inference
    df = pd.DataFrame()
    df["Sex"] = [sex_flag]
    df["Age"] = [age]
    df["Fare"] = [fare]
    df["Has_Cabin"] = [has_cabin]
    df["Family_Size"] = [familySize]
    df["Pclass"] = [p_class]
    df["Embarked"] = [embarked]

    # model
    model = pickle.load(open("titanic_model_pipeline2.h5", 'rb'))

    # columns in order
    df = df.loc[:, ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'Has_Cabin', 'Family_Size']]

    preds = model.predict_proba(df)
    return(preds[0][1])
    
@app.route("/Predictions", methods=["POST"])
def make_predictions():
    content = request.json["data"]
    print(content)

    # parse
    sex_flag = content["sex_flag"]
    age = float(content["age"])
    fare = float(content["fare"])
    familySize = int(content["familySize"])
    p_class = int(content["p_class"])
    embarked = content["embarked"]
    has_cabin = bool(int(content["has_cabin"]))

    preds = modelHelper.makePredictions(sex_flag, age, fare, familySize, p_class, embarked, has_cabin)
    return(jsonify({"ok": True, "prediction": str(preds)}))


#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
