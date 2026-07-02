import pandas as pd
import numpy as np

print("\033[1m" + "=== Advanced Pandas Multi-Table Joiner ===" + "\033[0m\n")

student_info = {
    'Student': ['Zaynul', 'Rahul', 'Amit', 'Sana'],
    'Course': ['BCA', 'B.Tech', 'MCA', 'B.Tech'],
    'City': ["Bareilly",'Delhi', 'Lucknow', 'Bareilly']
}

student_df = pd.DataFrame(student_info)

center_info = {
    'Course':['BCA', 'B.Tech', 'MCA', 'B.Tech'],
    'City':['Bareilly', 'Delhi', 'Lucknow', 'Lucknow'],
    'Center_Name': ['Berilly Tech college', 'Delhi IIT Campus', "Lucknow Universty", 'Bombay IIT']
}

center_df = pd.DataFrame(center_info)

print("\n===Student Table===")
print(student_df)

print("\n===Center Table===")
print(center_df)


final_df = pd.merge(student_df , center_df , on=['Course' ,'City'], how='left')
final_df['Center_Name'] = final_df['Center_Name'].fillna('Bareilly College')
print("\n===Merging ke baad Alloted Center Table")
print(final_df)

