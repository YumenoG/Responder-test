import responder

api = responder.API()

@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"

@api.route("/hoge")
def hello_world(req, resp):
    resp.text = "hoge"


api.run()