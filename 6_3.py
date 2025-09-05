def gallon():
    return 3.785 * a

a = float(input("Anna bensan määrä galooneina: "))
while a > 0:
    litra = gallon()
    print(f"Bensan määrä litroina: {litra}")
    a = float(input("Anna bensan määrä galooneina: "))