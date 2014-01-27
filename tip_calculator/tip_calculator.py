import sys

'''
meal = float(raw_input("What is the base cost of meal?")) 
tax = float(raw_input("What is the meal tax rate? (In hundredths)"))
tip = float(raw_input("How much tip do you want to give? (In hundredths)"))
'''

print sys.argv[1]
print sys.argv[2]
print sys.argv[3]

tax_value = float(sys.argv[2]) * float(sys.argv[1])
meal_with_tax = float(sys.argv[1]) + tax_value
tip_value = float(sys.argv[3]) * meal_with_tax
total = meal_with_tax + tip_value

print "The base cost of your meal is %r" % float(sys.argv[1])
print "The tax applied toward your meal is %r" % tax_value
print "The tip applied toward your meal is %r, given a tip of %r percent" % (tip_value,float(sys.argv[3]))
print "The total cost of your meal is %r" % total
