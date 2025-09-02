# 04importingandexportingData
import pandas as pd
data = {
    "Name" : ['Ayasha',"Sahil","Keshav","Nishant"],
    "Age" : [19,20,21,20],
    "Marks" : [90,75,85,70]
}

df = pd.DataFrame(data)


#CSV file creation
df.to_csv("student.csv",index=False)
print("CSV file is created")
df_csv = pd.read_csv("student.csv")
print(df_csv)

#excel file
df.to_excel("student.xlsx",index=False)
print("Excel is created")


#export to JSON(JavaScrpt Object Notation) file
df_json=df.to_json("Student.json",index=False)
print(df_json)
print("JSON file is created")