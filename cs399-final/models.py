import webapp2
import cgi
from google.appengine.ext import ndb
from google.appengine.api import mail
from google.appengine.api import users

from createEval import CreateEvaluation
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

#model
class PeerEvalMod(ndb.model):
    name = ndb.StringProperty()
    nameReq = ndb.BooleanProperty()
    score = ndb.IntegerProperty(default=100, min=0)
    scoreReq = ndb.BooleanProperty()
    workAgain = ndb.BooleanProperty()
    workAgainReq = ndb.BooleanProperty()
    comment = ndb.StringProperty()
    commentReq = ndb.BooleanProperty()
    quest = ndb.StringProperty()
    questReq = ndb.StringProperty()
    questType = ndb.StringProperty()
