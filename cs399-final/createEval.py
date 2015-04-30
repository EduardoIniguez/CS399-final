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
              "<div class='checkbox' name='nameInclude'><label class='control-label col-sm-2'>" \
              "<input type='checkbox' checked name='name'>Member Name</label>" \
              "<label class='control-label col-sm-3'><input type='checkbox' name='nameReq'>" \
              "required?</label></div></div></div><div class='form-group'>" \
              "<div class='col-sm-offset-2 col-sm-10'><div class='checkbox' name='scoreInclude'><label class='control-label col-sm-2'>" \
              "<input type='checkbox' checked name='score'>Score </label><label class='control-label col-sm-3'>" \
              "<input type='checkbox' name='scoreReq'>required?</label></div></div></div>" \
              "<div class='form-group'><div class='col-sm-offset-2 col-sm-10'><div class='checkbox' name='workAgainInclude'>" \
              "<label class='control-label col-sm-2'><input type='checkbox' checked name='workAgain'>Work with again </label>" \
              "<label class='control-label col-sm-3'><input type='checkbox' name='workAgainReq'>required?</label>" \
              "</div></div></div><div class='form-group' ><div  class='col-sm-offset-2 col-sm-10'><div class='checkbox' name='commentInclude'>" \
              "<label class='control-label col-sm-2'><input type='checkbox' checked name='comment'>Comment </label>" \
              "<label class='control-label col-sm-3'><input type='checkbox' name='commentReq'>required?</label></div></div></div>" \
              "<input type='text' hidden='hidden' value='' name='quest'><input hidden='hidden' type='text' value='' name='questReq'><input hidden='hidden' type='text' name='questType'>"

        temp_var = {'form':form}
        template = env.get_template('createEval.html')
        self.response.write(template.render(temp_var))

    def post(self):
            form = ''
            if self.request.get('name'):
                form = "pooop"
            # print self.request.get('name')
            # if self.request.get(''):
            #     form+='<div class='form-group'><label class='control-label col-sm-2' for='id_name'>Member Name:</label>' \
            #           '<div class='col-sm-10'><input type='text' class='form-control' id='id_name'></div></div>'
            # if self.request.get('score'):
            #      form += '<div class='form-group'><label class='control-label col-sm-2' for='id_score'>Score:</label>' \
            #              '<div class='col-sm-10'><input type='number' class='form-control' id='id_score' default=100 ></div></div>'
            # if self.request.get('workAgain'):
            #     form += '<div class='form-group'><div class='col-sm-offset-2 col-sm-10'><div class='checkbox'>' \
            #             '<label class='control-label col-sm-2' for='id_workagain'><input type='checkbox' checked id='id_workagain'>' \
            #             ' Work with again</label></div></div></div>'
            temp_var = {'form':form }
            template = env.get_template('createEval.html')
            self.response.write(template.render(temp_var))

    # def form(self,fields):
    #     if fields =='':
