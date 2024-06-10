"""
Find Winner Of Election

Given a list of votes, containing names of candidates in an election, 
    find which candidate received maximum number of votes. 
    If two or more candidate got the same number of votes, 
    return the lexicographically smaller name.

Example One
input: ["sam", "john", "jamie", "sam"]
Output: sam

Example Two
input: ["sam", "john", "sam", "john"]
Output: john

Notes

Constraints:
length of votes <= 105
length of votes[i] <= 105
number of characters in all votes[i] combined <= 105
"""

import unittest

def find_winner_of_election(votes: list[str]) -> str:
    """
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    vote_count = {}
    for vote in votes:
        if vote not in vote_count:
            vote_count[vote] = 1
        else:
            vote_count[vote] += 1
    max_vote = max(vote_count.values())
    # return min(vote_count, key=vote_count.get)
    max_vote_candidates = [candidate
                           for candidate, v_count in vote_count.items()
                           if v_count == max_vote
                           ]
    return min(max_vote_candidates)


class TestFindWinnerOfElection(unittest.TestCase):
    """
        Test case for the `find_winner_of_election` problem.
    """

    def test_find_winner_of_election(self):
        """
            Test case for the `find_winner_of_election` problem.
        """
        self.assertEqual(find_winner_of_election(["sam", "john", "jamie", "sam"]), "sam")
        self.assertEqual(find_winner_of_election(["sam", "john", "sam", "john"]), "john")

if __name__ == "__main__":
    unittest.main()