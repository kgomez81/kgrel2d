# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 13:27:18 2017
@author: Kevin Gomez (Masel Lab)
Script for plots used in "Modeling How Evolution in One Trait is Affected by Adapatation in Another"
"""

#---------------CHANGE WORKING DIRECTORY FIRST---------------------------------
#cd C://Users/dirge/Documents/kgrel2d/

from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal
from numpy import inf
import matplotlib.ticker as mtick
import pickle
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import matplotlib.mlab as mlab
import plotfunctions as pltfun


# ************************************************************************************
# ************************************************************************************
# ************************************************************************************
# --------------------Figure: 2dBulkBreakup.----------------------------------------
# ************************************************************************************
# ************************************************************************************
# ************************************************************************************

# figure 2: plot of sampled two dimensional distribution from simulated data
[N,s,U] = [1e9,1e-2,1e-5]
[sim_start,sim_end,cutoff] = [1e4,4e4,10/s]
#snapshot = [0.870e4,0.920e4,0.990e4,1.050e4,1.120e4,1.200e4]    #old mathematica data
snapshot = [0.6985e4, 0.7565e4, 0.8198e4, 0.8790e4, 0.9486e4, 1.0162e4]    #new matlab data 

# load time series data of distrStats from plotdata.py output
#pickle_file_name = './data/pythondata/timesGenosAbund_N-10p09_c1-0d01_c2-0d01_U1-1x10pn5_U2-1x10pn5_exp1.pickle'    #old mathematica data
pickle_file_name = './data/2dwave_data_time_series_distr_ml-01.pickle'
pickle_file = open(pickle_file_name,'rb') 
[times,genotypes_all,abundances_all] = pickle.load(pickle_file)
pickle_file.close()

# ------------------------------------------------------------------------------------                                   
# 2D distribution sample at time 8,700 generations

fig=plt.figure(figsize=[12,8])

ax=plt.subplot(231)
snapshot_indx = pltfun.get_sample_window(times,snapshot[0],snapshot[0])[0]
genotypes = genotypes_all[snapshot_indx]
abundances = abundances_all[snapshot_indx]  
fit_clss_width = np.max([np.max(genotypes[:,0])-np.min(genotypes[:,0])+5,np.max(genotypes[:,1])-np.min(genotypes[:,1])+5])
box_dim = [[fit_clss_width,2],[fit_clss_width,2]]
[distr_grid,class_xlabels,class_ylabels,hhf_points,stoch_points] = pltfun.get_2D_distr2(genotypes,abundances,box_dim,cutoff)
distr_grid = np.log10(N*distr_grid)
distr_grid[distr_grid == -inf] = 0
fit_distr_2d = ax.pcolormesh(distr_grid.transpose(),cmap=plt.cm.gray_r,vmin=0, vmax=9*np.log10(10))

# mark classes at the high fitness front
#ax.scatter(stoch_points[:,0],stoch_points[:,1],c="skyblue",marker="s",linewidth='0',s=140)
ax.scatter(hhf_points[:,0],hhf_points[:,1],c="None",marker="s",linewidth='1',s=150,edgecolor="dodgerblue")

# get line data for pre-high fitness front
[xl,yl] = pltfun.get_hifit_front_line(genotypes,40,box_dim)
ax.plot(xl-0.5,yl-0.5,c="black",linestyle="-")

#cbar = plt.colorbar(fit_distr_2d)
ax.axis('tight')        
ax.set_xticks(np.arange(distr_grid.shape[1])+0.5)
ax.set_yticks(np.arange(distr_grid.shape[0])+0.5)        
#ax.set_xticklabels(class_xlabels[1:],rotation=90)
#ax.set_yticklabels(class_ylabels[1:])
ax.set_xticklabels([])
ax.set_yticklabels([])
#ax.set_xlabel('Beneficial mutaitons trait 1',fontsize=24,labelpad=20)
#ax.set_ylabel('Beneficial mutaitons trait 2',fontsize=24,labelpad=10)
ax.tick_params(axis='both',labelsize=14)        
#cbar.ax.text(2.5,0.65,'Log$_{10}$ of Abundances',rotation=90,fontsize=18)
plt.annotate('t = '+str(snapshot[0]),xy=(0.1,0.05),xycoords='axes fraction',fontsize=16,color="Blue")
plt.annotate('A',xy=(0.85,0.90),xycoords='axes fraction',fontsize=16,weight='bold') 

# ---------------------------------------------------------------------------------
# 2D distribution sample at time 9,200 generations

ax=plt.subplot(232)
snapshot_indx = pltfun.get_sample_window(times,snapshot[1],snapshot[1])[0]
genotypes = genotypes_all[snapshot_indx]
abundances = abundances_all[snapshot_indx]
fit_clss_width = np.max([np.max(genotypes[:,0])-np.min(genotypes[:,0])+5,np.max(genotypes[:,1])-np.min(genotypes[:,1])+5])
box_dim = [[fit_clss_width,2],[fit_clss_width,2]]
[distr_grid,class_xlabels,class_ylabels,hhf_points,stoch_points] = pltfun.get_2D_distr2(genotypes,abundances,box_dim,cutoff)
distr_grid = np.log10(N*distr_grid)
distr_grid[distr_grid == -inf] = 0
fit_distr_2d = ax.pcolormesh(distr_grid.transpose(),cmap=plt.cm.gray_r,vmin=0, vmax=9*np.log10(10))

# mark classes at the high fitness front
#ax.scatter(stoch_points[:,0],stoch_points[:,1],c="skyblue",marker="s",linewidth='0',s=140)
ax.scatter(hhf_points[:,0],hhf_points[:,1],c="None",marker="s",linewidth='1',s=150,edgecolor="dodgerblue")

# get line data for pre-high fitness front
[xl,yl] = pltfun.get_hifit_front_line(genotypes,40,box_dim)
ax.plot(xl-0.5,yl-0.5,c="black",linestyle="-")

#cbar = plt.colorbar(fit_distr_2d)
ax.axis('tight')        
ax.set_xticks(np.arange(distr_grid.shape[1])+0.5)
ax.set_yticks(np.arange(distr_grid.shape[0])+0.5)        
#ax.set_xticklabels(class_xlabels[1:],rotation=90)
#ax.set_yticklabels(class_ylabels[1:])
ax.set_xticklabels([])
ax.set_yticklabels([])    
#ax.set_xlabel('Beneficial mutaitons trait 1',fontsize=24,labelpad=20)
#ax.set_ylabel('Beneficial mutaitons trait 2',fontsize=24,labelpad=10)
ax.tick_params(axis='both',labelsize=14)        
#cbar.ax.text(2.5,0.65,'Log$_{10}$ of Abundances',rotation=90,fontsize=18)
plt.annotate('t = '+str(snapshot[1]),xy=(0.1,0.05),xycoords='axes fraction',fontsize=16,color="green")
plt.annotate('B',xy=(0.85,0.90),xycoords='axes fraction',fontsize=16,weight='bold')

# ---------------------------------------------------------------------------------
# 2D distribution sample at time 9,900 generations

ax=plt.subplot(233)
snapshot_indx = pltfun.get_sample_window(times,snapshot[2],snapshot[2])[0]
genotypes = genotypes_all[snapshot_indx]
abundances = abundances_all[snapshot_indx]  
fit_clss_width = np.max([np.max(genotypes[:,0])-np.min(genotypes[:,0])+5,np.max(genotypes[:,1])-np.min(genotypes[:,1])+5])
box_dim = [[fit_clss_width,2],[fit_clss_width,2]]
[distr_grid,class_xlabels,class_ylabels,hhf_points,stoch_points] = pltfun.get_2D_distr2(genotypes,abundances,box_dim,cutoff)
distr_grid = np.log10(N*distr_grid)
distr_grid[distr_grid == -inf] = 0
fit_distr_2d = ax.pcolormesh(distr_grid.transpose(),cmap=plt.cm.gray_r,vmin=0, vmax=9*np.log10(10))

# mark classes at the high fitness front
#ax.scatter(stoch_points[:,0],stoch_points[:,1],c="skyblue",marker="s",linewidth='0',s=140)
ax.scatter(hhf_points[:,0],hhf_points[:,1],c="None",marker="s",linewidth='1',s=130,edgecolor="dodgerblue")

# get line data for pre-high fitness front
[xl,yl] = pltfun.get_hifit_front_line(genotypes,40,box_dim)
ax.plot(xl-0.5,yl-0.5,c="black",linestyle="-")

#cbar = plt.colorbar(fit_distr_2d)
ax.axis('tight')        
ax.set_xticks(np.arange(distr_grid.shape[1])+0.5)
ax.set_yticks(np.arange(distr_grid.shape[0])+0.5)        
#ax.set_xticklabels(class_xlabels[1:],rotation=90)
#ax.set_yticklabels(class_ylabels[1:])
ax.set_xticklabels([])
ax.set_yticklabels([])       
#ax.set_xlabel('Beneficial mutaitons trait 1',fontsize=24,labelpad=20)
#ax.set_ylabel('Beneficial mutaitons trait 2',fontsize=24,labelpad=10)
ax.tick_params(axis='both',labelsize=14)        
#cbar.ax.text(2.5,0.65,'Log$_{10}$ of Abundances',rotation=90,fontsize=18)
plt.annotate('t = '+str(snapshot[2]),xy=(0.1,0.05),xycoords='axes fraction',fontsize=16,color="red")
plt.annotate('C',xy=(0.85,0.90),xycoords='axes fraction',fontsize=16,weight='bold')

# ---------------------------------------------------------------------------------
# 2D distribution sample at time 10,500 generations

ax=plt.subplot(234)
snapshot_indx = pltfun.get_sample_window(times,snapshot[3],snapshot[3])[0]
genotypes = genotypes_all[snapshot_indx]
abundances = abundances_all[snapshot_indx]  
fit_clss_width = np.max([np.max(genotypes[:,0])-np.min(genotypes[:,0])+5,np.max(genotypes[:,1])-np.min(genotypes[:,1])+5])
box_dim = [[fit_clss_width,2],[fit_clss_width,2]]
[distr_grid,class_xlabels,class_ylabels,hhf_points,stoch_points] = pltfun.get_2D_distr2(genotypes,abundances,box_dim,cutoff)
distr_grid = np.log10(N*distr_grid)
distr_grid[distr_grid == -inf] = 0
fit_distr_2d = ax.pcolormesh(distr_grid.transpose(),cmap=plt.cm.gray_r,vmin=0, vmax=9*np.log10(10))

# mark classes at the high fitness front
#ax.scatter(stoch_points[:,0],stoch_points[:,1],c="skyblue",marker="s",linewidth='0',s=140)
ax.scatter(hhf_points[:,0],hhf_points[:,1],c="None",marker="s",linewidth='1',s=100,edgecolor="dodgerblue")

# get line data for pre-high fitness front
[xl,yl] = pltfun.get_hifit_front_line(genotypes,40,box_dim)
ax.plot(xl-0.5,yl-0.5,c="black",linestyle="-")

#cbar = plt.colorbar(fit_distr_2d)
ax.axis('tight')        
ax.set_xticks(np.arange(distr_grid.shape[1])+0.5)
ax.set_yticks(np.arange(distr_grid.shape[0])+0.5)        
#ax.set_xticklabels(class_xlabels[1:],rotation=90)
#ax.set_yticklabels(class_ylabels[1:])
ax.set_xticklabels([])
ax.set_yticklabels([])
#ax.set_xlabel('Beneficial mutaitons trait 1',fontsize=24,labelpad=20)
#ax.set_ylabel('Beneficial mutaitons trait 2',fontsize=24,labelpad=10)
ax.tick_params(axis='both',labelsize=14)        
#cbar.ax.text(2.5,0.65,'Log$_{10}$ of Abundances',rotation=90,fontsize=18)
plt.annotate('t = '+str(snapshot[3]),xy=(0.1,0.05),xycoords='axes fraction',fontsize=16,color="darkcyan")
plt.annotate('D',xy=(0.85,0.90),xycoords='axes fraction',fontsize=16,weight='bold') 

# ---------------------------------------------------------------------------------
# 2D distribution sample at time 11,200 generations
ax=plt.subplot(235)
snapshot_indx = pltfun.get_sample_window(times,snapshot[4],snapshot[4])[0]
genotypes = genotypes_all[snapshot_indx]
abundances = abundances_all[snapshot_indx]
fit_clss_width = np.max([np.max(genotypes[:,0])-np.min(genotypes[:,0])+5,np.max(genotypes[:,1])-np.min(genotypes[:,1])+5])
box_dim = [[fit_clss_width,2],[fit_clss_width,2]]
[distr_grid,class_xlabels,class_ylabels,hhf_points,stoch_points] = pltfun.get_2D_distr2(genotypes,abundances,box_dim,cutoff)
distr_grid = np.log10(N*distr_grid)
distr_grid[distr_grid == -inf] = 0
fit_distr_2d = ax.pcolormesh(distr_grid.transpose(),cmap=plt.cm.gray_r,vmin=0, vmax=9*np.log10(10))

# mark classes at the high fitness front
#ax.scatter(stoch_points[:,0],stoch_points[:,1],c="skyblue",marker="s",linewidth='0',s=140)
ax.scatter(hhf_points[:,0],hhf_points[:,1],c="None",marker="s",linewidth='1',s=90,edgecolor="dodgerblue")

# get line data for pre-high fitness front
[xl,yl] = pltfun.get_hifit_front_line(genotypes,40,box_dim)
ax.plot(xl-0.5,yl-0.5,c="black",linestyle="-")

#cbar = plt.colorbar(fit_distr_2d)
ax.axis('tight')        
ax.set_xticks(np.arange(distr_grid.shape[1])+0.5)
ax.set_yticks(np.arange(distr_grid.shape[0])+0.5)        
#ax.set_xticklabels(class_xlabels[1:],rotation=90)
#ax.set_yticklabels(class_ylabels[1:])
ax.set_xticklabels([])
ax.set_yticklabels([])    
#ax.set_xlabel('Beneficial mutaitons trait 1',fontsize=24,labelpad=20)
#ax.set_ylabel('Beneficial mutaitons trait 2',fontsize=24,labelpad=10)
ax.tick_params(axis='both',labelsize=14)        
#cbar.ax.text(2.5,0.65,'Log$_{10}$ of Abundances',rotation=90,fontsize=18)
plt.annotate('t = '+str(snapshot[4]),xy=(0.1,0.05),xycoords='axes fraction',fontsize=16,color="magenta")
plt.annotate('E',xy=(0.85,0.90),xycoords='axes fraction',fontsize=16,weight='bold')

# ---------------------------------------------------------------------------------
# 2D distribution sample at time 12,000 generations
ax=plt.subplot(236)
snapshot_indx = pltfun.get_sample_window(times,snapshot[5],snapshot[5])[0]
genotypes = genotypes_all[snapshot_indx]
abundances = abundances_all[snapshot_indx]  
fit_clss_width = np.max([np.max(genotypes[:,0])-np.min(genotypes[:,0])+5,np.max(genotypes[:,1])-np.min(genotypes[:,1])+5])
box_dim = [[fit_clss_width,2],[fit_clss_width,2]]
[distr_grid,class_xlabels,class_ylabels,hhf_points,stoch_points] = pltfun.get_2D_distr2(genotypes,abundances,box_dim,cutoff)
distr_grid = np.log10(N*distr_grid)
distr_grid[distr_grid == -inf] = 0
fit_distr_2d = ax.pcolormesh(distr_grid.transpose(),cmap=plt.cm.gray_r,vmin=0, vmax=9*np.log10(10))

# mark classes at the high fitness front
#ax.scatter(stoch_points[:,0],stoch_points[:,1],c="skyblue",marker="s",linewidth='0',s=140)
ax.scatter(hhf_points[:,0],hhf_points[:,1],c="None",marker="s",linewidth='1',s=120,edgecolor="dodgerblue")

# get line data for pre-high fitness front
[xl,yl] = pltfun.get_hifit_front_line(genotypes,40,box_dim)
ax.plot(xl-0.5,yl-0.5,c="black",linestyle="-")

#cbar = plt.colorbar(fit_distr_2d)
ax.axis('tight')        
ax.set_xticks(np.arange(distr_grid.shape[1])+0.5)
ax.set_yticks(np.arange(distr_grid.shape[0])+0.5)        
#ax.set_xticklabels(class_xlabels[1:],rotation=90)
#ax.set_yticklabels(class_ylabels[1:])
ax.set_xticklabels([])
ax.set_yticklabels([])       
#ax.set_xlabel('Beneficial mutaitons trait 1',fontsize=24,labelpad=20)
#ax.set_ylabel('Beneficial mutaitons trait 2',fontsize=24,labelpad=10)
ax.tick_params(axis='both',labelsize=14)        
#cbar.ax.text(2.5,0.65,'Log$_{10}$ of Abundances',rotation=90,fontsize=18)
plt.annotate('t = '+str(snapshot[5]),xy=(0.1,0.05),xycoords='axes fraction',fontsize=16,color="darkorange")
plt.annotate('F',xy=(0.85,0.90),xycoords='axes fraction',fontsize=16,weight='bold')

#------------------------------------------------------------------------------------

fig.text(0.51, 0.02, 'Beneficial mutations trait 1', ha='center', va='center',fontsize=14)
fig.text(0.1, 0.5, 'Beneficial mutations trait 2', ha='center', va='center', rotation='vertical',fontsize=14)
fig.text(0.95, 0.5, 'Log10 of abundances', ha='center', va='center', rotation='vertical',fontsize=14)
fig.subplots_adjust(right=0.89)
cbar_ax = fig.add_axes([0.90, 0.10, 0.02, 0.8])
fig.colorbar(fit_distr_2d, cax=cbar_ax)

fig.subplots_adjust(wspace=0.05)
#fig.subplots_adjust(bottom=0.25)
#plt.tight_layout()

#fig.savefig('./figures/2dBulkBreakup.pdf',bbox_inches='tight')      #old mathematica data
fig.savefig('./figures/2dBulkBreakup-updated.pdf',bbox_inches='tight')

