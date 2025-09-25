from flask import Flask, send_from_directory, render_template

app = Flask(__name__, template_folder='templates')

# Main page
@app.route('/')
def index():
    return render_template('AfishArchives.html')

# Serve PeopleArchives pages
@app.route('/PeopleArchives/<path:filename>')
def people_archives(filename):
    return send_from_directory('templates/PeopleArchives', filename)

# Serve other templates pages (static files directly in templates folder)
@app.route('/<page>.html')
def other_pages(page):
    return send_from_directory('templates', f'{page}.html')

# Serve assets
@app.route('/Assets/<path:filename>')
def assets(filename):
    return send_from_directory('Assets', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
