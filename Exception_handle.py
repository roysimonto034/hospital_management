import os
import py_compile
def check_file():
	gh={'x':1,'y':3,'z':2,'y':4}
	try:
		gd=[x for x in range(10)]
		print(gd)
		try:
			fp=open(os.path.join('f:\\Python_Program','progdeep.py'),'r')
			print("Files has been opened")
			print(fp.readline())
			fp.close()
			print("Print stamentent 4")
			print("Print stamentent 5")
			tp=10/0
		except FileNotFoundError:
			print("File is not found")
		except ZeroDivisionError:
			print("cannot be divided by error")
		finally:
			print("Print final inner")
		print("Print stamentent 6")
		# import pdb;pdb.set_trace()
		print("value of gh is"+str(gh['x']))
		# try:
		print("value of gh is"+str(gh['l']))
		# except:
			# print('Keyerror')
	except Exception as e:
		print(e)
	except:
		print("keyerror is raise")
	finally:
		print("print outer outer value")
	print("Print stamentent 7")

check_file()