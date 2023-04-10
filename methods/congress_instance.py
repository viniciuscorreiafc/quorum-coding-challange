from typing import Tuple, List
from methods.csv_utils import read_csv
from domain.bill import Bill
from domain.legislator import Legislator
from domain.vote import Vote
from domain.vote_result import VoteResult

def read_congress_instance() -> Tuple[List[Legislator], List[Bill], List[Vote], List[VoteResult]]:
  legislators = read_csv("data-set/legislators.csv", Legislator)
  bills = read_csv("data-set/bills.csv", Bill)
  votes = read_csv("data-set/votes.csv", Vote)
  vote_results = read_csv("data-set/vote_results.csv", VoteResult)
  return legislators, bills, votes, vote_results