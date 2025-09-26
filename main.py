from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home_page():
    return render_template("AfishArchives.html")

# Adhvay

@app.route("/Adhvay")
def adhvay_page():
    return render_template("PeopleArchives/Goonvay_Archive.html")

@app.route("/Adhvay/RelationshipStatus")
def adhvay_relationship_page():
    return render_template("Goonvay_relation.html")

@app.route("/Adhvay/W_GoonvaySongs")
def adhvay_songs_page():
    return render_template("W_GoonvaySongs.html")


# Priyam

@app.route("/Priyam")
def priyam_page():
    return render_template("PeopleArchives/Priyam_Archive.html")

@app.route("/Priyam/RelationshipStatus")
def priyam_relationship_page():
    return render_template("Priyam_relation.html")

# Havish
@app.route("/Havish")
def havish_page():
    return render_template("PeopleArchives/Havish_Archive.html")

@app.route("/Havish/RelationshipStatus")
def havish_relationship_page():
    return render_template("Havish_relation.html")

@app.route("/Havish/W_Havish")
def havish_W_page():
    return render_template("Havish_glaze.html")
# Amir
@app.route("/Amir")
def amir_page():    
    return render_template("PeopleArchives/Amir_Archive.html")

@app.route("/Amir/RelationshipStatus")
def amir_relationship_page():
    return render_template("Amir_relation.html")

# Danny
@app.route("/Danny")
def danny_page():
    return render_template("PeopleArchives/Danny.html")

@app.route("/Danny/WDannyPhotos")
def danny_photos_page():    
    return render_template("WDannyPhotos.html")

# Secret Page

@app.route("/Afish")
def afish_page():
    return render_template("Secret_Page.html")

# 404 Handler

@app.errorhandler(404)
def page_not_found(e):
    # "404.html" should live in your templates folder
    return render_template("404.html"), 404

# Assets

@app.route("/Assets/<path:filename>")
def assets(filename):
    return send_from_directory("Assets", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)