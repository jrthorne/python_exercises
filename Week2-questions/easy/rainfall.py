# Maximum average rainfall
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, denoting the rainfall in millimetres recorded
# for several towns over a 7 day period:

aurukun =  [15, 9, 11, 4, 10, 20, 95]
burdekin = [13, 9, 5, 0, 80, 150, 145]
cardwell = [115, 90, 100, 46, 130, 200, 195]
daintree = [140, 120, 110, 53, 100, 50, 175]
tully = [115, 90, 100, 54, 130, 200, 195]

# Write expressions to calculate the highest average rainfall
# and print the result in a message to screen

sum_au 	= sum(aurukun)
sum_bu	= sum(burdekin)
sum_ca	= sum(cardwell)
sum_da	= sum(daintree)
sum_tu	= sum(tully)

# There are 7 data points in each list
no_data = 7
max_avg = max(sum_au, sum_bu, sum_ca, sum_da, sum_tu) / no_data
print 'The max average rainfall is ', max_avg
