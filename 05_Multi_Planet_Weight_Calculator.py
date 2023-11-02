def calculate_weight_on_planet(weight_on_earth, gravitational_factor):
    return weight_on_earth * gravitational_factor

# Create a dictionary to store gravitational factors for each planet
gravitational_factors = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Moon": 0.165,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19,
    "Pluto": 0.06,
    "Sun": 27.01
}

# Get user input for weight on Earth
weight_on_earth = float(input("Enter your weight on Earth (in kg) = "))

# Iterate through the dictionary and calculate weight for user-specified planets
while True:
    planet = input("Enter the name of the celestial body (e.g., Mercury, Venus, Moon, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, or Sun) (or type 'exit' to quit) = ")
    if planet == "exit":
        break
    if planet in gravitational_factors:
        weight_on_planet = calculate_weight_on_planet(weight_on_earth, gravitational_factors[planet])
        print(f"Your weight on {planet} is {weight_on_planet} kg")
    else:
        print("Sorry, I don't have information for that celestial body.")