import numpy as np
import sys
import matplotlib.pyplot as plt

sys.path.append(".")
from python.Random import Random

#global variables
bin_width = 0.
Xmin = 0.
Xmax = 3.
random = Random()

# Normal distribution with mean zero and sigma = 1
# Note: multiply by bin width to match histogram
def Our(x):
	return np.sin(x)*np.sin(x)



def max_value(f):
	value = list(np.arange(Xmin, Xmax, 0.002))
	valuelist = map(f,value)
	return max(valuelist)
#function to generate the tail
def myflat(x):
	return max_value(Our)


def samplemyflat():
	flat = Xmax - (Xmax-Xmin) *random.rand()
	return flat
def myflatarea(f):
	value = list(np.arange(Xmin,Xmax,0.001))
	flatvalues = map(f,value)
	return max(flatvalues)*(Xmax-Xmin)
#main function
if __name__ == "__main__":


	# default number of samples
	Nsample = 100

	doLog = False
	doExpo = False

	# read the user-provided seed from the command line (if there)
	#figure out if you have to have -- flags before - flags or not
	if '-Nsample' in sys.argv:
		p = sys.argv.index('-Nsample')
		Nsample = int(sys.argv[p+1])

		doLog = bool(sys.argv[p])
	if '-h' in sys.argv or '--help' in sys.argv:
		print ("Usage: %s [-Nsample] number" % sys.argv[0])
		print
		sys.exit(1)


	data = []
	flatx =[]
	Ntrial = 0.
	i = 0.
	while i < Nsample:
		Ntrial += 1
		#print (Ntrial , Nsample)

		X = samplemyflat()#sampleourflat()
		Y = myflat(X)*random.rand()
		func_y = Our(X)
		if Y<Our(X):
			data.append(Y)
			flatx.append(X)

			#print (data)
			i += 1 #increase i and continue
	if Ntrial > 0:
		print("Integration of function is ",float(Nsample)/float(Ntrial)*myflatarea(myflat))
plt.scatter(flatx,data)
plt.show()
