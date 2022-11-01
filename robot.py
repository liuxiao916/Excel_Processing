import pandas as pd

names_Series = pd.read_excel(io='./data/namelist.xlsx')
names = names_Series['姓名'].values
# print(names['姓名'])
# print(names['姓名'].values)
print(names.shape)
# print(names)

# for i in range(names.shape[0]):
#     print(names[i])

class1_Series = pd.read_excel(io='./data/1.xlsx')
class1_names = class1_Series['学生姓名'].values
class1_times = class1_Series['观看直播时长'].values
result1 = []
# print(class1_names)

for i in range(names.shape[0]):
    isempty = True        # some guys have repeat data! We must deal it
    for j in range(class1_names.shape[0]):
        if names[i] in class1_names[j]:
            if isempty:
                result1.append(class1_times[j])
                isempty = False
            else:
                result1[i] = result1[i] + class1_times[j]  # record repeat data
    if isempty:
        result1.append(0)

class2_Series = pd.read_excel(io='./data/2.xlsx')
class2_names = class2_Series['学生姓名'].values
class2_times = class2_Series['观看直播时长'].values
result2 = []

for i in range(names.shape[0]):
    isempty = True        # some guys have repeat data! We must deal it
    for j in range(class2_names.shape[0]):
        if names[i] in class2_names[j]:
            if isempty:
                result2.append(class2_times[j])
                isempty = False
            else:
                result2[i] = result2[i] + class2_times[j]  # record repeat data
    if isempty:
        result2.append(0)

class3_Series = pd.read_excel(io='./data/3.xlsx')
class3_names = class3_Series['学生姓名'].values
class3_times = class3_Series['观看直播时长'].values
result3 = []

for i in range(names.shape[0]):
    isempty = True        # some guys have repeat data! We must deal it
    for j in range(class3_names.shape[0]):
        if names[i] in class3_names[j]:
            if isempty:
                result3.append(class3_times[j])
                isempty = False
            else:
                result3[i] = result3[i] + class3_times[j]  # record repeat data
    if isempty:
        result3.append(0)

class4_Series = pd.read_excel(io='./data/4.xlsx')
class4_names = class4_Series['学生姓名'].values
class4_times = class4_Series['观看直播时长'].values
result4 = []

for i in range(names.shape[0]):
    isempty = True        # some guys have repeat data! We must deal it
    for j in range(class4_names.shape[0]):
        if names[i] in class4_names[j]:
            if isempty:
                result4.append(class4_times[j])
                isempty = False
            else:
                result4[i] = result4[i] + class4_times[j]  # record repeat data
    if isempty:
        result4.append(0)

class_data = {'names': names, 'class1': result1,
              'class2': result2, 'class3': result3, 'class4': result4}
df = pd.DataFrame(class_data)
df.to_csv('Result.csv')
