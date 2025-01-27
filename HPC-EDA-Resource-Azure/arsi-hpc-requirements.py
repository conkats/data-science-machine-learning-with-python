import matplotlib.pyplot as plt
import numpy as np

# ARSIS HPC requirements

### RAM vs Cores per job
# Data from the table
users = ["Constantinos (PB)", "Constantinos (EPR)", "Ehimen (SB)", "Ewan (GV)", "Raheeg (GB)", "Assia (GB)"]
cores = [30, 164, 28, 264, 20, 20]  # Approximated from given ranges
ram = [4.5, 4.5, 4.5, 4.5, 150, 100]  # Approximated from given ranges

x = np.arange(len(users))  # Label locations

# Setting larger font sizes for readability
plt.rcParams.update({'font.size': 14})  # Increase font size globally

fig, ax1 = plt.subplots(figsize=(12, 8))  # Larger figure size for readability

# Plotting Cores on the first y-axis
ax1.bar(x - 0.2, cores, width=0.4, color='blue', label='Cores')
ax1.set_xlabel('Users', fontsize=16)
ax1.set_ylabel('Cores', color='k', fontsize=16)
ax1.set_xticks(x)
ax1.set_xticklabels(users, rotation=45, ha='right', fontsize=14)
ax1.tick_params(axis='y', labelcolor='k')

# Creating a second y-axis for RAM
ax2 = ax1.twinx()
ax2.bar(x + 0.2, ram, width=0.4, color='g', label='RAM (GB)')
ax2.set_ylabel('RAM (GB)', color='k', fontsize=16)
ax2.tick_params(axis='y', labelcolor='k')

# Adding a legend with larger font size
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes, fontsize=14)

# Setting the title with a larger font size
plt.title("Cores and RAM for Each User", fontsize=18)
plt.tight_layout()
plt.savefig("arsi-team-hpc-requirements.png", dpi=150)

##########################################################
###Wallclock against number of jobs per User
# Data from the table
wallclock_days = [1, 7, 1, 7, 3.5, 3.5]  # Wallclock time per job in days
jobs_per_month = [20, 20, 20, 20, 14, 14]  # Number of jobs per month

x = np.arange(len(users))  # Label locations

# Setting larger font sizes for readability
plt.rcParams.update({'font.size': 14})  # Increase font size globally

fig, ax1 = plt.subplots(figsize=(12, 8))  # Larger figure size for readability

# Plotting Wallclock time on the first y-axis
ax1.bar(x - 0.2, wallclock_days, width=0.4, color='cornflowerblue', label='Wallclock Time (days)')
ax1.set_xlabel('Users', fontsize=16)
ax1.set_ylabel('Wallclock Time (days)', color='k', fontsize=16)
ax1.set_xticks(x)
ax1.set_xticklabels(users, rotation=45, ha='right', fontsize=14)
ax1.tick_params(axis='y', labelcolor='k')

# Creating a second y-axis for Jobs per month
ax2 = ax1.twinx()
ax2.bar(x + 0.2, jobs_per_month, width=0.4, color='orange', label='Jobs per Month')
ax2.set_ylabel('Jobs per Month', color='k', fontsize=16)
ax2.tick_params(axis='y', labelcolor='k')

# Adding a legend with larger font size
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes, fontsize=14)

# Setting the title with a larger font size
plt.title("Wallclock Time and Jobs per Month for Each User", fontsize=18)
plt.tight_layout()
plt.savefig("wallclock_jobs_per_user.png", dpi=150)
