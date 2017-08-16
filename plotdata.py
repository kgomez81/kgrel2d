# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 13:27:18 2017
@author: Kevin Gomez (Masel Lab)
Script to process data generated by simulations in Mathematica code.
"""

# import packages needed for script
import pickle
import scipy as sp
import numpy as np
import copy as cpy

# set parameters of simulation and create required variables
[N,s1,s2,U1,U2] = [1e9,1e-2,1e-2,1e-5,1e-5];

# calculate desai and fisher (2007) theoretical "v" and "tau_est"
vU_thry = s1*s1*(2*np.log(N*s1)-np.log(s1/(1*U1)))/((np.log(s1/(1*U1)))**2)
v2U_thry = 0.5*s1*s1*(2*np.log(N*s1)-np.log(s1/(2*U1)))/((np.log(s1/(2*U1)))**2)
tau_est = 0.5*s1/v2U_thry

# section of code for processing new data from Mathematica simulations
data_name = '_N-10p09_c1-0d01_c2-0d01_U1-1x10pn5_U2-1x10pn5_exp2'
#folder_location = 'Documents/kgrel2d/'  # use this location in linux
folder_location = ''     # use this location if windows
[times,genotypes,abundances] = [[],[],[]]

# get simulation data and store genotypes as lists since they vary in dimensions over time
data_file=open('./'+folder_location+'data/pythondata/times'+data_name+'.dat')
times = data_file.read().splitlines()
times = np.array(map(float,times))
data_file.close()

data_file=open('./'+folder_location+'data/pythondata/genotypes'+data_name+'.dat')
genotypes = data_file.read().splitlines()
data_file.close()

data_file=open('./'+folder_location+'data/pythondata/abundances'+data_name+'.dat')
abundances = data_file.read().splitlines()
data_file.close()

del data_file
num_pts = len(times)

# clean up mathematica data's format and convert loaded data into lists of arrays
for i in range(num_pts):
    genotypes[i]='genotypes[i]=np.array(['+genotypes[i].replace('\t',',')+'])'
    genotypes[i]=genotypes[i].replace('{','[')
    genotypes[i]=genotypes[i].replace('}',']')
    exec(genotypes[i])
    abundances[i]='abundances[i]=np.array([['+abundances[i].replace('\t',',')+']])'
    exec(abundances[i])

# times is array, genotypes and abundances are lists of arrays
pickle_file_name = './'+folder_location+'data/pythondata/timesGenosAbund'+data_name+'.pickle'
pickle_file = open(pickle_file_name,'wb') 
pickle.dump([times,genotypes,abundances],pickle_file,pickle.HIGHEST_PROTOCOL)
pickle_file.close()

# compute data for use in plots
rel_fit = cpy.deepcopy(genotypes)
freq = cpy.deepcopy(abundances)
mean_fit = np.zeros((num_pts,2))
fit_var = np.zeros((num_pts,2))
fit_cov = cpy.deepcopy(times)
pop_load = cpy.deepcopy(times)
dcov_dt = cpy.deepcopy(times)

#del genotypes, abundances

for i in range(num_pts):
    num_genos = len(freq[i][0])   
    freq[i] = (1/np.sum(freq[i]))*freq[i]
    mean_fit[i] = freq[i].dot(rel_fit[i])[0]
    
    rel_fit[i] = rel_fit[i]-np.array([mean_fit[i] for j in range(num_genos)])
    rel_fit[i] = rel_fit[i]*np.array([[s1,s2] for j in range(num_genos)])
    
    fit_var[i] = (freq[i].dot(((rel_fit[i])**2)))[0]
    fit_cov[i] = freq[i].dot(rel_fit[i][:,0]*rel_fit[i][:,1])
    dcov_dt[i] = freq[i].dot(rel_fit[i][:,0]**2*rel_fit[i][:,1]+rel_fit[i][:,1]**2*rel_fit[i][:,0])
    
    L1 = np.amax((rel_fit[i]+np.array([[s1,0] for j in range(num_genos)])).dot(np.array([[1],[1]])))
    L2 = np.amax((rel_fit[i]+np.array([[0,s2] for j in range(num_genos)])).dot(np.array([[1],[1]])))
    pop_load[i] = max([L1,L2])

# dump data into a pickle files
pickle_file_name = './'+folder_location+'data/pythondata/distrStats'+data_name+'.pickle'
pickle_file = open(pickle_file_name,'wb') 
pickle.dump([times,mean_fit,fit_var,fit_cov,pop_load,dcov_dt,vU_thry,v2U_thry],pickle_file,pickle.HIGHEST_PROTOCOL)
pickle_file.close()

#del N, s1, s2, U1, U2, L1, L2, rel_fit, freq
#del vU_thry, v2U_thry, tau_est
#del times, mean_fit, fit_var, fit_cov, pop_load, dcov_dt
#del pickle_file_name, folder_location, data_name