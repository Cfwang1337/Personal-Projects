import sys

meal = float(raw_input("What is the base cost of meal?")) 
tax = float(raw_input("What is the meal tax rate? (In hundredths)"))
tip = float(raw_input("How much tip do you want to give? (In hundredths)"))

tax_value = tax * meal
meal_with_tax = meal + tax_value
tip_value = tip * meal_with_tax
total = meal_with_tax + tip_value

print "The base cost of your meal is %r" % meal
print "The tax applied toward your meal is %r" % tax_value
print "The tip applied toward your meal is %r, given a tip of %r percent" % (tip_value,tip)
print "The total cost of your meal is %r" % total
