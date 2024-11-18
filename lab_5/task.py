class Candidate:
    def __init__(self, name, votes ):
        self.name = name
        self.votes = votes

    def percent(self, total_vote):
        return self.votes / total_vote * 100

    def __str__(self):
        return f'{self.name}: {self.votes}%'


class Elections:
    def __init__(self):
        self.candidates = []
        self.total_vote = 0

    def add_candidate(self, candidate: Candidate):
        self.candidates.append(candidate)
        self.total_vote += candidate.votes

    def print_results(self):
        """Метод для виведення результатів виборів"""
        total = self.total_vote
        if total > 0:
            print(f"total votes: {total}")
            for candidate in self.candidates:
                percentage = candidate.percent(total)
                print(f"{candidate.name}: {candidate.votes} votes, {percentage:.2f}% of the total")
        else:
            print("there are  no votes")

    def find_winner(self):
        winner = self.candidates[0]  # Припускаємо, що перший кандидат - це переможець
        for candidate in self.candidates:
            if candidate.votes > winner.votes:
                winner = candidate
        print(f"winner: {winner.name}")
        return winner

    def display_all_candidates(self):
        for candidate in self.candidates:
            candidate.display_info()



def main():

    elections = Elections()

    # Запит на введення кандидатів та кількості голосів
    for i in range(5):
        name = input(f"Enter name candidate {i + 1}: ")
        votes = int(input(f"Enter votes for candidate {name}: "))
        candidate: Candidate = Candidate(name, votes)
        elections.add_candidate(candidate)


    # Виведення результатів виборів
    elections.print_results()

    # Визначення переможця виборів
    elections.find_winner()



if __name__ == '__main__':
    main()
