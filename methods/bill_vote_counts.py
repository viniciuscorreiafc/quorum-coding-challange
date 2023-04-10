from typing import Dict, List, Tuple
from methods.csv_utils import write_csv
from domain.bill import Bill
from domain.legislator import Legislator
from domain.vote import Vote
from domain.vote_result import VoteResult
from domain.vote_type import VoteType

def get_names_by_legislators_ids(legislators: List[Legislator]) -> Dict[int, str]:
  names_by_legislators_ids: Dict[int, str] = {}
  
  for legislator in legislators:
    names_by_legislators_ids[legislator.id] = legislator.name

  return names_by_legislators_ids

def get_vote_results_by_vote_ids(vote_results: List[VoteResult]) -> Dict[int, Dict[VoteType, int]]:
  vote_results_by_vote_ids: Dict[int, Dict[VoteType, int]] = {}
  
  for vote_result in vote_results:
    if vote_result.vote_id not in vote_results_by_vote_ids:
      vote_results_by_vote_ids[vote_result.vote_id] = { VoteType.SUPPORTIVE: 0, VoteType.OPPOSITE: 0 }
    vote_results_by_vote_ids[vote_result.vote_id][vote_result.vote_type] += 1

  return vote_results_by_vote_ids

def get_vote_results_by_bill_ids(votes: List[Vote], vote_results_by_vote_ids: Dict[int, Dict[VoteType, int]]) -> Dict[int, Dict[VoteType, int]]:
  vote_results_by_bill_ids: Dict[int, Dict[VoteType, int]] = {}

  for vote in votes:
    if vote.id in vote_results_by_vote_ids:
      vote_results_by_bill_ids[vote.bill_id] = vote_results_by_vote_ids[vote.id]
    else:
      vote_results_by_bill_ids[vote.bill_id] = { VoteType.SUPPORTIVE: 0, VoteType.OPPOSITE: 0 }
    
  return vote_results_by_bill_ids

def get_bill_vote_counts(vote_results_by_bill_ids: Dict[int, Dict[VoteType, int]], bill_id: int) -> Tuple[int, int]:
    supportive_votes = vote_results_by_bill_ids.get(bill_id, {}).get(VoteType.SUPPORTIVE, 0)
    opposite_votes = vote_results_by_bill_ids.get(bill_id, {}).get(VoteType.OPPOSITE, 0)
    return supportive_votes, opposite_votes

def get_bills_vote_results(bills: List[Bill], 
                          names_by_legislators_ids: Dict[int, str], 
                          vote_results_by_bill_ids: Dict[int, Dict[VoteType, int]]) -> List[Dict[str, str]]:
                          
  bills_vote_results = []
  
  for bill in bills:
    supported_votes, opposed_votes = get_bill_vote_counts(vote_results_by_bill_ids, bill.id)
    primary_sponsor_name = names_by_legislators_ids.get(bill.sponsor_id, "Sponsor not found")

    bill_vote_results = {
      "id": bill.id,
      "title": bill.title,
      "supporter_count": supported_votes,
      "opposer_count": opposed_votes,
      "primary_sponsor": primary_sponsor_name
    }
    bills_vote_results.append(bill_vote_results)

  return bills_vote_results

def generate_bills_csv(legislators: List[Legislator], bills: List[Bill], votes: List[Vote], vote_results: List[VoteResult]) -> None:  
  names_by_legislators_ids = get_names_by_legislators_ids(legislators)
  vote_results_by_vote_ids = get_vote_results_by_vote_ids(vote_results)
  vote_results_by_bill_ids = get_vote_results_by_bill_ids(votes, vote_results_by_vote_ids)
  bills_vote_results = get_bills_vote_results(bills, names_by_legislators_ids, vote_results_by_bill_ids)

  write_csv("bills.csv", bills_vote_results)