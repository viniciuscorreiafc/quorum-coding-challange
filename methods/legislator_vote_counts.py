from typing import Dict, List, Tuple
from .csv_utils import write_csv
from domain.legislator import Legislator
from domain.vote_result import VoteResult
from domain.vote_type import VoteType

def get_vote_results_by_legislators_ids(vote_results: List[VoteResult]) -> Dict[int, Dict[VoteType, int]]: 
  vote_results_by_legislators_ids: Dict[int, Dict[VoteType, int]] = {}

  for vote_result in vote_results:
    if vote_result.legislator_id not in vote_results_by_legislators_ids:
      vote_results_by_legislators_ids[vote_result.legislator_id] = { VoteType.SUPPORTIVE: 0, VoteType.OPPOSITE: 0 }
    vote_results_by_legislators_ids[vote_result.legislator_id][vote_result.vote_type] += 1

  return vote_results_by_legislators_ids

def get_legislator_vote_counts(vote_results_by_legislator_ids: Dict[int, Dict[VoteType, int]], legislator_id: int) -> Tuple[int, int]:
    supportive_votes = vote_results_by_legislator_ids.get(legislator_id, {}).get(VoteType.SUPPORTIVE, 0)
    opposing_votes = vote_results_by_legislator_ids.get(legislator_id, {}).get(VoteType.OPPOSITE, 0)
    return supportive_votes, opposing_votes

def get_legislators_vote_results(legislators: List[Legislator], vote_results_by_legislators_ids: Dict[int, Dict[VoteType, int]]) -> List[Dict[str, str]]:
  legislators_vote_results: List[Dict[str, str]] = []

  for legislator in legislators:
    supported_bills, opposed_bills = get_legislator_vote_counts(vote_results_by_legislators_ids, legislator.id)

    legislator_vote_results = {
      "id": legislator.id,
      "name": legislator.name,
      "num_supported_bills": supported_bills,
      "num_opposed_bills": opposed_bills
    }
    legislators_vote_results.append(legislator_vote_results)
  
  return legislators_vote_results

def generate_legislator_vote_counts_csv(legislators: List[Legislator], vote_results: List[VoteResult]) -> None:
  vote_results_by_legislators_ids = get_vote_results_by_legislators_ids(vote_results)
  legislators_vote_results = get_legislators_vote_results(legislators, vote_results_by_legislators_ids)

  write_csv("legislators-support-oppose-count.csv", legislators_vote_results)