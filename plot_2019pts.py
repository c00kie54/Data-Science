import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import sklearn
from sklearn.linear_model import LinearRegression

def data_read(name): 
    data =pd.read_csv(name)
    print('Data Loaded Sucessfully')
    return data

FW_data = data_read('/Users/alexcooke/Desktop/Player_Prices/FW-Table 1.csv') # Load forwards players + prices
DF_data = data_read('/Users/alexcooke/Desktop/Player_Prices/DF-Table 1.csv') # Load forwards players + prices
MF_data = data_read('/Users/alexcooke/Desktop/Player_Prices/MF-Table 1.csv') # Load forwards players + prices
GK_data = data_read('/Users/alexcooke/Desktop/Player_Prices/GK-Table 1.csv') # Load forwards players + prices

GK_data = GK_data[~(GK_data == 0).any(axis=1)]
DF_data = DF_data[~(DF_data == 0).any(axis=1)]
MF_data = MF_data[~(MF_data == 0).any(axis=1)]
FW_data = FW_data[~(FW_data == 0).any(axis=1)]

GK_data.dropna()
DF_data.dropna()
MF_data.dropna()
FW_data.dropna()
DF_data = DF_data[DF_data.Player != 'Player']
GK_data['Cost'] = GK_data['Cost'].str.replace('£', '')
DF_data['Cost'] = DF_data['Cost'].str.replace('£', '')
MF_data['Cost'] = MF_data['Cost'].str.replace('£', '')
FW_data['Cost'] = FW_data['Cost'].str.replace('£', '')
y1 = GK_data['Points'].astype(float)
x1 = GK_data['Cost'].astype(float)
y2 = DF_data['Points'].astype(float)
x2 = DF_data['Cost'].astype(float)
y3 = MF_data['Points'].astype(float)
x3 = MF_data['Cost'].astype(float)
y4 = FW_data['Points'].astype(float)
x4 = FW_data['Cost'].astype(float)



fig, axs = plt.subplots(2, 2,figsize=(15,10))

axs[0, 0].plot(x1, y1,'g.')
axs[1, 0].plot(x2, y2,'r.')
axs[0, 1].plot(x3, y3,'b.')
axs[1, 1].plot(x4, y4,'k.')
fig.suptitle('Cost vs Points for the different positions') 
axs[0, 0].set_title('Goalkeepers')
axs[1, 0].set_title('Defenders')
axs[0, 1].set_title('Midfielders')
axs[1, 1].set_title('Forwards')
axs[0,0].set_xlabel('Cost (£)')
axs[0,1].set_xlabel('Cost (£)')
axs[1,0].set_xlabel('Cost (£)')
axs[1,1].set_xlabel('Cost (£)')
axs[0,0].set_ylabel('Points')
axs[1,0].set_ylabel('Points')
axs[0,1].set_ylabel('Points')
axs[1,1].set_ylabel('Points')

x1_np = np.array(x1)
x2_np = np.array(x2)
x3_np = np.array(x3)
x4_np = np.array(x4)
y1_np = np.array(y1)
y2_np = np.array(y2)
y3_np = np.array(y3)
y4_np = np.array(y4)
x1_rs = x1_np.reshape(len(x1_np), 1)
x2_rs = x2_np.reshape(len(x2_np), 1)
x3_rs = x3_np.reshape(len(x3_np), 1)
x4_rs = x4_np.reshape(len(x4_np), 1)
y1_rs = y1_np.reshape(len(y1_np), 1)
y2_rs = y2_np.reshape(len(y2_np), 1)
y3_rs = y3_np.reshape(len(y3_np), 1)
y4_rs = y4_np.reshape(len(y4_np), 1)

reg = LinearRegression().fit(x1_rs, y1_rs)
x1_hat = np.arange(start=4, stop=7, step=1)
y1_hat = reg.coef_*x1_hat +reg.intercept_
y1_hat = y1_hat.flatten() 

reg = LinearRegression().fit(x2_rs, y2_rs)
x2_hat = np.arange(start=4, stop=8, step=0.5)
y2_hat = reg.coef_*x2_hat +reg.intercept_
y2_hat = y2_hat.flatten() 

reg = LinearRegression().fit(x3_rs, y3_rs)
x3_hat = np.arange(start=4.5, stop=13, step=0.5)
y3_hat = reg.coef_*x3_hat +reg.intercept_
y3_hat = y3_hat.flatten() 

reg = LinearRegression().fit(x4_rs, y4_rs)
x4_hat = np.arange(start=4.5, stop=11, step=0.5)
y4_hat = reg.coef_*x4_hat +reg.intercept_
y4_hat = y4_hat.flatten() 


fig, axs = plt.subplots(2, 2,figsize=(15,10))

axs[0, 0].plot(x1, y1,'g.')
axs[0, 0].plot(x1_hat, y1_hat,'c--')
axs[1, 0].plot(x2, y2,'r.')
axs[1, 0].plot(x2_hat, y2_hat,'c--')
axs[0, 1].plot(x3, y3,'b.')
axs[0, 1].plot(x3_hat, y3_hat,'c--')             
axs[1, 1].plot(x4, y4,'k.')
axs[1, 1].plot(x4_hat, y4_hat,'c--')
fig.suptitle('Cost vs Points for the different positions') 
axs[0, 0].set_title('Goalkeepers')
axs[1, 0].set_title('Defenders')
axs[0, 1].set_title('Midfielders')
axs[1, 1].set_title('Forwards')
axs[0,0].set_xlabel('Cost (£)')
axs[0,1].set_xlabel('Cost (£)')
axs[1,0].set_xlabel('Cost (£)')
axs[1,1].set_xlabel('Cost (£)')
axs[0,0].set_ylabel('Points')
axs[1,0].set_ylabel('Points')
axs[0,1].set_ylabel('Points')
axs[1,1].set_ylabel('Points')