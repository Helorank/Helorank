import webapp2
import logging
from util.template import jinja_environment
from models.rankSystem import *

class IndexHandler(webapp2.RequestHandler):
  def get(self):
    kyleAccount = Account(facebookID="KV35")
    kyleAccount.put()
    codyAccount = Account(facebookID="CS22")
    codyAccount.put()
    pool = Pool()
    pool.put()
    kyle = Player(username="Kyle Vermeer", account=kyleAccount, parent=kyleAccount, pool=pool)
    cody = Player(username="Cody Sam", account=codyAccount, parent=codyAccount, pool=pool)
    kyleKey = kyle.put()
    codyKey = cody.put()

    kyleTeam = Team.createTeamWithPlayers([kyle], description="Kyle")
    codyTeam = Team.createTeamWithPlayers([cody], description="Cody")

    firstGame = Game.createGameWithTeams([kyleTeam,codyTeam])
    firstGame.calculateNewELOs()
    template = jinja_environment.get_template('index.html')
    self.response.out.write(template.render({}))