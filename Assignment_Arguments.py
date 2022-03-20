#part 1
def greet(name: str, greeting: str ="Hello, <name>!"):
    return greeting.replace("<name>", name)

print (greet("Jim"))
print(greet("Bob", "What's up, <name>!"))

#part 2
def force(mass: float , body: str = "earth"):
    celestial_bodies = {
        "sun" : 274,
        "jupiter" : 24.9,
        "neptune" : 11.1,
        "saturn"  : 10.4,
        "earth"   : 9.8,
        "uranus"  : 8.9,
        "venus"   : 8.9,
        "mars"    : 3.7,
        "mercury" : 3.7,
        "moon"    : 1.6,
        "pluto"   : 0.6
        }
    return mass * celestial_bodies["neptune"] # or body

result_0 = force(5.972)
print(f"The force is {round(result_0,1)}*10^24 kg")

#part 3

def pull(m1: float,m2: float ,d: float):
    gravity = (6.674*10**-11*(m1*m2))/d**2
    return gravity
result_1 = pull(800,1500,3**2)
print(f"the pull is {round(result_1,8)}")