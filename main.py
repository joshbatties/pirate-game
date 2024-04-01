from island import Island
from mode1 import Mode1Navigator
from mode2 import Mode2Navigator
from random_gen import RandomGen

def main():
    # Set the random seed for reproducibility
    RandomGen.set_seed(123)

    # Generate random islands
    islands = [Island.random() for _ in range(10)]

    # Get user input for game mode
    while True:
        mode = input("Choose game mode (1 for Mode 1, 2 for Mode 2): ")
        if mode in ['1', '2']:
            break
        print("Invalid input. Please enter 1 or 2.")

    if mode == '1':
        # Mode 1 gameplay
        crew = int(input("Enter the number of crew members: "))
        mode1_navigator = Mode1Navigator(islands, crew)

        # Select islands to attack
        selected_islands = mode1_navigator.select_islands()
        print("\nSelected Islands (Mode 1):")
        for island, crew in selected_islands:
            print(f"Island: {island.name}, Crew: {crew}")

        # Calculate potential earnings for different crew numbers
        crew_numbers = [50, 75, 100, 125, 150]
        potential_earnings = mode1_navigator.select_islands_from_crew_numbers(crew_numbers)
        print("\nPotential Earnings (Mode 1):")
        for crew, earnings in zip(crew_numbers, potential_earnings):
            print(f"Crew: {crew}, Potential Earnings: {earnings:.2f}")

    else:
        # Mode 2 gameplay
        n_pirates = int(input("Enter the number of pirates: "))
        mode2_navigator = Mode2Navigator(n_pirates)
        mode2_navigator.add_islands(islands)

        while True:
            crew = int(input("\nEnter the number of crew members for the day (0 to quit): "))
            if crew == 0:
                break

            # Simulate a day
            day_results = mode2_navigator.simulate_day(crew)
            print("\nDay Simulation Results (Mode 2):")
            for island, crew in day_results:
                if island:
                    print(f"Island: {island.name}, Crew: {crew}")
                else:
                    print("No suitable island found.")

if __name__ == "__main__":
    main()