import numpy as np
import random
import struct
from math import sqrt


def binary(num):
    return int(''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num)),2)


class Prototype:
	def __init__(self, numActions=0, stateDimension=0, group=0, randomInit=True):
		self.theta_value = 0 # theta value associated with each prototype (feature) # float
		self.group = group
		self.frequence_value = 0	# float
		self.featureWidth_value = 0 # float
		self.adjacentcyThreshold = .01
		self.similarityThreshold = .0001

		self.state = [0]*stateDimension
		self.numActions = numActions
		if randomInit:
			self.setRandomly()

	# feature
	def copy(self, feature2):
		self.setFixed(feature2.getState(), feature2.getAction())

	# void
	def setRandomly(self):
		if self.numActions > 0:
			self.setAction(random.randrange(0,self.numActions))
		for i in range(len(self.state)):
			self.state[i] = random.random()

	#void # vector s and int a
	def setFixed(self, s, a):
		self.setState(s)
		self.setAction(a)
		self.setTheta(0.0)
		self.setFrequence(0.0)
		self.setFeatureWidth(0.0)

	#void
	def printPrototpye(self):
		print(str(self.state) + ', ' + str(self.featureWidth_value) + ', ' + str(self.theta_value))

	# bool, other prototype
	def isNeighbor(self, feature2):
		return self.calculateDiff(feature2) <= self.adjacentcyThreshold

	# bool, other prototpye
	def isDifferent(self, feature2):
		return self.calculateDiff(feature2) > self.similarityThreshold

	# unsigned int, feature
	def calculateDiff(self, feature2):

		# diff = 0 #unsigned int
		# actDif = 0 # unsigned int
		# stateDif = 0 # unsigned int
		# state_4_Dif = 0 # unsigned int

		# if self.action == feature2.getAction():
		# 	actDif = 0
		# else:
		# 	actDif = 1

		# difference = sum([sqrt((self.state[i] - feature2.state[i])**2) for i in range(len(self.state))]) # + actDif


		difference = 0
		for j in range(len(self.state)):
			z = binary(self.state[j]) & binary(feature2.state[j])
			while z:
				difference += 1
				z &= z-1 # magic!
		return difference		

		# for i in xrange(0,3):
		# 	if (self.state[i] != feature2.getState()[i])
		# 		stateDif++

		# local = self.state[3]
		# given = feature2.getState()[3]
		# big, small = 0,0
		# if local >= given:
		# 	big = local
		# 	smal = given
		# else:
		# 	big = given
		# 	small = local

		# if big - small <= big * .05:
		# 	state_4_Dif = 0
		# else:
		# 	state_4_Dif = 1

		# difference = actDif + stateDif + state_4_Dif
		return difference

	# void, vector s
	def setState(self, s):
		self.state = s

	# void, int a
	def setAction(self, a):
		self.action = a

	# vector<double>
	def getState(self):
		return self.state

	# int
	def getAction(self):
		return self.action

	# void, float theta
	def setTheta(self, theta):
		self.theta_value = theta

	# float
	def getTheta(self):
		return self.theta_value

	# void, float
	def setFrequence(self, frequence):
		self.frequence_value = frequence

	# float
	def getFrequence(self):
		return self.frequence_value

	# void, float
	def setFeatureWidth(self, featureWidth):
		self.featureWidth_value = featureWidth

	# float
	def getFeatureWidth(self):
		return self.featureWidth_value
