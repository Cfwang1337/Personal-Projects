from optparse import OptionParser

'''
meal = float(raw_input("What is the base cost of meal?")) 
tax = float(raw_input("What is the meal tax rate? (In hundredths)"))
tip = float(raw_input("How much tip do you want to give? (In hundredths)"))
print sys.argv[1]
print sys.argv[2]
print sys.argv[3]
'''
parser = OptionParser()

parser.add_option("-m", "--meal", dest="meal_arg", help="Enter the base cost of the meal")
parser.add_option("-x", "--tax", dest="tax_arg", help="Enter the meal tax rate")
parser.add_option("-p", "--tip", dest="tip_arg", help="Enter how much tip you want to give")

(options, args) = parser.parse_args()

print "The base cost of your meal is '{}'.".format(options.meal_arg)
print "The tax rate for your meal is '{}'.".format(options.tax_arg)
print "The tip rate for your meal is '{}'.".format(options.tip_arg)

tax_value = float(options.tax_arg) * float(options.meal_arg)
meal_with_tax = float(options.meal_arg) + tax_value
tip_value = float(options.tip_arg) * meal_with_tax
total = meal_with_tax + tip_value

print "The base cost of your meal is %r" % float(options.meal_arg)
print "The tax applied toward your meal is %r" % tax_value
print "The tip applied toward your meal is %r, given a tip of %r percent" % (tip_value,float(options.tip_arg))
print "The total cost of your meal is %r" % total
