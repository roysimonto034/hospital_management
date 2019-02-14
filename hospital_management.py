dctid = {123:'Kc Mukherjee',124:'S prasad',125:'Neelam Singh',126:'Chharu verma',127:'Akhilesh Bhagat'}
ptid = {421:'Dinesh',422:'Sabita',423:'Anmesha',424:'Rohit',425:'Suresh'}
fees={123:700,124:800,125:600,126:500,127:800}
class Doctor(object):
	visit=0
	def __init__(self, doct_id,report=[], patient_id=None, checkup=False):
		if doct_id in dctid.keys():
			self.doct_id=doct_id
		else:
			raise Exception("please select id from dctid")
		if patient_id in ptid.keys():
		   self.patient_id=patient_id
		else:
		   raise Exception("Please select id form ptid")
		self.report=report
	# def __str__(self):
	# 	return "He is doctor: "+dctid[self.doct_id]


""""Appoint_is is same as doct_id"""


class Patient(Doctor):

	bill=0
	cost=0
	ptid=0
	def __init__(self, patient_id, doct_id=None, checkup=False, appoint_id=0 ,report=[]):
		super().__init__(doct_id, report, patient_id, checkup)
		self.checkup = checkup
		self.appoint_id = appoint_id
		self.total_bill=0

	def appointment(self):
		
		if self.appoint_id:
			print("Patient: "+ptid[self.patient_id]+" has requested for a doctor")
			if self.doct_id and self.patient_id:
			   print("Appointment confirmed by doctor: "+dctid[self.doct_id])
			   if self.checkup:
				   Doctor.visit+=1
				   print("Doctor "+dctid[self.doct_id]+" has done checkup of "+ptid[self.patient_id])
			   else:
			   		print("Doctor "+dctid[self.doct_id]+"'s visit is Pending")
			else:
				print("Doctor: "+dctid[self.doct_id]+" is Unavialable")
		else:
			print(ptid[self.patient_id]+"Patient requires an appointment")

	def fees(self):
		import pdb;pdb.set_trace()
		if self.patient_id!=Patient.ptid:
			Patient.bill=0
			Patient.cost=0
			
		if Patient.bill:
		   Patient.bill+=fees.get(self.doct_id)*Doctor.visit
		   Doctor.visit-=1
		   # return "Total doctor's fees  for patient " + ptid.get(self.patient_id) + " is: " + str(Patient.bill)
		   return Patient.bill
		else:
			Patient.bill=fees.get(self.doct_id) * Doctor.visit
			Doctor.visit-=1
			# return "Doctor fees for patient "+ptid.get(self.patient_id)+" is: "+str(Patient.bill)
			return Patient.bill
		
	def reports(self):
		import pdb;pdb.set_trace()
		if self.patient_id!=Patient.ptid:
			Patient.bill=0
			Patient.cost=0
		reports={'MRI SCAN':5000,'CITY_SCAN':3000,'XRAY':2000,'ECG':4000}
		for rep in self.report:
			Patient.cost+=reports[rep]
		# return "total cost of reports for patient "+ptid.get(self.patient_id)+" is:"+str(Patient.cost)
		return Patient.cost

	def total_discharge_bill(self):
		#import pdb;pdb.set_trace()
		self.total_bill=self.fees()+self.reports()
		print("Doctor's fees  for patient " + ptid.get(self.patient_id) + " is: " + str(Patient.bill))
		print("total cost of reports for patient "+ptid.get(self.patient_id)+" is:"+str(Patient.cost))
		Patient.ptid=self.patient_id
		return "total bill for patient "+ptid.get(self.patient_id)+"is: "+str(self.total_bill)

		
#dct1=Doctor(103)
# dct2=Doctor(126)
dct3=Doctor(doct_id=123,patient_id=425)
dct2=Doctor(doct_id=125,patient_id=425)
dct1=Doctor(doct_id=126,patient_id=425)
# pat2=Patient(109,appoint_id=1)
# pat1=Patient(patient_id=423,doct_id=125,appoint_id=1)
# pat1.appointment()
"""Doctor 1 visted patient 1"""
pat2=Patient(patient_id=425,report=['CITY_SCAN','XRAY'],doct_id=123,appoint_id=1,checkup=True)
pat2.appointment()
print(pat2.reports())
print(pat2.fees())
print('*'*50)

"""Doctor 2 visted patient 1"""
pat2=Patient(patient_id=425,report=['ECG'],doct_id=125,appoint_id=1,checkup=True)
pat2.appointment()
print(pat2.fees())
print(pat2.reports())
print('*'*50)

"""Doctor 2 visted patient 1"""
pat2=Patient(patient_id=425,report=['MRI SCAN'],doct_id=125,appoint_id=1,checkup=True)
pat2.appointment()
print(pat2.fees())
print(pat2.reports())
print('*'*50)

"""Doctor 3 visted patient 1"""
pat2=Patient(patient_id=425,report=['MRI SCAN','ECG'],doct_id=126,appoint_id=1,checkup=True)
pat2.appointment()
print(pat2.total_discharge_bill())
print('*'*50)
#{'MRI SCAN':5000,'CITY_SCAN':3000,'XRAY':2000,'ECG':4000}
# fees={123:700,124:800,125:600,126:500,127:800}
"""Doctor 3 visted patient 1"""

pat1=Patient(patient_id=423,report=['MRI SCAN','ECG'],doct_id=127,appoint_id=1,checkup=False)
pat1.appointment()
print(pat1.total_discharge_bill())