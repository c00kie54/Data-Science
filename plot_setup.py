#Function that sets the data u for plotting


def plot_setup(player_data,pos_data,position):
    df_unique = pd.DataFrame(columns=['Name', 'Points', 'Position','Cost'])
    df_unique['Name'] = pos_data['name'].unique()
    df_unique['Position'] = position
    for i in range(len(df_unique)):
        df_unique.Points[i]= pos_data.loc[player_data['name'] == df_unique.Name[i] , 'total_points'].sum()
        df_unique.Cost[i]= (pos_data.loc[player_data['name'] == df_unique.Name[i] , 'value']
                                .sum())/len(pos_data[pos_data['name'].str.contains(df_unique.Name[i])])
    df_unique = df_unique[df_unique['Cost'] > 4]  
    return df_unique

def plot_scatter(x1,x2,x3,x4,x5,x6,x7,x8,y1,y2,y3,y4,y5,y6,y7,y8):
    x1_np = np.array(x1)
    x2_np = np.array(x2)
    x3_np = np.array(x3)
    x4_np = np.array(x4)
    x5_np = np.array(x5)
    x6_np = np.array(x6)
    x7_np = np.array(x7)
    x8_np = np.array(x8)
    y1_np = np.array(y1)
    y2_np = np.array(y2)
    y3_np = np.array(y3)
    y4_np = np.array(y4)
    y5_np = np.array(y5)
    y6_np = np.array(y6)
    y7_np = np.array(y7)
    y8_np = np.array(y8)
    x1_rs = x1_np.reshape(len(x1_np), 1)
    x2_rs = x2_np.reshape(len(x2_np), 1)
    x3_rs = x3_np.reshape(len(x3_np), 1)
    x4_rs = x4_np.reshape(len(x4_np), 1)
    x5_rs = x5_np.reshape(len(x5_np), 1)
    x6_rs = x6_np.reshape(len(x6_np), 1)
    x7_rs = x7_np.reshape(len(x7_np), 1)
    x8_rs = x8_np.reshape(len(x8_np), 1)
    y1_rs = y1_np.reshape(len(y1_np), 1)
    y2_rs = y2_np.reshape(len(y2_np), 1)
    y3_rs = y3_np.reshape(len(y3_np), 1)
    y4_rs = y4_np.reshape(len(y4_np), 1)
    y5_rs = y5_np.reshape(len(y5_np), 1)
    y6_rs = y6_np.reshape(len(y6_np), 1)
    y7_rs = y7_np.reshape(len(y7_np), 1)
    y8_rs = y8_np.reshape(len(y8_np), 1)

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
    x4_hat = np.arange(start=4.5, stop=13, step=0.5)
    y4_hat = reg.coef_*x4_hat +reg.intercept_
    y4_hat = y4_hat.flatten() 

    reg = LinearRegression().fit(x5_rs, y5_rs)
    x5_hat = np.arange(start=4, stop=7, step=1)
    y5_hat = reg.coef_*x5_hat +reg.intercept_
    y5_hat = y5_hat.flatten() 

    reg = LinearRegression().fit(x6_rs, y6_rs)
    x6_hat = np.arange(start=4, stop=8, step=0.5)
    y6_hat = reg.coef_*x6_hat +reg.intercept_
    y6_hat = y6_hat.flatten() 

    reg = LinearRegression().fit(x7_rs, y7_rs)
    x7_hat = np.arange(start=4.5, stop=13, step=0.5)
    y7_hat = reg.coef_*x7_hat +reg.intercept_
    y7_hat = y7_hat.flatten() 

    reg = LinearRegression().fit(x8_rs, y8_rs)
    x8_hat = np.arange(start=4.5, stop=13, step=0.5)
    y8_hat = reg.coef_*x8_hat +reg.intercept_
    y8_hat = y8_hat.flatten()



    fig, axs = plt.subplots(2, 2,figsize=(14,10))
    axs[0, 0].plot(x5, y5,'kx', label='2019/2020 ')
    axs[0, 0].plot(x5_hat, y5_hat,'b--',label='2019/2020 best fit')
    axs[0, 0].plot(x1, y1,'r.',label='2018/2019')
    axs[0, 0].plot(x1_hat, y1_hat,'g:',label='2018/2019 best fit' )

    axs[1, 0].plot(x6, y6,'kx')
    axs[1, 0].plot(x6_hat, y6_hat,'b--')
    axs[1, 0].plot(x2, y2,'r.')
    axs[1, 0].plot(x2_hat, y2_hat,'g:')

    axs[0, 1].plot(x7, y7,'kx')
    axs[0, 1].plot(x7_hat, y7_hat,'b--')  
    axs[0, 1].plot(x3, y3,'r.')
    axs[0, 1].plot(x3_hat, y3_hat,'g:') 

    axs[1, 1].plot(x8, y8,'kx')
    axs[1, 1].plot(x8_hat, y8_hat,'b--')
    axs[1, 1].plot(x4, y4,'r.')
    axs[1, 1].plot(x4_hat, y4_hat,'g:')

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


    legend = fig.legend()
    handles, labels = axs[0,0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper right', shadow=True, fontsize='x-large')
    return