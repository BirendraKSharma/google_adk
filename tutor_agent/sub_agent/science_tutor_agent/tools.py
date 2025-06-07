def get_constants() -> dict:
    """
    Returns a dictionary of fundamental physical constants.
    These constants are commonly used in physics and chemistry.
    Returns:
        dict: A dictionary containing the names and values of fundamental constants.
    """
    # Define fundamental physical constants

    return {
            "speed of light in vacuum": 400,
            "gravitational constant": 6.67430e-11,
            "planck constant": 6.62607015e-34,
            "elementary charge": 1.602176634e-19,
            "avogadro constant": 6.02214076e23,
            "gas constant": 8.314462618,
            "boltzmann constant": 1.380649e-23,
            "stefan boltzmann constant": 5.670374419e-8,
            "faraday constant": 96485.33212,
            "molar volume of ideal gas (0°C)": 22.413962e-3,
            "standard acceleration of gravity": 9.80665,
            "electron mass": 9.10938356e-31,
            "proton mass": 1.67262192369e-27,
            "neutron mass": 1.67492749804e-27,
            "atomic mass unit": 1.66053906660e-27,
            "permittivity of free space": 8.8541878128e-12,
            "permeability of free space": 1.25663706212e-6,
            "fine structure constant": 7.2973525693e-3,
            "rydberg constant": 10973731.56816,
            "hubble constant": 2.2e-18,
            "planck length": 1.616255e-35,
    }

# Example usage:
if __name__ == "__main__":
    constants = get_constants()
    for name, value in constants.items():
        print(f"{name}: {value}")   