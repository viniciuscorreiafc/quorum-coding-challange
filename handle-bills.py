import csv
from enum import Enum
from typing import TypeVar, Callable, Tuple, Dict, List

T = TypeVar("T")

def read_csv(file_path: str, constructor: Callable[..., T]) -> List[T]:
  instances = []
  with open(file_path, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
      instance = constructor(**row)
      instances.append(instance)
  return instances

def write_csv(file_name: str, data: List[Dict[str, str]]) -> None:
  with open(file_name, "w", newline="") as file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
      writer.writerow(row)

class VoteType(Enum):
  SUPPORTIVE = 1
  OPPOSITE = 2

class Legislator:
  def __init__(self, id: int, name: str):
    self.id = id
    self.name = name

class Bill:
  def __init__(self, id: int, title: str, sponsor_id: int):
    self.id = id
    self.title = title
    self.sponsor_id = sponsor_id

class Vote:
  def __init__(self, id: int, bill_id: int):
    self.id = id
    self.bill_id = bill_id

class VoteResult:
  def __init__(self, id: int, legislator_id: int, vote_id: int, vote_type: int):
    self.id = id
    self.vote_id = vote_id
    self.legislator_id = legislator_id
    self.vote_type = VoteType(int(vote_type))

def read_congress_instance() -> Tuple[List[Legislator], List[Bill], List[Vote], List[VoteResult]]:
  legislators = read_csv("data-set/legislators.csv", Legislator)
  bills = read_csv("data-set/bills.csv", Bill)
  votes = read_csv("data-set/votes.csv", Vote)
  vote_results = read_csv("data-set/vote_results.csv", VoteResult)
  return legislators, bills, votes, vote_results

def process_legislators_information(legislators: List[Legislator], vote_results: List[VoteResult]) -> None:
  vote_results_by_legislators_ids: Dict[int, Dict[VoteType, int]] = {}
  legislators_vote_results: List[Dict[str, int]] = []

  for vote_result in vote_results:
    if vote_result.legislator_id not in vote_results_by_legislators_ids:
      vote_results_by_legislators_ids[vote_result.legislator_id] = { VoteType.SUPPORTIVE: 0, VoteType.OPPOSITE: 0 }
    vote_results_by_legislators_ids[vote_result.legislator_id][vote_result.vote_type] += 1

  for legislator in legislators:
    supported_bills = vote_results_by_legislators_ids[legislator.id][VoteType.SUPPORTIVE] if legislator.id in vote_results_by_legislators_ids else 0
    opposed_bills = vote_results_by_legislators_ids[legislator.id][VoteType.OPPOSITE] if legislator.id in vote_results_by_legislators_ids else 0

    legislator_vote_results = {
      "id": legislator.id,
      "name": legislator.name,
      "num_supported_bills": supported_bills,
      "num_opposed_bills": opposed_bills
    }
    legislators_vote_results.append(legislator_vote_results)

  write_csv("legislators-support-oppose-count.csv", legislators_vote_results)

def process_bills_information(legislators: List[Legislator], bills: List[Bill], votes: List[Vote], vote_results: List[VoteResult]) -> None:  
  names_by_legislators_ids: Dict[int, str] = {}
  vote_results_by_vote_ids: Dict[int, Dict[VoteType, int]] = {}
  vote_results_by_bill_ids: Dict[int, Dict[VoteType, int]] = {}
  bills_vote_results = []

  for legislator in legislators:
    names_by_legislators_ids[legislator.id] = legislator.name

  for vote_result in vote_results:
    if vote_result.vote_id not in vote_results_by_vote_ids:
      vote_results_by_vote_ids[vote_result.vote_id] = { VoteType.SUPPORTIVE: 0, VoteType.OPPOSITE: 0 }
    vote_results_by_vote_ids[vote_result.vote_id][vote_result.vote_type] += 1

  for vote in votes:
    if vote.id in vote_results_by_vote_ids:
      vote_results_by_bill_ids[vote.bill_id] = vote_results_by_vote_ids[vote.id]
    else:
      vote_results_by_bill_ids[vote.bill_id] = { VoteType.SUPPORTIVE: 0, VoteType.OPPOSITE: 0 }

  for bill in bills:
    supported_votes = vote_results_by_bill_ids[bill.id][VoteType.SUPPORTIVE] if bill.id in vote_results_by_bill_ids else 0
    opposed_votes = vote_results_by_bill_ids[bill.id][VoteType.OPPOSITE] if bill.id in vote_results_by_bill_ids else 0
    primary_sponsor_name = names_by_legislators_ids[bill.sponsor_id] if bill.sponsor_id in names_by_legislators_ids else "Sponsor not found"

    bill_vote_results = {
      "id": bill.id,
      "title": bill.title,
      "supporter_count": supported_votes,
      "opposer_count": opposed_votes,
      "primary_sponsor": primary_sponsor_name
    }
    bills_vote_results.append(bill_vote_results)

  write_csv("bills.csv", bills_vote_results)

def main():
  legislators, bills, votes, vote_results = read_congress_instance()
  process_legislators_information(legislators, vote_results)
  process_bills_information(legislators, bills, votes, vote_results)

if __name__ == "__main__":
  main()
    