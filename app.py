import csv
from flask import Flask
from flask import render_template
# always use an undersscore with python variables
app = Flask(__name__)
    # need two underscores^

def get_csv():
    csv_path = "./static/la-riots-deaths.csv"
    csv_file = open(csv_path, 'rb')
    # rb tells python how to read the csv file, read binary ^
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    # be careful with lists, because it uses ram of your computer
    return csv_list
    # at the end of a function, always return something. it's job.

# slash is just the homepage of our website
@app.route("/")
def index():
    template = "index.html"
    # creates a blank html template. spacing is very important
    object_list = get_csv()
    return render_template(template, object_list=object_list)

@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    return render_tamplate(template, row_id=row_id)

# if this script is run from the command line... also, if statements need to end with a colon.
if __name__ == "__main__":
        # then fire up Flask test server
        app.run(debug=True, use_reloader=True)
        # needs to be indented, or else won't run. ^^
