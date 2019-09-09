#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_report(fle_name):
    # PICCNT1.CSV is background check
    # PICCNT2.CSV is beta source check with Tc-99
    
    df = pd.read_csv(fle_name, header=1)
    ttle = pd.read_csv(fle_name, header=None).loc[0][7]
    fig, ax1 = plt.subplots(2,1)
    ax1[0].set_xlabel('time (s)')
    ax1[0].set_ylabel('Counts Alpha')
    ax1[0].plot(df["DATE"], df["A"])
    lbl_mean = str(np.round(df["A"].mean()*100)/100)
    ax1[0].plot(df["DATE"], df["A"].mean() * np.ones(len(df["A"])), label=lbl_mean)
    ax1[0].plot(df["DATE"], df["A"].mean() + 2* np.sqrt(df["A"].var()) * np.ones(len(df["A"])), 'k--', 
               label='2 $\sigma$')
    ax1[0].plot(df["DATE"], df["A"].mean() - 2* np.sqrt(df["A"].var()) * np.ones(len(df["A"])), 'k--')
    ax1[0].plot(df["DATE"], df["A"].mean() + 3* np.sqrt(df["A"].var()) * np.ones(len(df["A"])), 'r--', 
               label='3 $\sigma$')
    ax1[0].plot(df["DATE"], df["A"].mean() - 3* np.sqrt(df["A"].var()) * np.ones(len(df["A"])), 'r--')
    ax1[0].tick_params(axis='y')
    ax1[0].tick_params(labelrotation=90)
    ax1[0].set_title('Alpha Count Control Chart ' + ttle)
    ax1[0].legend()
    
    ax1[1].set_xlabel('time (s)')
    ax1[1].set_ylabel('Counts Alpha')
    ax1[1].plot(df["DATE"], df["B"])
    lbl_mean = str(np.round(df["B"].mean()*100)/100)
    ax1[1].plot(df["DATE"], df["B"].mean() * np.ones(len(df["B"])), label=lbl_mean)
    
    ax1[1].plot(df["DATE"], df["B"].mean() + 2*np.sqrt( df["B"].var()) * np.ones(len(df["B"])), 'k--', 
                label='2 $\sigma$')
    ax1[1].plot(df["DATE"], df["B"].mean() - 2*np.sqrt( df["B"].var()) * np.ones(len(df["B"])), 'k--')
    ax1[1].plot(df["DATE"], df["B"].mean() + 3* np.sqrt(df["B"].var()) * np.ones(len(df["B"])), 'r--',
                label='3 $\sigma$')
    ax1[1].plot(df["DATE"], df["B"].mean() - 3* np.sqrt(df["B"].var()) * np.ones(len(df["B"])), 'r--')
    ax1[1].tick_params(axis='y')
    ax1[1].tick_params(labelrotation=90)
    ax1[1].set_title('Beta Count Control Chart ' + ttle)
    ax1[1].ticklabel_format(axis='y', scilimits=(0,0))
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    ax1[1].legend()
    plt.show()
    
#Begin processing    
fle_name = [r'M:\radcon\RAL\Protean\PICCNT1.CSV', #Background
            r'M:\radcon\RAL\Protean\PICCNT2.CSV', #Tc-99
            r'M:\radcon\RAL\Protean\PICCNT3.CSV', #Am-241
            #r'M:\radcon\RAL\Protean\PICCNT4.CSV'
           ] #None

for i in fle_name:
    run_report(i)
    


# In[2]:


fle_name = r'M:\radcon\RAL\Protean\PICPLAT.CSV'
df = pd.read_csv(fle_name, header=1)
df
fig, ax1 = plt.subplots(2,1)
ax1[0].set_xlabel('Voltage')
ax1[0].set_ylabel('Counts')
ax1[0].plot(df["VOLTS"], df["COUNTS"])
ax1[0].set_title('Plateua Curve Counts')
ax1[1].set_xlabel('Voltage')
ax1[1].set_ylabel('Slope')
ax1[1].plot(df["VOLTS"], df["SLOPE"])
ax1[1].set_title('Plateau Curve Slope')
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()


# In[3]:


fle_name = r'M:\radcon\RAL\Protean\2018_Q3_Source Leak Tests.csv'
df0 = pd.read_csv(fle_name, header=1)
df = df0.loc[:, ['SAMPLE_ID', 'PROGRAM_NAME', 'DATE', 'TIME', 'ADPM', 'BDPM', 'A', 'B', 
           'CNT_TIME','AEFF', 'BEFF', "ABKGCPM", 'BBKGCPM', 'A_MDA', 'B_MDA','BG_TIME' ]]

df['BLC_DPM'] = 1.645* 100 / df['BEFF'] * np.sqrt( df['BBKGCPM']* (1 /df['CNT_TIME'] + 1/df['BG_TIME']))
df['BLD_DPM'] = 2.71 * 100/ (df['BEFF'] * df['CNT_TIME']) + 2*df['BLC_DPM']

df['ALC_DPM'] = 1.645* 100 / df['AEFF'] * np.sqrt(2 * df['ABKGCPM']*(1 /df['CNT_TIME']+ 1/df['BG_TIME']) )
df['ALD_DPM'] = 2.71 * 100/ (df['AEFF'] * df['CNT_TIME']) + 2*df['ALC_DPM']
df


# In[4]:


df.dropna()
df.loc[df['BDPM']>=df['BLC_DPM'] , ('SAMPLE_ID', 'BDPM', 'B_MDA')]


# In[5]:


df0


# In[ ]:




