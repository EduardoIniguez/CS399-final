import webapp2

import cgi
from google.appengine.ext import ndb
from google.appengine.api import mail
from google.appengine.api import users

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))


class CreateEvaluation(webapp2.RequestHandler):
    def get(self):
        form ="<div class='form-group'><div class='col-sm-offset-2 col-sm-10'>" \
              "<div class='checkbox'><label class='control-label col-sm-2'>" \
              "<input type='checkbox' checked name='name'>Member Name</label>" \
              "<label class='control-label col-sm-3'><input type='checkbox' name='nameReq'>" \
              "required?</label></div></div></div><div class='form-group'>" \
              "<div class='col-sm-offset-2 col-sm-10'><div class='checkbox'><label class='control-label col-sm-2'>" \
              "<input type='checkbox' checked name='score'>Score </label><label class='control-label col-sm-3'>" \
              "<input type='checkbox' name='scoreReq'>required?</label></div></div></div>" \
              "<div class='form-group'><div class='col-sm-offset-2 col-sm-10'><div class='checkbox'>" \
              "<label class='control-label col-sm-2'><input type='checkbox' checked name='score'>Work with again </label>" \
              "<label class='control-label col-sm-3'><input type='checkbox' name='workAgainReq'>required?</label>" \
              "</div></div></div><div class='form-group' ><div  class='col-sm-offset-2 col-sm-10'><div class='checkbox'>" \
              "<label class='control-label col-sm-2'><input type='checkbox' checked name='comment'>Comment </label>" \
              "<label class='control-label col-sm-3'><input type='checkbox' name='commentReq'>required?</label></div></div></div>"
        temp_var = {'form':form}
        template = env.get_template('createEval.html')
        self.response.write(template.render(temp_var))

    def post(self):
            form = ""
            temp_var = {'form':form }
            template = env.get_template('createEval.html')
            self.response.write(template.render(temp_var))

    # def form(self,fields):
    #     if fields =='':
