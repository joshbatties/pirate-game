from island import Island
from random_gen import RandomGen

class Mode2Navigator:
    def __init__(self, n_pirates: int) -> None:
        """
        Best/Worst Case: O(1)
        """
        self.n_pirates = n_pirates
        self.islands = []

    def add_islands(self, islands: list[Island]):
        """
        Best/Worst Case: O(n), where n is the number of islands
        """
        self.islands.extend(islands)

    def simulate_day(self, crew: int) -> list[tuple[Island | None, int]]:
        """
        Best/Worst Case: O(n), where n is the number of islands
        """
        remaining_crew = crew
        results = []

        while remaining_crew > 0 and self.islands:
            # Select a random island to attack
            island = RandomGen.random_choice(self.islands)

            # Determine the number of pirates to send
            pirates_to_send = min(remaining_crew, island.marines + 1)

            # Update the island's money and marines
            money_earned = min(island.money, pirates_to_send * island.money / max(1, island.marines))
            island.money -= money_earned
            island.marines -= pirates_to_send

            # Remove the island if it has no more money or marines
            if island.money <= 0 or island.marines <= 0:
                self.islands.remove(island)

            # Update the remaining crew and add the result
            remaining_crew -= pirates_to_send
            results.append((island, pirates_to_send))

        # If there are no suitable islands left, add None to the results
        if remaining_crew > 0:
            results.append((None, remaining_crew))

        return results