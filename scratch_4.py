import pandas as pd
import numpy as np
df = pd.DataFrame({
'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],
'purch_amt': [150.5, np.nan, 65.26, 110.5, 948.5, np.nan, 5760, 1983.43, np.nan, 250.45, 75.29, 3045.6],
'sale_amt': [10.5, 20.65, np.nan, 11.5, 98.5, np.nan, 57, 19.43, np.nan, 25.45, 75.29, 35.6],
'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001],
'salesman_id': [5002, 5003, 5001,np.nan, 5002, 5001, 5001,np.nan, 5003, 5002, 5003,np.nan]})

#x = df.index.values
#y = df['ord_no']. to_numpy()
#interpolator = lambda t: np.interp(t,x,y)
#print(df.shape)

#B = df.notnull()
#nmp=B.values.tolist()
#print(B)
#print(nmp)



#index = nmp.index('False')
#print(index)

#print(B[B["purch_amt"] == 'false'])
#print(B.groupby('purch_amt'))
#print(A)
#mask = pd.isna(df['ord_no'])
#print(mask)
#print(list(df[mask]['ord_no'].index))
#d =[]
#for i in range (B.shape[0]):
    #for j in range(B.shape[1]):
        #if x[i] == False:
            #d.append(i)
#print(d)

df['ord_no'].fillna(df['ord_no'].interpolate(), inplace = True )
df['purch_amt'].fillna(df['purch_amt'].mean(), inplace = True )
df['sale_amt'].fillna(df['sale_amt'].mean(), inplace = True )
df['ord_date'].fillna('2012-10-10', inplace = True )
df['customer_id'].fillna(df['customer_id'].mean(), inplace = True )
df['salesman_id'].fillna(df['salesman_id'].mean(), inplace = True )

print(df)





