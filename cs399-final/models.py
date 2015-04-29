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
    name = ndb.StringProperty(required=True)
    score = ndb.IntegerProperty(default=100,required=True)
    workagain = ndb.BooleanProperty()
    comment = ndb.StringProperty()
    more = ndb.StringProperty
