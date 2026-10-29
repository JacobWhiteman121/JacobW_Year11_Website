from bottle import Bottle, run, route, template, view, static_file

app = Bottle()

# ROUTES FOR PAGES

@route('/')
@view('home')  # Uses views/home.tpl
def home():
    return {}  # Dictionary for template variables if needed

@route('/page1')
def page1():
    return template('page1')  # Manual template rendering

@route('/page2')
def page2():
    return template('page2')

@route('/page3')
def page3():
    return template('page3')

# ROUTE FOR STATIC FILES (CSS, images, JS)
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

# START SERVER
if __name__ == "__main__":
    run(host='localhost', port=5379, debug=True, reloader=True) 