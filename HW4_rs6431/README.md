# Assignment1:
The objective of this assignment is to verify the central limit theorm. Cetral limit theorm argues that when the sample size approches to infinite, the sample mean approaches a Normal (Gaussian) distribution with the population mean μ and standard deviation σ, regardless of the distribution of X. 

Through the five distribution tested in this assignment, when sample size growth, the sample mean indeed close to the mean of the parent distribution, regardless of the type of original distribution.

# Assignment 2:
The objective of this assignment is to train the ability to set the hypothesis and choose suitable dataset to evaluate the hypothesis.

* Defined function to let downloading and unzipping dataset become reproducible is really valuable.

* I addressed problem by myself, but also work with others when facing problem.
When covert 2015-07-01 00:00:00 to 2015-07-01 style, I fail to achive right data style to plot. 
Originally used: 
df['date'] = pd.to_datetime(df['starttime'])
df.set_index['date] code.

After consulting Tanya, change the code to:
df['date'] = pd.to_datetime(df['starttime']).dt.date
This code out put 'date' data as Series type, then it works in poting. 

Learned 'pandas.Series.dt.date'function only keep the yyyy-mm-dd part.

* Learned the df.plot.bar method to plot several bars together, which is useful.

# Assignment 3:
The objective of this assignment is to understand the Z-test and apply it to test the null/alternative hypothesis. 
