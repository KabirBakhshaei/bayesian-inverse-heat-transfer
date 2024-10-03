#⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬ Please read before running

# Plotting reconstructed mean temperature and true temperature at a specific probe(0.91, 0.02 , 0.55) over time with confidence interval.
# Plotting reconstructed mean heat flux and true heat flux at a specific probe (0.91, 0.0 , 0.55) on the hotside boundary condition.
# Plotting reconstructed mean heat flux and true heat flux at the entire hotSide BC over time.
# Plotting reconstructed mean heat flux and true heat flux at the entire hotSide BC over time with confidence interval
# Plotting some errors for Method Evaluation
# Calculating and printing the mean and standard deviation of "condNumberAutoCovInverse.txt," "condNumberCrossCov.txt," and "condNumberKalmanGain.txt,"
    
# If you change the location of probes both for temperature and hotside BC inside 06enKFwDF_3dIHTP.C, please modify their related comments of those probes inside this code.
        ##Probe [temperature]= (0.91, 0.02 , 0.55)      # Please see setProbe variable              in the 06enKFwDF_3dIHTP.C to adjust
        ##Probe [heat flux]  = (0.91, 0.0 , 0.55)       # Please see hotSide_probeLocation variable in the 06enKFwDF_3dIHTP.C to adjust
        
#⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫ Please read before running

import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np
import sys
import seaborn as sns
sys.path.insert(0, "./")

plt.rc('font', family='Times New Roman', size=18)                               # You can adjust the font size (14 in this case) as needed
plt.figure(figsize=(10, 6))                                                     # You can adjust the figure size as needed
colors = sns.color_palette('deep', n_colors=2)

#plt.style.use('classic')
#params = {'legend.fontsize': 'x-large','figure.figsize': (10, 8), 'axes.labelsize': 'x-large', 'axes.titlesize':'x-large', 'xtick.labelsize':'x-large','ytick.labelsize':'x-large'}
#pylab.rcParams.update(params)

#time = np.loadtxt("./ITHACAoutput/true/trueTimeVec_mat.txt")                                  # 100, Loading time vector [100 equal to the number of time steps]
time = np.loadtxt("/u/k/kbakhsha/ITHACA-FV-KF/tutorials/UQ/07enKFwDF_3dIHTP/ITHACAoutput/true/trueTimeVec_mat.txt")                                  # 100, Loading time vector [100 equal to the number of time steps]

#⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬ Plotting reconstructed mean temperature and true temperature at a specific probe(0.91, 0.02 , 0.55) over time.
probe_true = np.loadtxt("./ITHACAoutput/true/probe_true_mat.txt")                             # Column Vector(100), Reading true temprature [100 equal to the number of time instants] file at the probe  
probe_rec =  np.loadtxt("./ITHACAoutput/reconstruction/probe_rec_mat.txt")                    # Column Vector(100), Reading reconstructed mean[100 equal to the number of time steps] temprature file at the probe 
state_min =  np.loadtxt("./ITHACAoutput/reconstruction/probeState_minConf_mat.txt")           # Column Vector(100), Reading the 5th percentile value of state ensemble at different time steps 
state_max =  np.loadtxt("./ITHACAoutput/reconstruction/probeState_maxConf_mat.txt")           # Column Vector(100), Reading the 95th  percentile value of state ensemble at different time steps 

print("Size of probe_rec array:", probe_rec.shape) # It must be equal to the number of time steps 
print("Size of state_min array:", state_min.shape) # It must be equal to the number of time steps 
print("Size of state_max array:", state_max.shape) # It must be equal to the number of time steps 
print('Size of trueTimeVec_mat array:', time)
print('Size of trueTimeVec_mat array:', time.shape)

#fig = plt.figure(1,figsize=(10,6))
fig = plt.figure()
fig.canvas.manager.window.showMaximized()

#plt.plot(time, probe_true,"b", linewidth = 2, label="Ttrue Probe")
#plt.plot(time, probe_rec, linewidth=2, color='k', linestyle='--', label='Trec Probe')
plt.plot(time, probe_true, color=colors[0], label='Ttrue Probe', linewidth=2, marker='D', markersize=3, markevery=5)
plt.plot(time, probe_rec,  color=colors[1], label='Trec Probe',  linewidth=2, marker='s', markersize=3, markevery=5)

# Using plt.fill_between to visualize uncertainty or confidence intervals in the state values by filling the area between state_min and  state_max curves representing the 5th and 95th percentile values of the state ensemble at different time steps, respectively.
plt.fill_between(time, state_min, state_max, color='b', alpha=.1, label='Confidence Interval') # Fill the area between state_min and state_max with a specified color and transparency.
#plt.fill_between(time, state_min, state_max, color=colors[0], label='Confidence Interval', alpha=.1)

# Set labels and title
plt.grid(True)
plt.legend(loc='upper left', prop={'size': 10})
ax = plt.gca()
ax.spines['bottom'].set_linewidth(2)                                           # X-axis line width
ax.spines['left'].set_linewidth(2)                                             # Y-axis line width
plt.xlabel('Time [s]', fontsize=20, weight='bold')
plt.ylabel('T [K]', fontsize=20, weight='bold')
plt.xlim(0, 20)                                                                 # X-axis range from 0 to 20
#plt.title('True and Reconstructed Mean Temperature at a Probe(0.91, 0.02 , 0.55) over time.')
# Save the main plot
plt.savefig('TrueAndReconstructedMeanTemperatureAtaProbe_0.91_0.02_0.55_OverTime.png', dpi=400, bbox_inches='tight')
plt.show()

# Your existing code...
# Create inset_axes
axin = ax.inset_axes([0.6, 0.7, 0.25, 0.25])  # Adjust position and size as needed

# Plot reconstructed mean on inset_axes
axin.plot(time, probe_rec, color=colors[1], label='Trec Probe',  linewidth=2, marker='s', markersize=3, markevery=5)
axin.plot(time, probe_true,color=colors[0], label='Ttrue Probe', linewidth=2, marker='D', markersize=3, markevery=5)
axin.fill_between(time, state_min, state_max, color='b', alpha=.1, label='Confidence Interval')

# Set x-axis and y-axis limits for inset_axes
axin.set_xlim(11, 14)  # Set x-axis limits to [11, 14]
axin.set_ylim(315, 335)  # Set y-axis limits to [315, 335]

# Add labels and title for inset_axes
axin.set_xlabel('Time [s]', fontsize=8, weight='bold')
axin.set_ylabel('T [K]', fontsize=8, weight='bold')
axin.set_title('Zoomed-in View', fontsize=8, weight='bold')

# Change the size of tick labels for both x-axis and y-axis
axin.tick_params(axis='both', labelsize=8)  # Adjust labelsize as needed

# Embed axin in the main plot
ax.indicate_inset_zoom(axin)

# Save the figure with zoomed-in view
plt.savefig('TrueAndReconstructedMeanTemperatureWithZoom_0.91_0.02_0.55.png', dpi=400, bbox_inches='tight')
# Your existing code...


plt.show()
#⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫ Plotting reconstructed mean temperature and true temperature at a specific probe(0.91, 0.02 , 0.55) over time.

#⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬ Plotting reconstructed mean heat flux and true heat flux at a specific probe (0.91, 0.0 , 0.55) on the hotside boundary condition.
gTrue_probe = np.loadtxt("./ITHACAoutput/reconstruction/gTrue_probe_mat.txt")               # 100, Reading the true heat flux file at the probe
gRec_probe = np.loadtxt("./ITHACAoutput/reconstruction/gRec_probe_mat.txt")                 # 100, Reading the reconstructed mean heat flux at the probe
gRec_probeMaxConf = np.loadtxt("./ITHACAoutput/reconstruction/gRec_probeMaxConf_mat.txt")   # 100, Reading the reconstructed MaxConf heat flux at the probe
gRec_probeMinConf = np.loadtxt("./ITHACAoutput/reconstruction/gRec_probeMinConf_mat.txt")   # 100, Reading the reconstructed MinConf heat flux at the probe

#fig = plt.figure(3,figsize=(10,6))
fig = plt.figure()
fig.canvas.manager.window.showMaximized()

#plt.plot(time, gTrue_probe,      linewidth = 2, color='b', label="gTrue Probe" )
#plt.plot(time, gRec_probe,"k--", linewidth = 2, label="gRec Probe")
plt.plot(time, gTrue_probe, color=colors[0], label='gTrue Probe', linewidth=2, marker='D', markersize=3, markevery=5)
plt.plot(time, gRec_probe,  color=colors[1], label='gRec Probe',  linewidth=2, marker='s', markersize=3, markevery=5)

# Using plt.fill_between to visualize uncertainty or confidence intervals in the heatflux values by filling the area between heat flux min confidence of the probe and  heat flux max confidence of the probe curves representing the 5th and 95th percentile values of the heat flux parameter ensemble at different time steps, respectively.
plt.fill_between(time, gRec_probeMinConf, gRec_probeMaxConf , color='b', alpha=.1, label='Confidence Interval')
plt.grid(True)
plt.legend(loc='upper left', prop={'size': 10})
ax = plt.gca()
ax.spines['bottom'].set_linewidth(2)                                           # X-axis line width
ax.spines['left'].set_linewidth(2)                                             # Y-axis line width

plt.xlabel('Time [s]', fontsize=20, weight='bold')
#plt.ylabel('Heat Flux[w/m^2]', fontsize=25)
plt.ylabel(r'Heat Flux [$\mathbf{W/m^2}$]', fontsize=20, weight='bold')
plt.xlim(0, 20)                                                                
#plt.ylim(-500, -0.001) 
#plt.title('True and Reconstructed Mean Heat Flux at a Probe(0.91, 0.0 , 0.55) over time')
plt.savefig('TrueAndReconstructedMeanHeatFluxAtProbe_0.91_0.0_0.55_over_time.png', dpi=400, bbox_inches='tight')
plt.show()
#⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫ Plotting reconstructed mean heat flux and true heat flux at a specific probe (0.91, 0.0 , 0.55) on the hotside boundary condition.


#⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬ Plotting reconstructed mean heat flux and true heat flux at the entire hotSide BC over time.
# The total heat flux on the hot side is not a really good quantity. Because maybe on the corner, there are some places where we get very bad.
   # Would be better to have a MSE or realtive error plot.
parameterMean  =   np.loadtxt("./ITHACAoutput/reconstruction/parameterMean_mat.txt")                         # parameterMean_mat[25(mean weight),100(timesteps)] stores the reconstructed mean weight
heatFluxSpaceRBF = np.loadtxt("./ITHACAoutput/projection/HeatFluxSpaceRBF/heat_flux_space_basis_mat.txt")  # This matrix[25(RBF),400(faces)] stores heatFluxSpaceBasis data

parameterPriorMeanWithoutShifting = np.load('parameterPriorMeanWithoutShifting.npy')     # 5
parameterPriorMean = np.load('parameterPriorMean.npy')                                   # 5

# RBFs must be less than measurements or at least are equal to measurements
# By using RBF formula with the help of two above matrix, we create a matrix named out(100,400) containing the reconstructed heat flux for each face at each time step.

n1, m1 = parameterMean.shape      # n1 = 25(mean/weight), m1=100(times)
n, m   = heatFluxSpaceRBF.shape   # n = 25(RBF),          m=400(faces)

out = np.zeros((m1, m))                                         #(100,400)
outVectorAtTimeZeroWithoutShifting = np.zeros((1, m))           #(1,400)
outVectorAtTimeZeroWithShifting    = np.zeros((1, m))              #(1,400)

for j in range(m):
    outVectorAtTimeZeroWithoutShifting[0,j]= np.sum(parameterPriorMeanWithoutShifting[:,0]*heatFluxSpaceRBF[:, j])
    outVectorAtTimeZeroWithShifting[0,j]   = np.sum(parameterPriorMean[:,0]*heatFluxSpaceRBF[:, j])
outVectorAtTimeZeroWithoutShifting = np.transpose(outVectorAtTimeZeroWithoutShifting)           # This matrix out [400(faces), 1(t =0)]
outVectorAtTimeZeroWithShifting    = np.transpose(outVectorAtTimeZeroWithShifting)              # This matrix out [400(faces), 1(t =0)]


for i in range(m1):               #m1=100(times)
    for j in range(m):            #m=400(faces)
        out[i, j] = np.sum(parameterMean[:, i] * heatFluxSpaceRBF[:, j])            # This matrix out [100(timesteps), 400(faces)]
# out is the reconstructed heat flux matrix
out = np.transpose(out)           # This matrix out [400(faces), 100(timesteps)]
column_sums2 = out.sum(axis=0)    # [1,100] Integral or sum each column of the matrix out. Therefore, each element of the resulted row vector represents the total recunstructed heat flux at the hotSide BC at each time step

# trueBC = np.loadtxt("./ITHACAoutput/true/trueBC_mat.txt")                           # Why this vector is empty?
gTrue = np.loadtxt("./ITHACAoutput/projection/TrueHeatFlux/HeatFluxTrue_mat.txt")     # This matrix[100,400]
gTrue = np.transpose(gTrue)#  gTrue [400(faces), 101(timesteps)]
column_sums1 = gTrue.sum(axis=0)  # [1,101] Integral or sum of each column of the matrix gTrue. Therefore, each element of the resulted row vector represents the true heat flux at the hotSide BC at each time step

#fig = plt.figure(2,figsize=(10,6))
fig = plt.figure()
fig.canvas.manager.window.showMaximized()

#plt.plot(time, column_sums1[:-1],"b", linewidth = 2, label="True Heat Flux")
#plt.plot(time, column_sums2, "k--" ,  linewidth = 2, label="Reconstructed Heat Flux")
plt.plot(time, column_sums1[:-1],  color=colors[0], label='True Heat Flux',            linewidth=2, marker='D', markersize=3, markevery=5)
plt.plot(time, column_sums2,       color=colors[1], label='Reconstructed Heat Flux',   linewidth=2, marker='s', markersize=3, markevery=5)

plt.grid(True)
plt.legend(loc='upper left', prop={'size': 10})
ax.spines['bottom'].set_linewidth(2)                                           # X-axis line width
ax.spines['left'].set_linewidth(2)                                             # Y-axis line width

plt.xlabel('Time [s]', fontsize=20, weight='bold')
plt.ylabel(r'Heat Flux [$\mathbf{W/m^2}$]', fontsize=20, weight='bold')
plt.xlim(0, 20)   
#plt.title('True and Reconstructed Mean Heat Flux at the hotSide.')
plt.savefig('TrueAndReconstructedMeanHeatFluxAtTheHotSide.png', dpi=400, bbox_inches='tight')
plt.show()


param_min = np.loadtxt("./ITHACAoutput/reconstruction/parameter_minConf_mat.txt")     # [25(5th of each ensemble weight), 100(timesteps)]  stores the 5th  percentile value of the parameter(weight) ensemble at different time steps
param_max = np.loadtxt("./ITHACAoutput/reconstruction/parameter_maxConf_mat.txt")     # [25(95th of each ensemble weight),100(timesteps)]  stores the 95th percentile value of the parameter(weight) ensemble at different time steps

# no need these two lines
param_min_vector = param_min.sum(axis=0)  #[1,100] Sum each column of the param_min matrix. Therefore, each element of the resulted vector represents the total 5th  percentile value of the parameter(weight)ensemble at the hotSide BC at each time step
param_max_vector = param_max.sum(axis=0)  #[1,100] Sum each column of the param_min matrix. Therefore, each element of the resulted vector represents the total 95th  percentile value of the parameter(weight) ensemble at the hotSide BC at each time step
# no need these two lines

out1 = np.zeros((m1, m))    #(100,400)
out2 = np.zeros((m1, m))    #(100,400)

for i in range(m1):         #m1=100(times)
    for j in range(m):      #m=400(faces)
        out1[i, j] = np.sum(param_min[:, i] * heatFluxSpaceRBF[:, j])                 # This matrix[100(timesteps), 400(heat flux min confidence)]
        out2[i, j] = np.sum(param_max[:, i] * heatFluxSpaceRBF[:, j])                 # This matrix[100(timesteps), 400(heat flux min confidence)]
out1 = np.transpose(out1) #[400(heat flux min confidence), 100(timesteps)]
out2 = np.transpose(out2) #[400(heat flux min confidence), 100(timesteps)]
column_sums3 = out1.sum(axis=0) # [1,100]Sum of each column of the matrix out1. Therefore, each element of the resulted vector represents the total heat flux min confidence (5th)  at the hotSide BC at each time step
column_sums4 = out2.sum(axis=0) # [1,100]Sum of each column of the matrix out2. Therefore, each element of the resulted vector represents the total heat flux max confidence (95th) at the hotSide BC at each time step


#fig = plt.figure(4,figsize=(10,6))
fig = plt.figure()
fig.canvas.manager.window.showMaximized()

#plt.plot(time, column_sums1[1:],"b", linewidth = 2, label="True Heat Flux")
#plt.plot(time, column_sums2, "k--" , linewidth = 2, label="Reconstructed Heat Flux")
plt.plot(time, column_sums1[1:], color=colors[0], label='True Heat Flux',            linewidth=2, marker='D', markersize=3, markevery=5)
plt.plot(time, column_sums2,     color=colors[1], label='Reconstructed Heat Flux',   linewidth=2, marker='s', markersize=3, markevery=5)

# Using plt.fill_between to visualize uncertainty or confidence intervals in the heatflux values by filling the area between heat flux min confidence and  heat flux max confidence curves representing the 5th and 95th percentile values of the heat flux parameter ensemble at different time steps, respectively.
plt.fill_between(time, column_sums3, column_sums4 , color='b', alpha=.1, label='Confidence Interval')

#minConfidence = np.loadtxt("./ITHACAoutput/reconstuction/probe_minConfidence_mat.txt")   # not available
#maxConfidence = np.loadtxt("./ITHACAoutput/reconstuction/probe_MaxConfidence_mat.txt")   # not available

#for i in range(reconstructedBC.shape[0]):                                                # not required
    #plt.plot(time, reconstructedBC[i,:])

    
    
#plt.fill_between(time, minConfidence, maxConfidence, color='b', alpha=.1)                # not available

# Using plt.fill_between to visualize uncertainty or confidence intervals in the parameter values by filling the area between param_min and  param_max curves representing the 5th and 95th percentile values of the parameter ensemble at different time steps, respectively.
#plt.fill_between(time, param_min_vector, param_max_vector, color='b', alpha=.1, label='Confidence Interval') # Fill the area between param_min and param_max with a specified color and transparency.

plt.grid(True)
plt.legend(loc='upper left', prop={'size': 10})
ax.spines['bottom'].set_linewidth(2)                                           # X-axis line width
ax.spines['left'].set_linewidth(2)                                             # Y-axis line width

plt.xlabel('Time [s]', fontsize=20, weight='bold')
plt.ylabel(r'Heat Flux [$\mathbf{W/m^2}$]', fontsize=20, weight='bold')
plt.xlim(0, 20)   
#plt.title('True and Reconstructed Mean Heat Flux at the hotSide with Confidence Interval.')
plt.savefig('TrueAndReconstructedMeanHeatFluxAtTheHotSideWithConfidenceInterval.png', dpi=400, bbox_inches='tight')
plt.show()
#⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫ Plotting reconstructed mean heat flux and true heat flux at the hotSide BC over time.

#⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬ Plotting the MSE, MAE, mean and sum relative error of the reconstructed heat flux compared to the true heat flux over time.

# The total heat flux on the hot side is not a really good quantity. Because maybe on the corner, there are some places where we get very bad.
   # Would be better to have a MSE or realtive error plot.
# out   = reconstructed heat flux  [400(faces), 100(timesteps)]
# gTrue =  true heat flux          [400(faces), 101(timesteps)]
# time  100 time steps
gTrue = gTrue[:, :-1]  # Remove the last time step from gTrue

relative_error = np.abs((gTrue - out) / gTrue) * 100                           # Calculate the relative error
mean_relative_error = np.mean(relative_error, axis=0)                          # Calculate the mean relative error across all faces at each time step
sum_relative_error = np.sum(relative_error, axis=0)                            # Calculate the sum of relative errors across all faces for each time step


mean_relative_error_at_t0_WithoutShifting = np.abs((gTrue[:,0]-outVectorAtTimeZeroWithoutShifting)/gTrue[:,0]) *100
mean_relative_error_at_t0_WithoutShifting = np.mean(mean_relative_error_at_t0_WithoutShifting)

mean_relative_error_at_t0_WithShifting = np.abs((gTrue[:,0]-outVectorAtTimeZeroWithShifting)/gTrue[:,0]) *100
mean_relative_error_at_t0_WithShifting = np.mean(mean_relative_error_at_t0_WithShifting)

# MSE values represent the average squared error in its typical form (in its original data and not as a percentage)between predicted values (out) and actual values (gTrue)
 # without applying any additional normalization or scaling.
mse = np.mean(((out - gTrue) ** 2)/(out.shape[0]*out.shape[1]), axis=0)        # from sklearn.metrics import mean_squared_error       mse = mean_squared_error(gTrue, out, multioutput='raw_values')    Incorrect
mae = np.mean(np.abs(out - gTrue), axis=0)*100                                 #from sklearn.metrics import mean_absolute_error       mae = mean_absolute_error(gTrue, out, multioutput='raw_values') 

# Export mean of the relative error over space and then over time to a text file
mean_of_mean_relative_error = np.mean(mean_relative_error)                     
# Define the filename
filename = "meanOfMeanRelativeError.txt"
with open(filename, "w") as file:
    file.write(f"Mean of Mean Relative Error: {mean_of_mean_relative_error}")

# Export the mean relative error at t=0 with Shifting Weight Factor  to a text file
filename = "meanRelativeErrorAtT0.txt"
with open(filename, "w") as file:
    file.write(f"Mean Relative Error at t=0 withShifting: {mean_relative_error_at_t0_WithShifting:.2f}%")

# Export the mean relative error at t=0 without shifting to a text file
filename = "meanRelativeErrorAtT0WithoutShifting.txt"
with open(filename, "w") as file:
    file.write(f"Mean Relative Error at t=0 without shifting: {mean_relative_error_at_t0_WithoutShifting:.2f}%")


#Plot the mean relative error over time, 
#fig = plt.figure(5,figsize=(10,6))
fig = plt.figure()
fig.canvas.manager.window.showMaximized()
#plt.plot(time, mean_relative_error, marker='o', linestyle='-')
plt.plot(time, mean_relative_error,  color=colors[0], linewidth=2, marker='D', markersize=3, markevery=5)

plt.grid(True)
ax.spines['bottom'].set_linewidth(2)                                           # X-axis line width
ax.spines['left'].set_linewidth(2)                                             # Y-axis line width
plt.xlabel('Time [s]', fontsize=20, weight='bold')
plt.ylabel('Mean Relative Error (%)', fontsize=20, weight='bold')
plt.xlim(0, 20)  
#plt.title('Mean Relative Error Over Time')
plt.savefig('MeanRelativeErrorOverTime.png', dpi=400, bbox_inches='tight')
plt.show()

#Plot the mean relative error over time, log scale
# fig = plt.figure(6, figsize=(10, 8))
# plt.plot(time, mean_relative_error, marker='o', linestyle='-')
# plt.title('Mean Relative Error Over Time- log scale')
# plt.xlabel('Time Step')
# plt.ylabel('Mean Relative Error (%)- log scale')
# plt.ylim(1, 100)                                                                # limit the range from 1 to 100
# plt.yscale('log')                                                               # Set the vertical axis to log scale
# plt.grid(True) 
# plt.show()


# Plot the sum relative error over time
# fig = plt.figure(7,figsize=(10,8))
# plt.plot(time, sum_relative_error, marker='o', linestyle='-')
# plt.xlabel('Time Step')
# plt.ylabel('Sum Relative Error (%)')
# plt.title('Sum Relative Error Over Time')
# plt.grid(True)
# plt.show()


# Plot Mean Squared Error (MSE) over time
#fig = plt.figure(8, figsize=(10, 6))
fig = plt.figure()
fig.canvas.manager.window.showMaximized()
#plt.plot(time, mse, marker='o', linestyle='-')
plt.plot(time, mse,  color=colors[0], linewidth=2, marker='D', markersize=3, markevery=5)

plt.grid(True)
ax.spines['bottom'].set_linewidth(2)                                           # X-axis line width
ax.spines['left'].set_linewidth(2)                                             # Y-axis line width
plt.xlabel('Time [s]', fontsize=20, weight='bold')
plt.ylabel('MSE', fontsize=20, weight='bold')
plt.xlim(0, 20)  
#plt.title('Mean Squared Error (MSE) Over Time')
plt.savefig('MeanSquaredError.png', dpi=400, bbox_inches='tight')
plt.show()


# Plot Mean Absolute Error (MAE) over time
# fig = plt.figure(9, figsize=(10, 8))
# plt.plot(time, mae, marker='o', linestyle='-')
# plt.title('Mean Absolute Error (MAE) Over Time')
# plt.xlabel('Time Step')
# plt.ylabel('MAE (%)')
# plt.grid(True)
# plt.show()
#⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫ Plotting the MSE, MAE, mean and sum relative error of the reconstructed heat flux compared to the true heat flux over time.

#⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫ Calculating and printing the mean and standard deviation of "condNumberAutoCovInverse.txt," "condNumberCrossCov.txt," and "condNumberKalmanGain.txt,"
# Load data from the text files
autoCovInverse_data = np.loadtxt("condNumberAutoCovInverse.txt")
crossCov_data = np.loadtxt("condNumberCrossCov.txt")
kalmanGain_data = np.loadtxt("condNumberKalmanGain.txt")

# Calculate the mean and standard deviation for each column
autoCovInverse_mean = np.mean(autoCovInverse_data, axis=0)
autoCovInverse_std = np.std(autoCovInverse_data, axis=0)

crossCov_mean = np.mean(crossCov_data, axis=0)
crossCov_std = np.std(crossCov_data, axis=0)

kalmanGain_mean = np.mean(kalmanGain_data, axis=0)
kalmanGain_std = np.std(kalmanGain_data, axis=0)


filename = "autoCovInverse_mean_std.txt"
with open(filename, "w") as file:
    file.write(f"autoCovInverse_mean: {autoCovInverse_mean}\n")
    file.write(f"autoCovInverse_std: {autoCovInverse_std}\n")
    
filename = "crossCov_mean_std.txt"
with open(filename, "w") as file:
    file.write(f"crossCov_mean: {crossCov_mean}\n")
    file.write(f"crossCov_std: {crossCov_std}\n")

filename = "kalmanGain_mean_std.txt"
with open(filename, "w") as file:
    file.write(f"kalmanGain_mean: {kalmanGain_mean}\n")
    file.write(f"kalmanGain_std: {kalmanGain_std}\n")

#⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫ Calculating and printing the mean and standard deviation of "condNumberAutoCovInverse.txt," "condNumberCrossCov.txt," and "condNumberKalmanGain.txt,"