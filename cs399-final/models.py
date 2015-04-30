from google.appengine.ext import ndb


class FormMod(ndb.Model):
    name = ndb.BooleanProperty(default=False)
    nameReq = ndb.BooleanProperty(default=False)
    score = ndb.BooleanProperty(default=False)
    scoreReq = ndb.BooleanProperty(default=False)
    workAgain = ndb.BooleanProperty(default=False)
    workAgainReq = ndb.BooleanProperty(default=False)
    comment = ndb.BooleanProperty(default=False)
    commentReq = ndb.BooleanProperty(default=False)
    quest = ndb.StringProperty()
    questReq = ndb.StringProperty()
    questType = ndb.StringProperty()


class PeerEvalMod(ndb.Model):
    name = ndb.StringProperty()
    nameReq = ndb.BooleanProperty()
    score = ndb.IntegerProperty(default=100)
    scoreReq = ndb.BooleanProperty()
    workAgain = ndb.BooleanProperty()
    workAgainReq = ndb.BooleanProperty()
    comment = ndb.StringProperty()
    commentReq = ndb.BooleanProperty()
    quest = ndb.StringProperty()
    questReq = ndb.StringProperty()
    questType = ndb.StringProperty()