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
        
class CreateEvaluation(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('createEval.html') 
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', SplashPage),
    ('/index.html', Home),
    ('/createEval.html', CreateEvaluation),

], debug=True)