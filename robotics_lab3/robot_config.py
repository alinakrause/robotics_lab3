import robot_model
import math
import numpy as np


if __name__ == '__main__':
	#calculate total homogenous transformation
	a = robot_model.kinematic_chain([[np.pi/2,1.0,0.0,0.0],[np.pi/2,1.0,0.0,0.0]])
	#calculate x,y,z components of position
	pos = robot_model.get_pos(a)
	#calculate roll-pitch-yaw angles
	rot = robot_model.get_rot(a)
	print('two-link planar')
	print('x: %.2f' %pos[0])
	print('y: %.2f' %pos[1])
	print('z: %.2f' %pos[2])
	print('pitch: %.2f' %rot[1])
	print('roll: %.2f' %rot[2])
	print('yaw: %.2f' %rot[0])
	
	#calculate total homogenous transformation
	b = robot_model.kinematic_chain([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
	#calculate x,y,z components of position
	pos = robot_model.get_pos(b)
	#calculate roll-pitch-yaw angles
	rot = robot_model.get_rot(b)
	print('6 DoF UR5e case 1')
	print('x: %.2f' %pos[0])
	print('y: %.2f' %pos[1])
	print('z: %.2f' %pos[2])
	print('pitch: %.2f' %rot[1])
	print('roll: %.2f' %rot[2])
	print('yaw: %.2f' %rot[0])
	
	#calculate total homogenous transformation
	c = robot_model.kinematic_chain([[0,0,0,0],[-np.pi/2,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
	#calculate x,y,z components of position
	pos = robot_model.get_pos(c)
	#calculate roll-pitch-yaw angles
	rot = robot_model.get_rot(c)
	print('6 Dof UR5e case 2')
	print('x: %.2f' %pos[0])
	print('y: %.2f' %pos[1])
	print('z: %.2f' %pos[2])
	print('pitch: %.2f' %rot[1])
	print('roll: %.2f' %rot[2])
	print('yaw: %.2f' %rot[0])
	
	

