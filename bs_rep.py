

#import numpy and pandas packages in order to read in file and complete tasks
import numpy as np
import pandas as pd

#Read in data and assign to variable: fish_data
fish_data = pd.read_csv('gandhi_et_al_bouts.csv', skiprows=4)

#Assign bout_lengths columns from fish data to releveant genotype Wild Type and Mutant
bout_lengths_wt = fish_data[fish_data.genotype == 'wt'].bout_length
bout_lengths_mut = fish_data[fish_data.genotype == 'mut'].bout_length

#Use main guard when creating bootstrap function 
if __name__ == '__main__':
    #Create function with relevant arguments including, data, function and sample size
    def draw_bs_reps(data, func, size=1):
        """Generate bootstrap replicate of data."""
        bs_sample = np.random.choice(data, len(data))
        return func(bs_sample)
        
# Compute mean active bout length
mean_wt = np.mean(bout_lengths_wt)
mean_mut = np.mean(bout_lengths_mut)

# Draw bootstrap replicates using function created above
bs_reps_wt = draw_bs_reps(bout_lengths_wt, np.mean, size=10000)
bs_reps_mut = draw_bs_reps(bout_lengths_mut, np.mean, size=10000)

# Compute 95% confidence intervals using numpy method percentile
conf_int_wt = np.percentile(bs_reps_wt, [2.5, 97.5])
conf_int_mut = np.percentile(bs_reps_mut, [2.5, 97.5])

# Print the results: Mean length and confidence intervals for each genotype
print("""
Wild Type:  mean length = {0:.3f} min., confidence interval = [{1:.1f}, {2:.1f}] min.
Mutant: mean length = {3:.3f} min., confidence interval = [{4:.1f}, {5:.1f}] min.
""".format(mean_wt, *conf_int_wt, mean_mut, *conf_int_mut))
