from optparse import OptionParser
from tip_calculator_as_functions import calculate_rate, calculate_meal_costs

def main():
	parser = OptionParser()

	parser.add_option("-m", "--meal", dest="meal_arg", help="Enter the base cost of the meal")
	parser.add_option("-x", "--tax", dest="tax_arg", help="Enter the meal tax rate")
	parser.add_option("-p", "--tip", dest="tip_arg", help="Enter how much tip you want to give")

	(options, args) = parser.parse_args()
	try:
		options_meal_arg = float(options.meal_arg)
		print "The base cost of your meal is '{}'.".format(options_meal_arg)
	except ValueError:
		print "Not convertible to float"
		options_meal_arg = raw_input("Try again; enter a float or integer")

	try:
		options_tax_arg = float(options.tax_arg)
		print "The tax rate for your meal is '{}'.".format(options_tax_arg)
	except ValueError:
		print "Not convertible to float"
		options_tax_arg = raw_input("Try again; enter a float or integer")
	if not options_tax_arg <1:
		options_tax_arg = raw_input("Try again; enter a value betwee 0 and 1")
		#raise AssertionError("tax rate must be between 0 and 1")

	try:
		options_tip_arg = float(options.tip_arg)
		print "The tip rate for your meal is '{}'.".format(options_tip_arg)
	except ValueError:
		print "Not convertible to float"
		options_tip_arg = raw_input("Try again; enter a float or integer")
	if not options_tip_arg <1:
		options_tip_arg = raw_input("Try again; enter a value betwee 0 and 1")
		#raise AssertionError("tip rate must be between 0 and 1")

	tax_value = float(options_tax_arg) * float(options_meal_arg)
	meal_with_tax = float(options_meal_arg) + tax_value
	tip_value = float(options_tip_arg) * meal_with_tax
	total = meal_with_tax + tip_value

	print "The base cost of your meal is %r" % float(options_meal_arg)
	print "The tax applied toward your meal is %r" % tax_value
	print "The tip applied toward your meal is %r, given a tip percent of %r" % (tip_value,float(options_tip_arg))
	print "The total cost of your meal is %r" % total
 
if __name__ == '__main__':
    main()