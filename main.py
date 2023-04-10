from methods.congress_instance import read_congress_instance
from methods.bill_vote_counts import generate_bills_csv
from methods.legislator_vote_counts import generate_legislator_vote_counts_csv

def main():
  legislators, bills, votes, vote_results = read_congress_instance()
  generate_legislator_vote_counts_csv(legislators, vote_results)
  generate_bills_csv(legislators, bills, votes, vote_results)

if __name__ == "__main__":
  main()
    