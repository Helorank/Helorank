import webapp2
from webapp2_extras import routes

routes = [
  webapp2.Route(r'/',handler='handlers.index.IndexHandler'),
  webapp2.Route(r'/About',handler='handlers.index.aboutHandler'),
  webapp2.Route(r'/Helos',handler='handlers.index.helosHandler'),
  webapp2.Route(r'/Pools',handler='handlers.index.poolsHandler'),
  webapp2.Route(r'/Games',handler='handlers.index.gamesHandler'),
  webapp2.Route(r'/Players',handler='handlers.index.playersHandler'),
  webapp2.Route(r'/SubmitGame',handler='handlers.index.submitGameHandler'),
  webapp2.Route(r'/DisputeGame',handler='handlers.index.disputeGameHandler'),
  webapp2.Route(r'/CreatePool',handler='handlers.index.createPoolHandler'),
  webapp2.Route(r'/JoinPool',handler='handlers.index.joinPoolHandler'),
  webapp2.Route(r'/Contact',handler='handlers.index.contactHandler'),
  webapp2.Route(r'/Blog',handler='handlers.index.blogHandler'),
  webapp2.Route(r'/Terms',handler='handlers.index.termsHandler')
]