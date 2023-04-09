import csv
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

def readLegislators(): 
  legislators = []
  with open('data-set/legislators.csv', mode='r') as legislatorsFile:
    legislatorsReader = csv.DictReader(legislatorsFile)
    count = 0
    for row in legislatorsReader:
        count += 1
        if count == 0:
            continue
        lagislator = Legislator(row["id"], row["name"])
        legislators.append(lagislator)
  return legislators

def readBills(): 
  bills = []
  with open('data-set/bills.csv', mode='r') as billsFile:
    billsReader = csv.DictReader(billsFile)
    count = 0
    for row in billsReader:
        count += 1
        if count == 0:
            continue
        bill = Bill(row["id"], row["title"], row["sponsor_id"])
        bills.append(bill)
  return bills

def readVotes(): 
  votes = []
  with open('data-set/votes.csv', mode='r') as votesFile:
    votesReader = csv.DictReader(votesFile)
    count = 0
    for row in votesReader:
        count += 1
        if count == 0:
            continue
        vote = Vote(row["id"], row["bill_id"])
        votes.append(vote)
  return votes

def readVoteResults(): 
  voteResults = []
  with open('data-set/vote_results.csv', mode='r') as voteResultsFile:
    voteResultsReader = csv.DictReader(voteResultsFile)
    count = 0
    for row in voteResultsReader:
        count += 1
        if count == 0:
            continue
        vote = VoteResult(row["id"], row["legislator_id"], row["vote_id"], row["vote_type"])
        voteResults.append(vote)
  return voteResults

def readCongressInstance():
  legislators = readLegislators()
  bills = readBills()
  votes = readVotes()
  voteResults = readVoteResults()
  return legislators, bills, votes, voteResults

def main():
  legislators, bills, votes, voteResults = readCongressInstance()
  print(legislators, bills, votes, voteResults)

if __name__ == '__main__':
  main()
    