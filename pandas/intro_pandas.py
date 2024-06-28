import pandas as pd
# 1
def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data)
    return df.rename(columns={0 :"student_id",1 :"age"})
# 2
def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return list(players.shape)
# 3
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
# 4
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df = students.loc[students['student_id'] == 101, ['name','age']]
    return df
# 5 
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
   employees['bonus'] = employees['salary'] * 2
   return employees
# 6
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates('email')
#7
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])
# 8
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees
#9
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={'id':'student_id','first':'first_name','last':'last_name','age' : 'age_in_years'})  
#10
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students
#11
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products
#12
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1,df2])
#13
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return pd.pivot(index='month',columns='city',values='temperature')
#14
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(
        id_vars=['product'],
        value_vars=['quarter_1','quarter_2','quarter_3','quarter_4'],
        var_name='quarter',
        value_name='sales'
        )
#15
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df_weight = animals[animals['weight'] > 100]
    df_sorted = df_weight.sort_values(by=['weight'],ascending=False)
    return df_sorted[['name']]
