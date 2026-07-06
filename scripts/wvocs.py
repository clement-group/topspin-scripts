import math
# import struct # Used for bitwise work
import array
#NOTE: The Jython webpage lies about the ordering of parameters in the class creation function! 
# array.zeros(3, 'f') # Does not work
# array.zeros('f',3) # This works!



def f1(x, w1t1=math.pi/2, w1t2=math.pi):
	f1x = array.zeros('d',len(x))
	for i in range(len(x)):
		f1x[i] = 1/((1+x[i]**2)**(3./2.))
		f1x[i] *= math.sin((w1t1) * math.sqrt(1+x[i]**2))
		f1x[i] *= (1- math.cos((w1t2) * math.sqrt(1+x[i]**2)))
	return f1x

def f2(x, w1t1=math.pi/2, w1t2=math.pi):
	f2x = array.zeros('d',len(x))
	for i in range(len(x)):
		f2x[i] = (-1*x[i])/((1+x[i]**2)**(2.))
		f2x[i] *= (1 - math.cos((w1t1) * math.sqrt(1+x[i]**2)))
		f2x[i] *= (1 - math.cos((w1t2) * math.sqrt(1+x[i]**2)))
	return f2x

def get_power(freq, w1, window_filter=True):
	cent = len(freq)/2
	x = array.zeros('d',len(freq))
	for i in range(len(freq)):
		x[i] = (freq[i] - freq[cent]) / w1
	f1x = f1(x)
	f2x = f2(x)
	power = array.zeros('d',len(x))
	for i in range(len(x)):
		power[i] = math.sqrt(f1x[i]**2.0 + f2x[i]**2.0)
		if window_filter:
			power[i] *= abs(x[i]) < 1.73
	return power

def get_freq():
	# As Topspin has no facile way of getting the Hz as a list, this calculates them
	# Also returns the excitation pulse frequency
	# This is based on the convbin2asc AU program
	si = int(GETPAR2("SI")) # size of the spectrum
	offset = float(GETPAR2("OFFSET")) # low field limit of the spectrum
	sf = float(GETPAR2("SF")) # spectrometer frequency
	hzppt = float(GETPAR2("HZpPT")) # Spectral resolution
	# NOTE: the following command might be quite brittle as I don't know the details of how Topspin stores the information for its pulse programs
	T1 = float(GETPAR2("P").split()[1])
	w1 = 1e6/(T1*4)
	
	hzoffset= offset*sf;
	freq = array.zeros('d',si)
	for i in range(si):
		freq[i] = hzoffset - hzppt*(i+0.5)
	
	return freq, w1


frequencies, w1 = get_freq()
# SAVE_ARRAY_AS_1R1I([i%100 for i in range(65536)],None)
# RE()

intensities = GETPROCDATA(-1000000, 10000000) # No way to ask for all of the spectra

scaling_factors = get_power(frequencies,w1)
if len(intensities) != len(scaling_factors):
	MSG("Spectral intensities do no match with the number of frequency points. Aborting scaling")
else:
	for i in range(len(intensities)):
		intensities[i] *= scaling_factors[i]
	
	SAVE_ARRAY_AS_1R1I(intensities, None)


