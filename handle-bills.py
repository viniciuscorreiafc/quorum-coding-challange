import csv
from enum import Enum
from typing import TypeVar, Callable, Tuple, Dict, List

T = TypeVar('T')

def readCsv(filePath: str, constructor: Callable[..., T]) -> List[T]:
  objects = []
  with open(filePath, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      object = constructor(row)
      objects.append(object)
  return objects

def writeCsv(filename: str, data: List[Dict[str, str]]) -> None:
  with open(filename, 'w', newline='') as csvfile:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
      writer.writerow(row)

class VoteType(Enum):
  supportive = 1
  oppositive = 2

class Legislator:
  def __init__(self, id: int, name: str):
    self.id = id
    self.name = name

class Bill:
  def __init__(self, id: int, title: str, legislatorId: int):
    self.id = id
    self.title = title
    self.legislatorId = legislatorId

class Vote:
  def __init__(self, id: int, billId: int):
    self.id = id
    self.billId = billId

class VoteResult:
  def __init__(self, id: int, legislatorId: int, billId: int, voteType: int):
    self.id = id
    self.billId = billId
    self.legislatorId = legislatorId
    self.voteType = VoteType(int(voteType))

def readCongressInstance() -> Tuple[List[Legislator], List[Bill], List[Vote], List[VoteResult]]:
  legislators = readCsv('data-set/legislators.csv', lambda row: Legislator(row['id'], row['name']))
  bills = readCsv('data-set/bills.csv', lambda row: Bill(row["id"], row["title"], row["sponsor_id"]))
  votes = readCsv('data-set/votes.csv', lambda row: Vote(row["id"], row["bill_id"]))
  voteResults = readCsv('data-set/vote_results.csv', lambda row: VoteResult(row["id"], row["legislator_id"], row["vote_id"], row["vote_type"]))
  return legislators, bills, votes, voteResults

def processLegislatorsInformation(legislators: List[Legislator], voteResults: List[VoteResult]) -> None:
  voteResultsByLegislators: Dict[int, Dict[VoteType, int]] = {}
  legislatorsVoteResults: List[Dict[str, int]] = []

  for voteResult in voteResults:
    if voteResult.legislatorId not in voteResultsByLegislators:
      voteResultsByLegislators[voteResult.legislatorId] = { VoteType.supportive: 0, VoteType.oppositive: 0 }
    voteResultsByLegislators[voteResult.legislatorId][voteResult.voteType] += 1

  for legislator in legislators:
    supportedBills = voteResultsByLegislators[legislator.id][VoteType.supportive] if legislator.id in voteResultsByLegislators else 0
    opposedBills = voteResultsByLegislators[legislator.id][VoteType.oppositive] if legislator.id in voteResultsByLegislators else 0

    legislatorVoteResults = {
      "id": legislator.id,
      "name": legislator.name,
      "num_supported_bills": supportedBills,
      "num_opposed_bills": opposedBills
    }
    legislatorsVoteResults.append(legislatorVoteResults)

  writeCsv("legislators-support-oppose-count.csv", legislatorsVoteResults)

def processBillsInformation(legislators: List[Legislator], bills: List[Bill], votes: List[Vote], voteResults: List[VoteResult]):  
  print(legislators, bills, votes, voteResults)

def main():
  legislators, bills, votes, voteResults = readCongressInstance()
  processLegislatorsInformation(legislators, voteResults)
  processBillsInformation(legislators, bills, votes, voteResults)

if __name__ == '__main__':
  main()
    