from typing import Dict, List
from .csv_utils import write_csv
from domain.legislator import Legislator
from domain.vote_result import VoteResult
from domain.vote_type import VoteType

def generate_legislator_vote_counts_csv(legislators: List[Legislator], vote_results: List[VoteResult]) -> None:
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