import math
import numpy as np

def dh_transformation(theta, a, d, alpha):
	dh = [[np.cos(theta),-np.sin(theta)*np.cos(alpha),np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
	[np.sin(theta),np.cos(theta)*np.cos(alpha),-np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
	[0.0, np.sin(alpha), np.cos(alpha), d],
	[0.0,0.0,0.0,1.0]]
	return dh

def kinematic_chain(dh_param):
	trans = np.identity(4)
	for x in dh_param:
		dh = dh_transformation(x[0],x[1],x[2],x[3])
		trans = np.matmul(trans,dh)
	return trans

def get_pos(trans):
	x = trans[0][3]
	y = trans[1][3]
	z = trans[2][3]
	pos = [x,y,z]
	return pos

def get_rot(trans):
	phi = np.arctan(trans[1][0]/trans[0][0])
	theta = np.arctan((-1*trans[2][0])/(np.sqrt((trans[2][1]*trans[2][1])+(trans[2][2]*trans[2][2]))))
	psi = np.arctan(trans[2][1]/trans[2][2])
	angles = [phi,theta,psi]
	return angles
		