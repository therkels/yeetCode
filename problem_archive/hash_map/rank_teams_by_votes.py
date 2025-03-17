from typing import List
from collections import defaultdict

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        team_ranking = dict()
        vote_size = len(votes[0])
        if len(votes) == 1:
            return votes[0]
        team_ranking = defaultdict(lambda: [0] * len(votes[0]))

        for vote in votes:
            for idx, team in enumerate(vote):
                team_ranking[team][idx] -= 1

        team_rank_sort = sorted(team_ranking.items(), key=lambda item: (item[1], item[0]))

        return "".join([key for key, _ in team_rank_sort])

if __name__ == "__main__":
    S = Solution()
    votes = ["ABC","ACB","ABC","ACB","ACB"]
    print(S.rankTeams(votes))