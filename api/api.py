from flask import Flask, request
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)
CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost"}


@app.route('/compute', methods=['POST'])
def compute():
    msg = "Operation in progress..."
    age = request.json.get('age')
    try:
        with ClusterRpcProxy(CONFIG) as rpc:
            # asynchronously spawning the compute task
            result = rpc.compute.compute_age(age)
            # return msg, 200git status
        return msg, 200
    except Exception as e:
        return 'error %s' % e, 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# from flask import Flask
# from flask_restful import Resource, Api
#
# app = Flask(__name__)
# api = Api(app)
#
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
#
# api.add_resource(HelloWorld, '/')
#
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')





# from flask import Flask, request
# from nameko.standalone.rpc import ClusterRpcProxy
#
# app = Flask(__name__)
# CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost"}
#
#
# @app.route('/compute', methods=['POST'])
# def compute():
#     msg = "Operation in progress..."
#     age = request.json.get('age')
#     with ClusterRpcProxy(CONFIG) as rpc:
#         # asynchronously spawning the compute task
#         # result = rpc.compute.compute_age(age)
#         return msg, 200
#
#
# app.run(debug=True, host='0.0.0.0')
#
#
