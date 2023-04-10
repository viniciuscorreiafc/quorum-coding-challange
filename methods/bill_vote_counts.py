from typing import Dict, List
from methods.csv_utils import write_csv
from domain.bill import Bill
from domain.legislator import Legislator
from domain.vote import Vote
from domain.vote_result import VoteResult
from domain.vote_type import VoteType

def generate_bills_csv(legislators: List[Legislator], bills: List[Bill], votes: List[Vote], vote_results: List[VoteResult]) -> None:  
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