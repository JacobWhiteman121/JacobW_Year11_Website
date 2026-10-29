
from bottle import Bottle, run, template, view, static_file

app = Bottle()

# ROUTES FOR PAGES

@app.route('/')
@view('home')
def home():
    return {}

@app.route('/page1')
def page1():
    return template('page1')

@app.route('/page2')
def page2():
    return template('page2')

@app.route('/page3')
def page3():
    return template('page3')

# ROUTE FOR STATIC FILES
@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

# START SERVER LOCALLY
if __name__ == "__main__":
    run(app=app, host='localhost', port=5379, debug=True, reloader=True)
