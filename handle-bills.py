from enum import Enum 

class VoteType(Enum):
  supportive = 1
  oppositive = 2

class Legislator:
  def __init__(self, id, name):
    self.id = id
    self.name = name

class Bill:
  def __init__(self, id, title, legislatorId):
    self.id = id
    self.title = title
    self.legislatorId = legislatorId

class Vote:
  def __init__(self, id, billId):
    self.id = id
    self.billId = billId

class VoteResult:
  def __init__(self, id, legislatorId, billId, voteType):
    self.id = id
    self.billId = billId
    self.legislatorId = legislatorId
    self.voteType = voteType
    