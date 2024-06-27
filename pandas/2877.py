import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data)
    return df.rename(columns={0 :"student_id",1 :"age"})
