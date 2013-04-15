import webapp2
import logging
from util.template import jinja_environment

class IndexHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('index.html')
		self.response.out.write(template.render({}))