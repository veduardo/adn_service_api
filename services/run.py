from app import app

#
# Note: Need to have the env variable set in order
# to be able to run the "flask run" command.
#
# export FLASK_APP=~/Projects/adnymics/services/run.py
#

if __name__ == "__main__":
    app.run(debug=True)