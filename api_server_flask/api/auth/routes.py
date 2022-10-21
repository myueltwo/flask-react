from flask_restx import Namespace, Resource

auth_ns = Namespace('auth', description='Authentication of users')


@auth_ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {
                   "success": True,
                   "msg": "Hello world"
               }, 200
