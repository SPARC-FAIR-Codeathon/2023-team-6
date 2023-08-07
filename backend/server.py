# Import flask and datetime module for showing date and time
from flask import Flask
 
# Initializing flask app
app = Flask(__name__)
 
 
# Post route placeholder for running script to generate and return dockerfile
@app.route('/run')
def run_script():
 
    # Returning an api for showing in  reactjs
    return {
        'placeholder':"this is a placeholder"
        }
 
     
# Running app
if __name__ == '__main__':
    app.run(debug=True)
