import csv
from enum import Enum
from typing import TypeVar, Callable, List, Tuple

T = TypeVar('T')

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

def readCsv(filePath: str, constructor: Callable[..., T]) -> List[T]:
  objects = []
  with open(filePath, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      object = constructor(row)
      objects.append(object)
  return objects

def readCongressInstance() -> Tuple[List[Legislator], List[Bill], List[Vote], List[VoteResult]]:
  legislators = readCsv('data-set/legislators.csv', lambda row: Legislator(row['id'], row['name']))
  bills = readCsv('data-set/bills.csv', lambda row: Bill(row["id"], row["title"], row["sponsor_id"]))
  votes = readCsv('data-set/votes.csv', lambda row: Vote(row["id"], row["bill_id"]))
  voteResults = readCsv('data-set/vote_results.csv', lambda row: VoteResult(row["id"], row["legislator_id"], row["vote_id"], row["vote_type"]))
  return legislators, bills, votes, voteResults

def processLegislatorsInformation(legislators: List[Legislator], bills: List[Bill], votes: List[Vote], voteResults: List[VoteResult]):
  print(legislators, bills, votes, voteResults)

def processBillsInformation(legislators: List[Legislator], bills: List[Bill], votes: List[Vote], voteResults: List[VoteResult]):  
  print(legislators, bills, votes, voteResults)

def main():
  legislators, bills, votes, voteResults = readCongressInstance()
  processLegislatorsInformation(legislators, bills, votes, voteResults)
  processBillsInformation(legislators, bills, votes, voteResults)

if __name__ == '__main__':
  main()
    