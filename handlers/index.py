import webapp2
import logging
from util.template import jinja_environment
from models.rankSystem import *

class IndexHandler(webapp2.RequestHandler):
  def get(self):
    kyle = Player(firstName="Kyle",lastName="Vermeer")
    cody = Player(firstName="Cody",lastName="Sam")
    kyleKey = kyle.put()
    codyKey = cody.put()

    firstGame = GameResult(playerKeys=[kyleKey,codyKey])
    firstGameKey = firstGame.put()
    firstGame.calculateNewELOs()
    template = jinja_environment.get_template('index.html')
    self.response.out.write(template.render({}))