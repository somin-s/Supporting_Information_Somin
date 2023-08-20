import mdtraj as md
import matplotlib.pyplot as plt
import numpy as np

traj = md.load('MD_QMMM_withoutAB.dcd', top='system_withoutAB.pdb')

ALA380 = traj.topology.select('resid 379 to 379')
LYS384 = traj.topology.select('resid 382 to 382')
ASP385 = traj.topology.select('resid 384 to 384')
LYS530 = traj.topology.select('resid 528 to 528')
GLY574 = traj.topology.select('resid 573 to 573')
SER576 = traj.topology.select('resid 575 to 575')
LYS858 = traj.topology.select('resid 857 to 857')

_ALA380 = traj.atom_slice(ALA380)
_LYS384 = traj.atom_slice(LYS384)
_ASP385 = traj.atom_slice(ASP385)
_LYS530 = traj.atom_slice(LYS530)
_GLY574 = traj.atom_slice(GLY574)
_SER576 = traj.atom_slice(SER576)
_LYS858 = traj.atom_slice(LYS858)

rmsf_ALA380 = md.rmsf(_ALA380, _ALA380, 0)
rmsf_LYS384 = md.rmsf(_LYS384, _LYS384, 0)
rmsf_ASP385 = md.rmsf(_ASP385, _ASP385, 0)
rmsf_LYS530 = md.rmsf(_LYS530, _LYS530, 0)
rmsf_GLY574 = md.rmsf(_GLY574, _GLY574, 0)
rmsf_SER576 = md.rmsf(_SER576, _SER576, 0)
rmsf_LYS858 = md.rmsf(_LYS858, _LYS858, 0)

names = ['ALA380','LYS384','ASP385','LYS530', 'GLY574', 'SER576', 'LYS858']

data = [rmsf_ALA380, rmsf_LYS384, rmsf_ASP385, rmsf_LYS530, rmsf_GLY574, rmsf_SER576, rmsf_LYS858]
plt.boxplot(data, labels = names)


plt.xlabel("ATP-IDE_Residues", fontweight='normal', fontsize=14)
plt.ylabel("RMSF ($\AA$)", fontweight='normal', fontsize=14)
