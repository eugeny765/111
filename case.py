
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance .csv')
df.info()
print(df.head(11))
print(df['parental level of education'].value_counts())


#print('гипотеза, что по каждому предмету с подготовкой результаты лучше')

#result_with_math = df[df['test preparation course']=='completed']['math score'].mean()
#result_without_math = df[df['test preparation course']=='none']['math score'].mean()
#result_with_reading = df[df['test preparation course']=='completed']['reading score'].mean()
#result_without_reading = df[df['test preparation course']=='none']['reading score'].mean()
#result_with_writing = df[df['test preparation course']=='completed']['writing score'].mean()
#result_without_writing = df[df['test preparation course']=='none']['writing score'].mean()
#print('результат с подготовкой по математике', round(result_with_math, 2))
#print('результат без подготовки по математике', round(result_without_math, 2))
#print('результат с подготовкой по чтению', round(result_with_reading, 2))
#print('результат без подготовки по чтению', round(result_without_reading, 2))
#print('результат с подготовкой по письму', round(result_with_writing, 2))
#print('результат без подготовки по письму', round(result_without_writing, 2))

#print('результат по всем предметам с подготовкой выше')


#s = pd.Series(data = [result_with_math, result_without_math, result_with_reading, result_without_reading, 
#result_with_writing, result_without_writing], index = ['с подготовкой к математике','без подготовки к математике',
#'с подготовкой к чтению','без подготовки к чтению','с подготовкой к письму','без подготовки к письму'])
#s.plot(kind = 'barh',figsize = (8, 5))
#plt.show()


print('гипотеза, что дети с родителями, с более высоким уровнем образования, имеют лучше результаты по математике')


result_somecollege = df[df['parental level of education'] == 'some college']['math score'].mean()
result_associatesdegree = df[df['parental level of education'] == "'associate's degree'"]['math score'].mean()
result_highschool = df[df['parental level of education'] == 'high school']['math score'].mean()
result_somehighschool = df[df['parental level of education'] == 'some high school']['math score'].mean()
result_bachelorsdegree = df[df['parental level of education'] == "'bachelor's degree'"]['math score'].mean()
result_mastersdegree  = df[df['parental level of education'] == "'master's degree '"]['math score'].mean()
print('значение1', round(result_somecollege, 2))
print('значение2', round(result_associatesdegree, 2))
print('значение3', round(result_highschool, 2))
print('значение4', round(result_somehighschool, 2))
print('значение5', round(result_bachelorsdegree, 2))
print('значение6', round(result_mastersdegree, 2))

