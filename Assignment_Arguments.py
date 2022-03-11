def greet(name,template):
    template = f"Hello, {name}!"
    return template

greeting = greet("Jim", "" ) 
print(greeting)

celestial_bodies = {
        "sun" : 274,
        "jupiter" : 24.9,
        "neptune" : 11.1,
        "saturn"  : 10.4,
        "earth"   : 9.8,  #earth as default??
        "uranus"  : 8.9,
        "venus"   : 8.9,
        "mars"    : 3.7,
        "mercury" : 3.7,
        "moon"    : 1.6,
        "pluto"   : 0.6
        }
def force(mass,body):
    calculation = mass * body 
    return calculation

result_0 = force(5.972, celestial_bodies["sun"])
print(f"The force is {round(result_0,1)}*10^24 kg")

def pull(m1,m2,d):
    calculation = (6.674*10**-11*(m1*m2))/d**2
    return calculation

result_1 = pull(800,1500,3**2)
print(f"the pull is {round(result_1,8)}")





