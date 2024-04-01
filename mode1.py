from island import Island

class Mode1Navigator:
    """
    My approach for the __init method was quite simple, just initialise the number of crew and the islands that can be visited, which are passed as arguments. 
    The only operations done here are assignment operations which are constant time so the complexity is O(1) in the best and worst case.

    My approach for the select_islands method was to calculate the potenital earnings per pirate (which is given by money/marines) for each island and store them using list comprehension.
    I then used a while loop with the halt condition being the list of islands (with per-pirate earning values) being empty, the loop will break when the available crew are exhausted. 
    Inside the loop I would find the remaining island with the highest potential earnings per pirate using the max function with a keyword argument for second element in the tuple (the earnings per pirate)
    Then I would select to send all available crew (upto the number of marines) to that island, by appending a tuple of this number and the island itself to a list which is returned when the method finishes.
    
    My approach for the select_islands_from_crew_numbers method  is to initialise an empty list which will store the total the amount of money you could make with the respective crew size in the input list.
    I then looped over the input list, calling the select_islands method for each crew size
    I then used list comprehension to calculate the earnings for attacking a specific island, which is the minimum of the island's total money and the product of the number of crew sent and the ratio of money to marines (ensuring we don't divide by zero using max(1, island.marines)). These are then added up using the sum function.
    Then append total earnings to the list (potenital_earnings) and return this list after all iterations have been completed.

    My approach for the update_island method was to simply update the island object that is passed as argument to the new money and marine values passed as argument.
    Since all we are doing is updating values which is constant time, so the complexity is O(1) in the best and worst case.
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Best/Worst Case O(1)
        """
        self.crew = crew
        self.islands = islands
        

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Best/Worst Case O(n^2), where n is the number of islands.
        """
        potenital_earnings_per_pirate = [(Island, min(Island.money, Island.money/Island.marines)) for Island in self.islands]
        selected_islands = []
        available = self.crew

        while potenital_earnings_per_pirate:
            highest_earning_island = max(potenital_earnings_per_pirate, key=lambda x: x[1])
            potenital_earnings_per_pirate.remove(highest_earning_island)
            island, earnings_per_pirate = highest_earning_island
            if available == 0:
                break
            crew_to_send = min(available, island.marines)
            selected_islands.append((island, crew_to_send))
            available -= crew_to_send
        return selected_islands



    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Best/Worst Case O(m x n^2)
        where n is the number of islands
        where m is the number of crew configurations
        """
        potenital_earnings = []
        for crew in crew_numbers:
            self.crew = crew
            selected_islands = self.select_islands()
            total_earnings = sum(min(island.money, pirates * island.money/max(1, island.marines)) for island, pirates in selected_islands)
            potenital_earnings.append(total_earnings)

        return potenital_earnings

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Best/Worst Case O(1)
        """
        island.money = new_money
        island.marines = new_marines
