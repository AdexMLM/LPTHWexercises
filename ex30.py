people = 30
cars = 30
buses = 30


if cars > people and buses < people:
    print "We should take the cars."
elif cars < people or buses < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars or people > buses:
    print "That's too many buses."
elif buses < cars and people < buses:
    print "Maybe we could take the buses."
else:
    print "We still cannot decide."

if people > buses and cars < buses:
    print "Alrihgt, let's just take the buses."
else:
    print "Fine, let's stay home then."


print buses > cars or people > buses
