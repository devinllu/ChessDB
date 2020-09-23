from flask import render_template, redirect, url_for, request
from flaskapp import app
import urllib
import urllib.request

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/download")
def download_page():
    return render_template("download.html")

@app.route("/statistics")
def statistics_page():
    return render_template("statistics.html")

@app.route("/download", methods=["POST"])
def download_data():
    username = request.form["username_key"]
    filepath = request.form["path_key"]

    if filepath[-1] != '/':
        filepath += '/'

    ## chess.com API -> https://www.chess.com/news/view/published-data-api
    site_url = "https://api.chess.com/pub/player/" + username + "/games/"
    archives_url = site_url + "archives"

    open_url = urllib.request.urlopen(archives_url)
    archives = open_url.read().decode("utf-8").replace("{\"archives\":[\"", "\",\"")
    archives_list = archives.split("\",\"" + site_url)
    archives_list[len(archives_list) - 1] = archives_list[len(archives_list) - 1].rstrip("\"]}")

    # download the data
    for i in range(len(archives_list) - 1):
        get_url = site_url + archives_list[i + 1] + "/pgn"
        filename = archives_list[i + 1].replace("/", "-")
        urllib.request.urlretrieve(get_url, filepath + filename + ".pgn")
        print(filename + ".pgn has been downloaded successfully")

    return username.upper() + " " + filepath.upper()
