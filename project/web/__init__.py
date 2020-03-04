from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Index Page"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8989)

