import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


df_1 = pd.read_excel('Datos sesión 7 - est 2.xlsx', sheet_name='GDP pc constant')
df_2 = pd.read_excel('Datos sesión 7 - est 2.xlsx', sheet_name='GDP per hour worked')

df_1.shape, df_2.shape 

df_1.head(2)

df_2.head()

df_1.columns = [str(col) for col in df_1.columns]
df_1.columns


columns = ['Country', '1970', '1971',
       '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980',
       '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
       '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998',
       '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
       '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
       '2017', '2018']
df_1 = df_1[columns]

df_2.columns = [str(col) for col in df_2.columns]
df_2.columns

columns = ['Country', '1970', '1971',
       '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980',
       '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
       '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998',
       '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
       '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
       '2017', '2018']

df_2 = df_2[columns]

df_1['Country'].nunique(), df_2['Country'].nunique()


df_2 = df_2[~df_2.isnull().any(axis=1)]


df_1 = df_1[df_1.Country.isin(df_2.Country)]


df_1.shape, df_2.shape


cnt_names = df_1['Country'].unique()

country_factor = {}

for idx, country in enumerate(cnt_names):
    x = df_1[df_1.Country.isin([cnt_names[idx]])].values[0][1:].reshape(-1,1)
    y = df_2[df_2.Country.isin([cnt_names[idx]])].values[0][1:]
    model = LinearRegression()
    model.fit(x, y)
    r_sq = model.score(x, y)
    coef = model.coef_
    country_factor[country] = [r_sq, coef]

country_factor

res = pd.DataFrame(country_factor.items())
res.columns = ['Country', 'result']

res['r2_sq'] = res['result'].apply(lambda x: x[0])
res['coef_score'] = res['result'].apply(lambda x: x[1])


res.head()

res = res[['Country', 'r2_sq', 'coef_score']]


res.to_excel(results.xlsx)



