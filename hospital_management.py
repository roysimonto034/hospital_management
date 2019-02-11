dctid = {123:'Kc Mukherjee',124:'S prasad',125:'Neelam Singh',126:'Chharu verma',127:'Akhilesh Bhagat'}
ptid = {421:'Dinesh',422:'Sabita',423:'Anmesha',424:'Rohit',425:'Suresh'}
fees={123:700,124:800,125:600,126:500,127:800}
class Doctor(object):
	visit=0
	def __init__(self, doct_id, patient_id=None, checkup=False):
		if doct_id in dctid.keys():
			self.doct_id=doct_id
		else:
			raise Exception("please select id from dctid")
		if patient_id in ptid.keys():
		   self.patient_id=patient_id
		else:
		   raise Exception("Please select id form ptid")

	# def __str__(self):
	# 	return "He is doctor: "+dctid[self.doct_id]


""""Appoint_is is same as doct_id"""


class Patient(Doctor):

	bill=0
	def __init__(self, patient_id, doct_id=None, checkup=False, appoint_id=0):
		super().__init__(doct_id, patient_id, checkup)
		self.checkup = checkup
		self.appoint_id = appoint_id
		

	def appointment(self):
		if self.appoint_id:
			print("Patient: "+ptid[self.patient_id]+" has requested for a doctor")
			if self.doct_id and self.patient_id:
			   print("Appointment confirmed by doctor: "+dctid[self.doct_id])
			   if self.checkup:
				   Doctor.visit+=1
				   print("Doctor "+dctid[self.doct_id]+" has done checkup of "+ptid[self.patient_id])
			   else:
			   		return "Doctor "+dctid[self.doct_id]+"'s visit is Pending"
			else:
				return"Doctor: "+dctid[self.doct_id]+" is Unavialable"
		else:
			return ptid[self.patient_id]+"Patient requires an appointment"

	def billing(self):
		if Patient.bill:
		   Patient.bill+=fees.get(self.doct_id)*Doctor.visit
		   return "Total Bill for patient " + ptid.get(self.patient_id) + " is: " + str(Patient.bill)
		else:
			Patient.bill=fees.get(self.doct_id) * Doctor.visit
			Doctor.visit-=1
			return "Bill for patient "+ptid.get(self.patient_id)+" is: "+str(Patient.bill)
		
		
		
#dct1=Doctor(103)
# dct2=Doctor(126)
dct3=Doctor(doct_id=123,patient_id=425)
dct2=Doctor(doct_id=125,patient_id=425)
# pat2=Patient(109,appoint_id=1)
# pat1=Patient(patient_id=423,doct_id=125,appoint_id=1)
# pat1.appointment()
pat2=Patient(patient_id=425,doct_id=123,appoint_id=1,checkup=True)
pat2.appointment()
print(pat2.billing())
pat2=Patient(patient_id=425,doct_id=125,appoint_id=1,checkup=True)
pat2.appointment()
print(pat2.billing())






