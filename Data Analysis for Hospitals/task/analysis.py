import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype

if __name__ == '__main__':
    pd.set_option('display.max_columns', 12)

    # Load datasets
    general = pd.read_csv('test/general.csv')
    prenatal = pd.read_csv('test/prenatal.csv')
    sports = pd.read_csv('test/sports.csv')

    # rename columns to match the column names in general
    gen_columns = general.columns
    pre_columns = prenatal.columns
    sports_columns = sports.columns
    pre2gen = {k: v for k, v in zip(pre_columns, gen_columns)}
    sports2gen = {k: v for k, v in zip(sports_columns, gen_columns)}
    prenatal.rename(columns=pre2gen, inplace=True)
    sports.rename(columns=sports2gen, inplace=True)

    # concatenate the datasets on columns
    data = pd.concat([general, prenatal, sports], ignore_index=True)

    # drop columns
    data = data.drop(columns=['Unnamed: 0'])
    # print(data.isna().all(axis=1).sum())
    data.dropna(how='all', inplace=True)
    data['gender'].replace(to_replace={'female': 'f', 'woman': 'f', 'male': 'm', 'man': 'm'}, inplace=True)
    data.loc[data['hospital'] == 'prenatal', 'gender'] = data.loc[data['hospital'] == 'prenatal', 'gender'].fillna('f')
    na_cols = dict(bmi=0, diagnosis=0, blood_test=0, ecg=0, ultrasound=0, mri=0, xray=0, children=0, months=0)
    data.fillna(na_cols, inplace=True)

    # print(data.shape)
    # print(data.sample(n=20, random_state=30))
    # print(data.pivot_table(index='hospital', columns='diagnosis', values='gender', aggfunc='count'))
    # print(data.pivot_table(index='hospital', values='age', aggfunc='count'))
    # print(data.pivot_table(index='hospital', values='age', aggfunc='median'))
    # print(data.blood_test.unique())
    # print(data.groupby(['hospital', 'blood_test']).count())

    # print(data.pivot_table(index='hospital', values=data.blood_test.unique(), aggfunc='count'))
    # print(data['diagnosis'].value_counts().index)
    # print(data['diagnosis'].unique())
    bins = [0, 15, 35, 55, 70, 80]
    plt.hist(x=data['age'], bins=bins, color='orange', edgecolor='white')
    plt.show()
    labels = data['diagnosis'].value_counts().index
    plt.pie(data['diagnosis'].value_counts(), labels=labels)
    plt.show()
    plt.violinplot(data['height'])
    plt.show()

    print('The answer to the 1st question: 15-35')
    print(f'The answer to the 2nd question: pregnancy')
    print(f"The answer to the 3rd question: It's because prenatal hospital deals with small children and other hospitals with audults")
    # print(f'The answer to the 4th question is {38-19}')
    # print(f'The answer to the 5th question is prenatal, 325 blood tests')
