#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import cgi
from google.appengine.ext import ndb
from google.appengine.api import mail
from google.appengine.api import users

from createEval import CreateEvaluation
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

class SplashPage(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('basesplash.html') 
        self.response.write(template.render())
        
class Home(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('index.html') 
        self.response.write(template.render())


class About(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('about.html') 
        self.response.write(template.render())
        
class Contact(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('contact.html') 
        self.response.write(template.render())
        
    def post(self):
        userMail=self.request.get("mail")
        subject=self.request.get("subject")
        name=self.request.get("name")
        userMessage=self.request.get("message")
        message=mail.EmailMessage(sender="ei36@nau.edu",subject="Test")
    
    
    # not tested
        if not mail.is_email_valid(userMail):
            self.response.out.write("Check your email again")
            
            message.to=userMail
            message.body="""Thank you!
                     You have entered following information:
                     Your mail: %s
                     Subject: %s
                     Name: %s
                     Message: %s""" %(userMail,subject,name,userMessage)
            message.send()
        template = env.get_template('message.html') 
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', SplashPage),
    ('/index.html', Home),
    ('/createEval.html', CreateEvaluation),
    ('/contact.html', Contact),
    ('/about.html', About),
    

], debug=True)