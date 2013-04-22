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
        kyle = Player.createPlayer(username="Kyle Vermeer", account=kyleAccount, pool=pool)
        cody = Player.createPlayer(username="Cody Sam", account=codyAccount, pool=pool)
    
        kyleTeam = Team.createTeamWithPlayers([kyle], description="Kyle")
        codyTeam = Team.createTeamWithPlayers([cody], description="Cody")
    
        firstGame = Game.createGameWithTeams([kyleTeam,codyTeam])
        firstGame.updateRatings()
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render({}))

class aboutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('about.html')
        self.response.out.write(template.render({}))
         
class helosHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('helos.html')
        self.response.out.write(template.render({}))
        
class poolsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('pools.html')
        self.response.out.write(template.render({}))
        
class gamesHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('games.html')
        self.response.out.write(template.render({}))
        
class playersHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('players.html')
        self.response.out.write(template.render({}))
        
class submitGameHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('submitGame.html')
        self.response.out.write(template.render({}))
        
class disputeGameHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('disputeGame.html')
        self.response.out.write(template.render({}))
        
class createPoolHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('createPool.html')
        self.response.out.write(template.render({}))
        
class joinPoolHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('joinPool.html')
        self.response.out.write(template.render({}))
        
class contactHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('contact.html')
        self.response.out.write(template.render({}))
        
class blogHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('blog.html')
        self.response.out.write(template.render({}))
        
class termsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('terms.html')
        self.response.out.write(template.render({}))
        
class signUpHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('signUp.html')
        self.response.out.write(template.render({}))
        
class logInHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('logIn.html')
        self.response.out.write(template.render({}))
        
class logOutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('logOut.html')
        self.response.out.write(template.render({}))
