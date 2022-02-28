import jsonpickle
from flask import Flask, request, render_template

from APIRequests import *
from APIResponse import PostResponse, GetResponse, PutResponse, DeleteResponse

# main-file of the visualizer-backend:
#   - every route and its methods are listed below
#   - the route-methods call the appropriate function and supply it with the user-inputs
#   - the result of the function gets packed into a response
#   - the response gets serialized and sent to the requester
#
# to use the app:
#   - run 'python v_sdn_visualizer.py'
#   - open up localhost:5000
#   - start sending in requests
app = Flask(__name__,  template_folder='.')


@app.route('/')
def main_page():
    return render_template('static/index.html')


@app.route('/network', methods=['GET'])
def network():
    return jsonpickle.encode(get_network(), unpicklable=False)


@app.route('/controller', methods=['GET', 'POST', 'DELETE'])
def controller():
    request_id = request.form.get('id', default='No id')
    if request.method == 'GET':
        request_id = request.args.get('id', default='No id')
        success, data = get_component(request.args)
        response = GetResponse(request_id, success, data)
    if request.method == 'POST':
        success, data = create_controller(request.form)
        response = PostResponse(request_id, success, data)
    if request.method == 'DELETE':
        success, data = remove_component(request.form)
        response = DeleteResponse(request_id, success, data)
    return jsonpickle.encode(response, unpicklable=False)


@app.route('/host', methods=['GET', 'POST', 'DELETE'])
def host():
    request_id = request.form.get('id', default='No id')
    if request.method == 'GET':
        request_id = request.args.get('id', default='No id')
        success, data = get_component(request.args)
        response = GetResponse(request_id, success, data)
    if request.method == 'POST':
        success, data = create_host(request.form)
        response = PostResponse(request_id, success, data)
    if request.method == 'DELETE':
        success, data = remove_component(request.form)
        response = DeleteResponse(request_id, success, data)
    return jsonpickle.encode(response, unpicklable=False)


@app.route('/switch', methods=['GET', 'POST', 'DELETE'])
def switch():
    request_id = request.form.get('id', default='No id')
    if request.method == 'GET':
        request_id = request.args.get('id', default='No id')
        success, data = get_component(request.args)
        response = GetResponse(request_id, success, data)
    if request.method == 'POST':
        success, data = create_switch(request.form)
        response = PostResponse(request_id, success, data)
    if request.method == 'DELETE':
        success, data = remove_component(request.form)
        response = DeleteResponse(request_id, success, data)
    return jsonpickle.encode(response, unpicklable=False)


@app.route('/link', methods=['GET', 'PUT', 'POST', 'DELETE'])
def link():
    request_id = request.form.get('id', default='No id')
    if request.method == 'GET':
        request_id = request.args.get('id', default='No id')
        success, data = get_component(request.args)
        response = GetResponse(request_id, success, data)
    if request.method == 'POST':
        success, data = create_link(request.form)
        response = PostResponse(request_id, success, data)
    if request.method == 'PUT':
        success, data = update_link(request.form)
        response = PutResponse(request_id, success, data)
    if request.method == 'DELETE':
        success, data = remove_component(request.form)
        response = DeleteResponse(request_id, success, data)
    return jsonpickle.encode(response, unpicklable=False)


if __name__ == '__main__':
    app.run(debug=True)
