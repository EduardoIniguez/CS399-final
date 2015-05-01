import webapp2

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

from models import FormMod


class CreateEvaluation(webapp2.RequestHandler):
    def get(self):
        form ="<div class='form-group'><div class='col-sm-offset-2 col-sm-10'>" \
              "<div class='checkbox' ><label class='control-label col-sm-2'>" \
              "<input type='checkbox' checked name='nameInclude'>Member Name</label>" \
              "<label class='control-label col-sm-3'><input type='checkbox' name='nameReq'>" \
              "required?</label></div></div></div><div class='form-group'>" \
              "<div class='col-sm-offset-2 col-sm-10'><div class='checkbox'><label class='control-label col-sm-2'>" \
              "<input type='checkbox' checked name='scoreInclude'>Score </label><label class='control-label col-sm-3'>" \
              "<input type='checkbox' name='scoreReq'>required?</label></div></div></div>" \
              "<div class='form-group'><div class='col-sm-offset-2 col-sm-10'><div class='checkbox'>" \
              "<label class='control-label col-sm-2'><input type='checkbox' checked name='workAgainInclude'>Work with again </label>" \
              "<label class='control-label col-sm-3'><input type='checkbox' name='workAgainReq'>required?</label>" \
              "</div></div></div><div class='form-group' ><div  class='col-sm-offset-2 col-sm-10'><div class='checkbox'>" \
              "<label class='control-label col-sm-2'><input type='checkbox' checked name='commentInclude'>Comment </label>" \
              "<label class='control-label col-sm-3'><input type='checkbox' name='commentReq'>required?</label></div></div></div>" \
              "<input type='text' hidden='hidden' name='quest'><input hidden='hidden' type='text' name='questReq'><input hidden='hidden' type='text' name='questType'>"

        # form =
        temp_var = {'form':form}
        template = env.get_template('createEval.html')
        self.response.write(template.render(temp_var))

    def post(self):
        # form = ''
        form = FormMod()
        if self.request.get("nameInclude"):
            form.name = True
            if self.request.get("nameReq"):
                form.nameReq = True
        if self.request.get("scoreInclude"):
            form.score = True
            if self.request.get("scoreReq"):
                form.scoreReq = True
        if self.request.get("workAgainInclude"):
            form.workAgain = True
            if self.request.get("workAgainReq"):
                form.workAgainReq = True
        if self.request.get("commentInclude"):
            form.comment = True
            if self.request.get("commentReq"):
                form.commentReq = True
        form.quest = self.request.get('quest')
        form.questReq = self.request.get('questReq')
        form.questType = self.request.get('questType')
        form =form.put()

        form = "<a href='" + form.urlsafe() +"'>Please Share This Link</a>"
        message = "Here is a link to your new evaluation"
        temp_var = {'form':form, 'message':message }
        template = env.get_template('success.html')

        self.response.write(template.render(temp_var))

