import webapp2

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

from google.appengine.ext import ndb
from models import PeerEvalMod


class TakeEvaluation(webapp2.RequestHandler):
    def get(self, surveyID):
        try:
            formKey = ndb.Key(urlsafe=surveyID)
            formtemp = formKey.get()
            form = ''
            if formtemp.name:
                form +='<div class="form-group"><label>Member Name:</label><input type="text" name="name" class="form-control" '
                if formtemp.nameReq:
                    form += 'required '
                form += '></div>'
            if formtemp.score:
                form +='<div class="form-group"><label>Member Score:</label><input type="number" name="score" class="form-control" placeholder="100" '
                if formtemp.scoreReq:
                    form += 'required '
                form += '></div>'
            if formtemp.workAgain:
                form +='<div class="form-group"><label>Work with Again:</label><input type="checkbox" name="workAgain" class="form-control" '
                if formtemp.workAgainReq:
                    form += 'required '
                form += '></div>'
            if formtemp.comment:
                form +='<div class="form-group"><label>Comments:</label><input type="text" name="comments" class="form-control" '
                if formtemp.commentReq:
                    form += 'required '
                form += '></div>'
            questStr = formtemp.quest.split(",")
            questReqStr = formtemp.questReq.split(",")
            questTypeStr = formtemp.questType.split(",")
            count = 0
            for i in range(0,len(questStr)):
                if questStr[i].replace(" ","")!="":
                    count += 1
                    form += '<div class="form-group"><label>' +questStr[i] + ':</label><input type='
                    if questTypeStr[i]=="TF":
                        form += '"checkbox" '
                    elif questTypeStr[i]=="rate":
                        form += '"number" placeholder="100"'
                    else:
                        form += '"text" '
                    form += 'name="custom'
                    form += str(i)
                    form += '" class="form-control" '
                    test = ''
                    if questReqStr[i]=="true":
                        form += 'required '
                    form += '></div>'

            # form = len(questStr[2]) #len(questReqStr) + len(questTypeStr)
            temp_var = {'form':form, 'count':count, 'test':test}
            template = env.get_template('takeEval.html')
            self.response.write(template.render(temp_var))
        except:
            # pass
            self.response.write("<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1>The resource could not be found.<br /><br /></body></html>")


    def post(self, id):
        form = ''
        x = self.request.get('field_count')
        x = int(x)
        test = ''
        # for i in range(0,x):
        submission = PeerEvalMod()
            # test+=str(i)
            # if i !=0:
            #     name = "name"+ str(i)
            #     score = "score" + str(i)
            #     workAgain = "workAgain" + str(i)
            #     comments = "comments"+ str(i)
            # else:
        name = "name"
        score = "score"
        workAgain = "workAgain"
        comments = "comments"
        # test +=workAgain
        if self.request.get(name):
            submission.name = str(self.request.get(name))
            # test = self.request.get("name")
        if self.request.get(score):
            submission.score = int(self.request.get(score))
        if not(self.request.get(workAgain)):
            submission.workAgain = False
        if self.request.get("comments"):
            submission.comment= str(self.request.get(comments))
        custSTR = ''
        if x>0:
            for i in range(0,x):
                test = "custom" + str(i)
                custSTR += str(self.request.get(test))
                custSTR += ","
            # testes = submission
        test = ''
        submission.quest = custSTR

        submission.put()
        form = "<a href='.'>Please Click Here to Go Home</a>"
        message ="Evaluation Submitted"
        temp_var = {'form':form, 'message':message,'test':test }
        template = env.get_template('success.html')

        self.response.write(template.render(temp_var))

