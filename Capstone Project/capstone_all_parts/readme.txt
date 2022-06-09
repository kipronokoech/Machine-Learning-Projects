# convert risk score into decimal between 0 and 1
df3['risk_score'] = df3['risk_score']/100.

df3 = df3.drop(['count3_6', 'count6_12',
       'count12_more','income_groups','age_groups','sourcing_channel'], axis=1)

# df3['premium']=pd.cut(df3.premium, bins=[0, 1e4, 2e4, 3e4, 4e4, 5e4, df.premium.max()], labels=[1,2,3,4,5,6])

# Ordinal columns with respective values to replace with
rank_replace = {
                "income_groups": {'100K-200K': 2,
                                 '200K-300K': 3,
                                 'Under100K': 1,
                                 '300K-400K': 4,
                                 '400K-500K': 5,
                                 'Above600K': 7,
                                 '500K-600K': 6},
                "premium": {'A': 1,
                             'B': 2,
                             'C': 3,
                             'D': 4,
                             'E': 5,
                             'F': 6},
                'age_groups': {'Age40-60': 2,
                                 'Age60-80': 3,
                                 'Age20-40': 1,
                                 'Above80': 4}
                }

to_dummies = ["marital_status", "accomodation", "residence"]




{'model_name': 'logistic_default',
 'train_acc': 0.5001428979708488,
 'test_acc': 0.9362998831190515,
 'train_recall': 0.997713632466419,
 'test_recall': 0.998708643184753,
 'train_precision': 0.5000716229766509,
 'test_precision': 0.9374294670846395,
 'train_f1': 0.6662213740458015,
 'test_f1': 0.9670993057651676}

# df3['risk_score'] = df3['risk_score']/100.

{'model_name': 'logistic_default',
 'train_acc': 0.6010288653901115,
 'test_acc': 0.588495575221239,
 'train_recall': 0.5998856816233209,
 'test_recall': 0.5890813554793606,
 'train_precision': 0.6012603838441707,
 'test_precision': 0.9545421747600837,
 'train_f1': 0.6005722460658083,
 'test_f1': 0.7285493997136249}



# making copy of df from part 2 as a variable df3 for convenience.
df3 = df2.copy()

# convert risk score into decimal between 0 and 1
df3['risk_score'] = df3['risk_score']/100.

df3 = df3.drop(['count3_6', 'count6_12',
       'count12_more','income','age','sourcing_channel'], axis=1)

df3['premium']=pd.cut(df3.premium, bins=[0, 1e4, 2e4, 3e4, 4e4, 5e4, df.premium.max()], labels=[1,2,3,4,5,6])

# Ordinal columns with respective values to replace with
rank_replace = {
                "income_groups": {'100K-200K': 4,
                                 '200K-300K': 6,
                                 'Under100K': 2,
                                 '300K-400K': 8,
                                 '400K-500K': 10,
                                 'Above600K': 14,
                                 '500K-600K': 12},
                "premium": {'A': 1,
                             'B': 2,
                             'C': 3,
                             'D': 4,
                             'E': 5,
                             'F': 6},
                'age_groups': {'Age40-60': 2,
                                 'Age60-80': 3,
                                 'Age20-40': 1,
                                 'Above80': 4}
                }

to_dummies = ["marital_status", "accomodation", "residence"]

# Replace ordinal columns with proper number codes
#
df3.replace(rank_replace, inplace=True)

# Create dummies for nominal features.
df3=pd.get_dummies(df3, columns=to_dummies)

df3['default'] = df3['default'].astype('int64')
df3['late_pay'] = df3['late_pay'].astype('int64')
df3['premium'] = df3['premium'].astype('int64')

X = df3.drop("default" , axis=1) # Features
y = df3["default"] # Target

# late_pay 1 or 0

{'model_name': 'logistic_default',
 'train_acc': 0.7525007144898542,
 'test_acc': 0.7514610118550676,
 'train_recall': 0.7559302657902258,
 'test_recall': 0.7516587255644119,
 'train_precision': 0.7507805847289242,
 'test_precision': 0.9781537926638465,
 'train_f1': 0.7533466248931928,
 'test_f1': 0.8500780581155261}

 test [[16880  5577]
 [  377  1122]]
# making copy of df from part 2 as a variable df3 for convenience.
df3 = df2.copy()

# convert risk score into decimal between 0 and 1
df3['risk_score'] = df3['risk_score']/100.

df3['late_pay'] = df3.count3_6 + df3.count6_12 + df3.count12_more


df3 = df3.drop(['count3_6', 'count6_12',"accomodation", 'residence',
       'count12_more','income','age','sourcing_channel','marital_status'], axis=1)

# Redefine: Late premium - establish people who have been late for at least 3 months

df3['premium']=pd.cut(df3.premium, bins=[0, 1e4, 2e4, 3e4, 4e4, 5e4, df.premium.max()], labels=[1,2,3,4,5,6])

# Ordinal columns with respective values to replace with
rank_replace = {
                "income_groups": {'100K-200K': 2,
                                 '200K-300K': 3,
                                 'Under100K': 1,
                                 '300K-400K': 4,
                                 '400K-500K': 5,
                                 'Above600K': 7,
                                 '500K-600K': 6},
                "premium": {'A': 1,
                             'B': 2,
                             'C': 3,
                             'D': 4,
                             'E': 5,
                             'F': 6},
                'age_groups': {'Age40-60': 2,
                                 'Age60-80': 3,
                                 'Age20-40': 1,
                                 'Above80': 4}
                }

#to_dummies = ["marital_status", "accomodation", "residence"]

# Replace ordinal columns with proper number codes
#
df3.replace(rank_replace, inplace=True)

# Create dummies for nominal features.
#df3=pd.get_dummies(df3, columns=to_dummies)

df3['default'] = df3['default'].astype('int64')
df3['late_pay'] = df3['late_pay'].astype('int64')
df3['premium'] = df3['premium'].astype('int64')

X = df3.drop("default" , axis=1) # Features
y = df3["default"] # Target

# late pay added

{'model_name': 'logistic_default',
 'train_acc': 0.7590740211488997,
 'test_acc': 0.7798881282350977,
 'train_recall': 0.7936553300943127,
 'test_recall': 0.7846551186712384,
 'train_precision': 0.7423148890670943,
 'test_precision': 0.9758001993576254,
 'train_f1': 0.7671270718232044,
 'test_f1': 0.8698506725903986}


# making copy of df from part 2 as a variable df3 for convenience.
df3 = df2.copy()

# convert risk score into decimal between 0 and 1
df3['risk_score'] = df3['risk_score']/100.

df3['late_pay'] = df3.count3_6 + df3.count6_12 + df3.count12_more


df3 = df3.drop(['count3_6', 'count6_12',
       'count12_more','income','age','sourcing_channel'], axis=1)

# Redefine: Late premium - establish people who have been late for at least 3 months

df3['premium']=pd.cut(df3.premium, bins=[0, 1e4, 2e4, 3e4, 4e4, 5e4, df.premium.max()], labels=[1,2,3,4,5,6])

# Ordinal columns with respective values to replace with
rank_replace = {
                "income_groups": {'100K-200K': 2,
                                 '200K-300K': 3,
                                 'Under100K': 1,
                                 '300K-400K': 4,
                                 '400K-500K': 5,
                                 'Above600K': 7,
                                 '500K-600K': 6},
                "premium": {'A': 1,
                             'B': 2,
                             'C': 3,
                             'D': 4,
                             'E': 5,
                             'F': 6},
                'age_groups': {'Age40-60': 2,
                                 'Age60-80': 3,
                                 'Age20-40': 1,
                                 'Above80': 4}
                }

to_dummies = ["marital_status", "accomodation", "residence"]

# Replace ordinal columns with proper number codes
#
df3.replace(rank_replace, inplace=True)

# Create dummies for nominal features.
df3=pd.get_dummies(df3, columns=to_dummies)

df3['default'] = df3['default'].astype('int64')
df3['late_pay'] = df3['late_pay'].astype('int64')
df3['premium'] = df3['premium'].astype('int64')

X = df3.drop("default" , axis=1) # Features
y = df3["default"] # Target

# late pay summed




# making copy of df from part 2 as a variable df3 for convenience.
df3 = df2.copy()

# convert risk score into decimal between 0 and 1
df3['risk_score'] = df3['risk_score']/100.

df3['late_pay'] = df3.count3_6 + df3.count6_12 + df3.count12_more


df3 = df3.drop(['late_pay','income','age','sourcing_channel'], axis=1)

# Redefine: Late premium - establish people who have been late for at least 3 months

df3['premium']=pd.cut(df3.premium, bins=[0, 1e4, 2e4, 3e4, 4e4, 5e4, df.premium.max()], labels=[1,2,3,4,5,6])

# Ordinal columns with respective values to replace with
rank_replace = {
                "income_groups": {'100K-200K': 2,
                                 '200K-300K': 3,
                                 'Under100K': 1,
                                 '300K-400K': 4,
                                 '400K-500K': 5,
                                 'Above600K': 7,
                                 '500K-600K': 6},
                "premium": {'A': 1,
                             'B': 2,
                             'C': 3,
                             'D': 4,
                             'E': 5,
                             'F': 6},
                'age_groups': {'Age40-60': 2,
                                 'Age60-80': 3,
                                 'Age20-40': 1,
                                 'Above80': 4}
                }

to_dummies = ["marital_status", "accomodation", "residence"]

# Replace ordinal columns with proper number codes
#
df3.replace(rank_replace, inplace=True)

# Create dummies for nominal features.
df3=pd.get_dummies(df3, columns=to_dummies)

df3['default'] = df3['default'].astype('int64')
#df3['late_pay'] = df3['late_pay'].astype('int64')
df3['premium'] = df3['premium'].astype('int64')

X = df3.drop("default" , axis=1) # Features
y = df3["default"] # Target

# late pay droped and the three related columns kept

{
 'model_name': 'logistic_default',
 'train_acc': 0.7605030008573879,
 'test_acc': 0.7862748372015361,
 'train_recall': 0.795655901686196,
 'test_recall': 0.791646257291713,
 'train_precision': 0.7433911882510014,
 'test_precision': 0.9757945002469949,
 'train_f1': 0.7686361126449477,
 'test_f1': 0.874127249483725
}

