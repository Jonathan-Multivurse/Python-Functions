from flask import render_template

def test_hello_world(request):
    return render_template('test_hello_world.html')