import webapp2
from webapp2_extras import routes

routes = [
	webapp2.Route(r'/',handler='handlers.index.IndexHandler')
]