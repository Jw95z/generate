# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
# import "packages" from "this" project
from __init__ import app  # Definitions initialization
# Blueprint import api definition
from covid import covid_api
from clock import clocks
from update import update_api
from update_1 import update1_api


from bp_projects.projects import app_projects # Blueprint directory import projects definition
 # register api routes
app.register_blueprint(app_projects) # register api routes
app.register_blueprint(covid_api)
app.register_blueprint(update_api)
app.register_blueprint(update1_api)
app.register_blueprint(clocks)
@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.route('/updates/')  # connects /stub/ URL to stub() function
def updates():
    return render_template("updates.html")
# this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
