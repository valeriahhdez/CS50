def energy_eq(m):
    c = 300000000
    e = m * c **2
    return e

input_m = int(input("m: "))

energy = energy_eq(input_m)

print(f"E: {energy}")