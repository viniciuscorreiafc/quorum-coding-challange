from domain.vote_type import VoteType

class VoteResult:
  def __init__(self, id: int, legislator_id: int, vote_id: int, vote_type: int):
    self.id = id
    self.vote_id = vote_id
    self.legislator_id = legislator_id
    self.vote_type = VoteType(int(vote_type))