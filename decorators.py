def outerfunc(func):
	def inner_func(*args, **kwargs):
		print"This function is wrapped"
		return func(*args, **kwargs)
	return inner_func

@outerfunc
def myfunc():
	print 'Hi simonto nice 2 meet u'

@outerfunc
def display(name,age):
	print 'Hello i am {} my age is {}'.format(name,age)
#hi_func = outerfunc('Hi simonto')
#bye_func= outerfunc('bye simonto')

display('simonto',28)

class  Decorator_class(object):
	
	def __init__(self,function):
		self.function=function
	
	def __call__(self, *args, **kwargs):
	   print"call method is called before {}" .format(self.function.__name__)
	   return self.function(*args,**kwargs)
	   
@Decorator_class   
def display_func(name,org):
	print "{} is working in {}".format(name,org)

display_func('newton','zeomega')


class Employee:
	
	def __init__(self,fname,sname,country=None,skill=None):
#		import pdb;pdb.set_trace()
		self.fname=fname
		self.sname=sname
		self.country=country
		self.skill=skill
		self.email=self.fname+self.sname+'@gmail.com'   
	 	
	
	@property
	def gmail(self):
		return "{}{}{}".format(self.fname,self.sname,'@gmail.com')
    
	@property
	def completename(self):
		return '{} {}'.format(self.fname,self.sname)
		
	@completename.setter
	def completename(self,name):
		fn,sn=name.split(' ')
		self.fname=fn
		self.sname=sn
     
	@classmethod
	def information(cls,details):
		fname,sname,cnty,skill=details.split('-')
		return cls(fname,sname,cnty,skill)
	
	def __repr__(self):
		print self.fname+' '+self.sname+' is from '+self.country+' and he does '+self.skill
		
#	@static

	def fullname(self):
		return '{} {}'.format(self.fname,self.sname)
		
stp='Joe-Root-England-Batting'
stp2='Ricky-Pointing-Australia-Batting'
emp1=Employee('Jim','Deikens')
print emp1.fullname()
print emp1.gmail
emp1.fname='Simonto'
print emp1.fullname()
print emp1.email
print emp1.gmail
print emp1.completename
emp1.completename='zabbir Alkwaza'
print emp1.completename
emp2=Employee.information(stp)
emp2.__repr__()
emp3=Employee.information(stp2)
emp3.__repr__()
emp4=Employee.information(stp2)
emp4.__repr__()


