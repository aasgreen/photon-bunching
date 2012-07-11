#
#his is a list of the probability functions for the beamsplitter

import math as math
from scipy import integrate
import matplotlib.pyplot as plt

math.exp(2)
def Eout(t, Ein,eta):
	out = Ein(t)**2/(integrate.quad(lambda x: eta * Ein(x)**2,0,t)[0]+1)**2
	return sqrt(out)
def normalize(tau):
	if tau == 0.:
		return 1
	else:
		return (1./(math.exp(2.*tau)-1.)**2)

def psi11norm(tau):
	return math.exp(-2.*tau)*(math.exp(tau)-2.*math.exp(-tau))**2
def psi11(tau):
	return (-math.exp(-2.*tau)+1.)*(-math.exp(tau)+2.*math.exp(-tau))**2 * normalize(tau)

def psi11_atom(tau):
	return (-math.exp(tau)+2.*math.exp(-tau))**2 *normalize(tau)

def psi11_field(tau):
	return	(-math.exp(-2.*tau)+1.) * normalize(tau)

def psi11_amp_field(tau):
	return math.exp(-2*tau) * normalize(tau)


def psi20(tau):
	return 2.*(1. -math.exp(-2.*tau))**2 

def psi20norm(tau):
	return 2*(1.-math.exp(-2.*tau))*math.exp(-2.*tau)
def psi02norm(tau):
	return 2*(1.-math.exp(-2.*tau))*math.exp(-2.*tau)
def psi02(tau):
	return 2.*( 1. -math.exp(-2.*tau))**2 *normalize(tau)

def exptest(t):
	data = math.exp(3)
	return data

def ef(tau):
	return (1-math.exp(-2*tau))
def prob_check (t):
	return psi11norm(t)+psi20norm(t)+psi02norm(t)

def plot_prob(funcList, ylim):
	yList = [i/500.*ylim for i in range(500)]
	plt.cla()
	for func in funcList:
		plt.plot(yList, map(func, yList),label=str(func) )
	plt.legend()
	plt.xlabel(r'$\tau$')
	plt.ylabel('Probability')
	plt.ylim([0,3])
	return 0
		

def plot_prob_bs(funcList, ylim):
	yList = [i/500.*ylim for i in range(500)]
	plt.cla()
	for func in funcList:
		plt.plot(map(ef,yList), map(func, yList),label=str(func) )
	plt.legend()
	plt.xlabel('Efficiency')
	plt.ylabel('Probability')
	plt.ylim([0,1])
	return 0
	
