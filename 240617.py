import os
import sys



class Customer:
	totalCharge = 0
	totalodometer = 0

	def __init__(self, class_code, rent_days, odometer_start, odometer_end):
		# The customer's classification code b,d,w,q
		self.class_code = class_code
		# The number of days the vehicle was rented
		self.rent_days = rent_days
		# The vehicle's odometer reading at the start of the rental period
		self.odometer_start = odometer_start
		# The vehicle's odometer reading at the end of the rental period
		self.odometer_end = odometer_end
	def totalodometer(self):
	#The function calculates how many otometer the driver mayke
		if self.odometer_start < self.odometer_end:
			totalodometer = float(self.odometer_end - self.odometer_start)
			return totalodometer
	def totalBudaet(self):
	#The function calculates how many money the customer have to pay ccording to classification code
		if self.class_code in ('B' 'b'):
			totalCharge = (40 * int(self.rent_days) +
							float(self.totalodometer()) * 0.25)
			print(' $ ' + str("%.2f" % totalCharge))
		elif self.class_code in ('D' 'd'):
			totalCharge = (60 * int(self.rent_days))
			print('$ ' + str(totalCharge))
		elif float(self.totalodometer / self.rent_days()) <= 100:
			totalCharge = (60 * int(self.rent_days))
			print('$ ' + str(totalCharge))
		elif float(self.totalodometer / self.rent_days()) >= 100:
			totalCharge = (60 * int(self.rent_days) +
							float(self.totalodometer()) * 0.25)
			print('$ ' + str("%.2f" % totalCharge))
		elif self.class_code in ('W' 'w'):
			totalCharge = (int(self.rent_days / 7)) * 190
			print('$ ' + str(totalCharge))
		elif totalCharge == 0:
			print('$ ' + str(totalCharge)) + 190
		elif float(self.totalodometer / (self.rent_days / 7)()) <= 900:
			print('$ ' + str(totalCharge))
		elif float(self.totalodometer / (self.rent_days / 7)()) >= 901 <= 1500:
			totalCharge = (self.rent_days / 7) * 290
			print('$ ' + str("%.2f" % totalCharge))
		elif float(self.totalodometer / (self.rent_days / 7)()) >= 1501:
			totalCharge = (self.rent_days / 7) * 390 + \
				[(self.rent_days / 7 (- 1500)) * 0.25]
			print('$ ' + str("%.2f" % totalCharge))
		else:
			self.class_code not in('b', 'B', 'd', 'D', 'w', 'W')
			totalCharge = 0
			print('$ ' + str(totalCharge))

	def customerProperties(self):
			print "The customer's classification code : " ,self.class_code,"\n", "Total Rent Days: ",self.rent_days,"\n","The vehicle's odometer reading at the start of the rental period : ", self.odometer_start,"\n" ,"The vehicle's odometer reading at the end of the rental period: ",self.odometer_end,"\n","The number of miles driven during the rental period: ", self.totalodometer(),"\n","The amount of money billed to the customer for the rental period: ",self.totalBudaet()

	'''def customerProperties(self):
		print ("The customer's classification code : "
			+ str(self.class_code)
			+ "\n"
			+ "Total Rent Days: "
			+ str(self.rent_days)
			+ "\n"
			+ "The vehicle's odometer reading at the start of the rental period : "
			+ str(self.odometer_start)
			+ "\n"
			+ "The vehicle's odometer reading at the end of the rental period: "
			+ str(self.odometer_end)
			+ "\n"
			+ "The number of miles driven during the rental period: "
			+ str(self.totalodometer())
			+ "\n"
			+ "The amount of money billed to the customer for the rental period: "
			+ str(self.totalBudaet()))'''


print "Please enter Customer Code"
CustomerCode = raw_input()

while CustomerCode  :
	if CustomerCode in('b','B','d','D','w','W'):
		print "Please enter Rent Days:"
		RentDays = raw_input()
		print "Please enter odometer reading at the start of the rent:"
		OdometerStart = int(raw_input())
		print "Please enter odometer reading at the end of the rent:"
		OdometerEnd = int(raw_input())
		NewCustomer = Customer(CustomerCode,RentDays,OdometerStart,OdometerEnd)
		NewCustomer.customerProperties()
		print("\n")
		print "Please enter Customer Code"
		CustomerCode = raw_input()
	if CustomerCode not in('b','B','d','D','w','W','q','Q') :
		print "Please enter Rent Days"
		RentDays = raw_input()
		print "Please enter odometer reading at the start of the rent"
		OdometerStart = raw_input()
		print "Please enter odometer reading at the end of the rent"
		OdometerEnd = raw_input()
		print "You have entered wrong Customer code ,Total Charge for the period will be set to Zero\n"
		NewCustomer = Customer(CustomerCode,RentDays,OdometerStart,OdometerEnd)
		NewCustomer.customerProperties()
		print "Please enter Customer Code"
		CustomerCode = raw_input()
	if CustomerCode in('q','Q'):
		print "The program closes Bay Bye"
		sys.exit()