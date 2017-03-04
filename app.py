from flask import Flask
from flask import render_template
# always use an undersscore with python variables
app = Flask(__name__)
    # need two underscores^


@app.route('/')
# slash is just the homepage of our website
def index():
    template = "index.html"
    return render_template(template)
# creates a blank html template. spacing is very important


# if this script is run from the command line... also, if statements need to end with a colon.
if __name__ == "__main__":
        # then fire up Flask test server
        app.run(debug=True, use_reloader=True)
        # needs to be indented, or else won't run. ^^
