import math

# Function to calculate the number of slices a pizza yields
def slicesPerPizza(diameter):
    radius = diameter / 2
    pizza_area = math.pi * (radius ** 2)  
    slices = pizza_area / 14.125  
    return math.floor(slices)  

if __name__ == "__main__":
    print("Welcome to Mario and Luigi's Pizzeria")
    print()
    
    # Get input from the user
    diameter = int(input("Enter the diameter of the pizzas you want to order (in inches): "))
    party_size = int(input("Enter the number of people in your party: "))

    # Calculate slices per pizza
    slices_per_pizza = slicesPerPizza(diameter)

    # Calculate the number of pizzas needed
    total_slices_needed = party_size * 3 
    pizzas_needed = math.ceil(total_slices_needed / slices_per_pizza)  

    print(f"For a party of {party_size} people you need to order {pizzas_needed} pizza(s).")
    print(f"A {(diameter)} inch pizza will yield {slices_per_pizza} slices.")  

