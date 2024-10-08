from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import ModelHelper
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

modelHelper = ModelHelper()

#############################################################
# API ROUTES
#############################################################
@app.route("/predictions", methods=["POST"])
def make_predictions():
    content = request.json["data"]
    print(content)

    parsed_content = {
        "name": content["name"],
        "gamelist_length":9,
        "min_players": int(content["min_players"]),
        "max_players": int(content["max_players"]),
        "min_playtime": int(content["min_playtime"]),
        "max_playtime": int(content["max_playtime"]),    
        "min_age": int(content["min_age"]),
        "min_average_rating": int(content["min_average_rating"]),
    }

    preds = modelHelper.make_game_recommendations(**parsed_content)

    return(jsonify({"ok": True, "prediction": preds}))


#############################################################
# HTML ROUTES
#############################################################

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
