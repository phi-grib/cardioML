import pandas as pd

class building:
    def __init__(self,filepath,engine='openpyxl'):
        self.df=pd.read_excel(filepath, engine=engine)
        self.df=self.df[~(self.df.EADs==1)]
        self.df=self.df.drop(columns=['EADs'])
        self.df=self.df[(self.df.APD90!=0)&(self.df.APD90!=1000)]
        self.df=self.df.reset_index(drop=True)
    def dataframe(self):
#         self.df=self.df.drop(index=[97583,  97627, 100021, 103114, 103300, 103481, 108902, 109004,109053, 115007, 121518],axis=0)
        self.df=self.df.reset_index(drop=True)
        return self.df
    def split (self,n,df):
        self.n=int(n)
        self.df=df
        X_train=self.df.iloc[::n,:3]
        X_val=self.df.iloc[50::n,:3]
        t=X_train.index
        t2=X_val.index
        X_test=df.loc[~df.index.isin(t|t2)].iloc[:,:3]
        y_train=df.loc[X_train.index,'APD90'].astype('float')
        y_val=df.loc[X_val.index,'APD90'].astype('float')
        y_test=df.loc[X_test.index,'APD90'].astype('float')
        return X_train,X_test,X_val,y_train,y_test,y_val