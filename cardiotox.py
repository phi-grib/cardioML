import numpy as np
import pandas as pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import random
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler,MinMaxScaler, PolynomialFeatures
from sklearn.model_selection import GridSearchCV,KFold,train_test_split, cross_val_score
from sklearn.metrics import accuracy_score,r2_score,mean_squared_error,mean_absolute_error
import matplotlib.pyplot as plt
import time
from tqdm.notebook import tqdm
import warnings

def build_model(model,n2,c,n_error_min,n_error_max,X_train,X_val,X_test,y_train,y_val,y_test):
    import random
    from sklearn.svm import SVR
    random.seed(46)
    model=model
    model.fit(X_train,y_train)
    ypredt=model.predict(X_train)
    ypredval=model.predict(X_val)
    ypred=model.predict(X_test)
    maetrain=mean_absolute_error(y_train,ypredt)
    maetest=mean_absolute_error(y_test,ypred)
    maeval=mean_absolute_error(y_val,ypredval)
    print(f'MAE selecting 1/{n2} indexes for training series {maetrain:.3f}')
    print(f'MAE selecting 1/{n2} indexes for Validation series {maeval:.3f}')
    print(f'MAE selecting 1/{n2} indexes for test series {maetest:.3f}')
    residuales=(abs(ypred-y_test))*100/y_test
    residuals_train=(abs(ypredt-y_train))*100/y_train
    residuals_val=(abs(ypredval-y_val))*100/y_val
    resi_train=pd.DataFrame({'Resi':residuals_train,'y_pred':ypredt}).reset_index(drop=True)
    resi_val=pd.DataFrame({'Resi':residuals_val,'y_pred':ypredval}).reset_index(drop=True)
    resi_test=pd.DataFrame({'Resi':residuales,'y_pred':ypred}).reset_index(drop=True)
    idx_error_train=np.where(np.logical_and(resi_train.Resi>=n_error_min, resi_train.Resi<=n_error_max))[0]
    idx_error_val=np.where(np.logical_and(resi_val.Resi>=n_error_min, resi_val.Resi<=n_error_max))[0]
    idx_error_test=np.where(np.logical_and(resi_test.Resi>=n_error_min, resi_test.Resi<=n_error_max))[0]
    error_train=resi_train.loc[idx_error_train,:]
    error_val=resi_val.loc[idx_error_val,:]
    error_test=resi_test.loc[idx_error_test,:]
    defi_error_perc_train=len(error_train)*100/len(resi_train)
    defi_error_perc_val=len(error_val)*100/len(resi_val)
    defi_error_perc_test=len(error_test)*100/len(resi_test)
    print('MRE train set=%.2f'%(resi_train.Resi.mean())+'%')
    print('MRE validation set=%.2f'%(resi_val.Resi.mean())+'%')
    print('MRE test set=%.2f'%(resi_test.Resi.mean())+'%')
    print('Maximum RE train set=%.2f'%(resi_train.Resi.max())+'%')
    print('Maximum RE validation set=%.2f'%(resi_val.Resi.max())+'%')
    print('Maximum RE test set=%.2f'%(resi_test.Resi.max())+'%')
    print('When RE is between %s-%s'%(n_error_min,n_error_max)+'%'+' a %.2f'%(defi_error_perc_train)+str('% of data have a RE lower than 5% for the train set'))
    print('When RE is between %s-%s'%(n_error_min,n_error_max)+'%'+' a %.2f'%(defi_error_perc_val)+str('% of data have a RE lower than 5% for the validation set'))
    print('When RE is between %s-%s'%(n_error_min,n_error_max)+'%'+' a %.2f'%(defi_error_perc_test)+str('% of data have a RE lower than 5% for the test set'))
    fig,ax = plt.subplots(1,1,figsize=(10,6))
    params = {'mathtext.default': 'regular' }          
    plt.rcParams.update(params)
    plt.rcParams["font.family"] = 'Franklin Gothic Medium'
    ax.tick_params(axis='both', labelsize=22)
    ax.set_yticks(np.arange(0,11.5,2.5))
    ax.set_yticklabels(['0','2.5','5','7.5','10'])
    ax.xaxis.set_ticks([0,250,350,450,550,650,750]) 
    ax.scatter(y_test,resi_test.Resi,s=3)
    ax.set_ylim(0,10.5)
    ax.set_xlim(220,800)
    ax.set_xlabel('$APD_{90}$ (ms)',size=22,labelpad=15)
    ax.set_ylabel('RE (%)',size=22,labelpad=2)
    ax.legend([''],prop={'size': 12},markerscale=3)
    ax.get_legend().remove()
    plt.show()
    
def plotea(model,n_ical,X_train,X_val,X_test,y_train,y_val,y_test):
    model=model
    model.fit(X_train,y_train)
    ypred = model.predict(X_test)
    ypredval = model.predict(X_val)
    ypredt=model.predict(X_train)
    predictions=X_test.copy()
    predictions['Predict']=model.predict(X_test)
    testing=pd.concat([X_test,y_test],axis=1)
    testing=testing[testing.CaL==n_ical]
    predict_ical_test=predictions[predictions.CaL==n_ical]

    predictions_train=X_train.copy()
    predictions_train['Predict']=model.predict(X_train)
    training=pd.concat([X_train,y_train],axis=1)
    training=training[training.CaL==n_ical]
    predict_ical_train=predictions_train[predictions_train.CaL==n_ical]

    predictions_val=X_val.copy()
    predictions_val['Predict']=model.predict(X_val)
    val=pd.concat([X_val,y_val],axis=1)
    val=val[val.CaL==n_ical]
    predict_ical_val=predictions_val[predictions_val.CaL==n_ical]

    juntos_real=pd.concat([training,val,testing],axis=0).sort_index()
    juntos_predict=pd.concat([predict_ical_train,predict_ical_val,predict_ical_test],axis=0).sort_index()
    plt.figure(figsize=(10,12))
    ax = plt.axes(projection='3d')
    ax.view_init(20,59)#(15,59)
    params = {'mathtext.default': 'regular' }          
    plt.rcParams.update(params)
    plt.rcParams["font.family"] = 'Franklin Gothic Medium'
    plt.rcParams.update({'font.size': 25})
    ax.tick_params(axis='x', pad=0)
    ax.tick_params(axis='y', pad=0)
    ax.tick_params(axis='z', pad=15)
    ax.set_ylim(-3,2)
    ax.set_xticks([-3, -2, -1,0,1,2])
#     ax.set_yticks([2,1,0,-1,-2,-3])
    ax.set_yticklabels(['-3','-2','-1','0','1','2'])
    #     ax.set_title('ICAL {:.f}'.format(n))
    ax.set_xlabel('$I_{Kr}$',labelpad=15,size=25)#fontdict=dict(weight='bold')#'$log_{10}$ $([D]/IC50_{IKr})$'
    ax.set_ylabel('$I_{Ks}$',labelpad=20,size=25)
    ax.zaxis.set_rotate_label(False)  # disable automatic rotation
    ax.set_zlabel('$APD_{90}$ (ms)',labelpad=40, rotation=90,size=25)
    plt.locator_params(axis='z', nbins=7)
#     plt.tight_layout()
#     ax.set_zticks([0,1,2,3])
#     ax.set_ylim(300,750)
    ax.scatter3D(juntos_predict['Kr'], juntos_predict['Ks'], juntos_predict['Predict'], cmap=plt.cm.Blues)
    ax.scatter3D(juntos_real['Kr'], juntos_real['Ks'], juntos_real['APD90'], cmap=plt.cm.Reds)
#     ax.legend(['Prediction','Experimental'])