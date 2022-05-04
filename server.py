from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

data = {
    "0": {
        "title": "Keyword",
        "img1": "https://i.ibb.co/z5PJSZd/wordcloud-tag.jpg",
        "img2": "https://i.ibb.co/zJmH31r/tag.jpg",
    },
    "1": {
        "title": "Country Code",
        "img1": "https://i.ibb.co/3Fhhxqn/wordcloud-country.jpg",
        "img2": "https://i.ibb.co/PzwLdyT/country.jpg",
    },
    "2": {
        "title": "Device",
        "img1": "https://i.ibb.co/q0TjZ8v/wordcloud-device.jpg",
        "img2": "https://i.ibb.co/R7hPK6w/device.jpg",
    },
    "3": {
        "title": "Dataflow",
        "img": "https://i.ibb.co/2FGwnxZ/number.jpg"
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




