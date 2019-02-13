from math import sin, pi

class Borwein ():
	def __init__(self, n):
		self.n = n
	def get_n(self):
		return (self.n)
	def compute(self, x):
		k = 0
		resultat = 1
		while k != self.n + 1:
			up = sin(x / ((2 * k) + 1))
			down = x / ((2 * k) + 1)
			if down != 0:
				resultat = resultat * (up / down)
			k = k + 1
		return (resultat)
