from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

data = {
    "0": {
        "title": "Keyword",
        "img1": "https://i.kym-cdn.com/entries/icons/original/000/026/563/twitter_cover.jpg",
        "img2": "/resource/tag",
    },
    "1": {
        "title": "Country Code",
        "img1": "/resource/wordcloud_country",
        "img2": "/resource/country",
    },
    "2": {
        "title": "Device",
        "img1": "/resource/wordcloud_device",
        "img2": "/resource/device",
    },
    "3": {
        "title": "Dataflow",
        "img": "/resource/number"
    }
}


@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/<id>')
def keyword_page(id=None):
    if int(id) < 3:
        print("graph!!!!")
        return render_template("graphPage.html", data=data[id], id=id)
    else:
        print("data!!!")
        return render_template("dataflow.html", data=data[id], id=id)

if __name__ == '__main__':
   app.run(debug = True)




