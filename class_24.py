import pandas as pd

names_Series = pd.read_excel(io='data/24/24_name.xlsx')
names = names_Series['姓名'].values
# print(names['姓名'])
# print(names['姓名'].values)
# print(names)

f=dict.fromkeys(names,0)
# for i in range(names.shape[0]):
#     print(names[i])

class1_Series = pd.read_excel(io='data/24/24-9-5.xlsx')
class1_names = class1_Series['成员'].values

for key in f.keys():
    isrepeat = False
    for j in range(class1_names.shape[0]):
        if key in class1_names[j]:
            if not isrepeat:
                isrepeat = True
                f[key] = f[key]+1

# print(f)

class2_Series = pd.read_excel(io='data/24/24-9-19.xls')
class2_names = class2_Series['姓名'].values

for key in f.keys():
    isrepeat = False
    for j in range(class2_names.shape[0]):
        if key in class2_names[j]:
            if not isrepeat:
                isrepeat = True
                f[key] = f[key]+1

# print(f)

class3_Series = pd.read_excel(io='data/24/24-9-26.xls')
class3_names = class3_Series['姓名'].values

for key in f.keys():
    isrepeat = False
    for j in range(class3_names.shape[0]):
        if key in class3_names[j]:
            if not isrepeat:
                isrepeat = True
                f[key] = f[key]+1

# print(f)

class4_Series = pd.read_excel(io='data/24/24-10-8.xls')
class4_names = class4_Series['姓名'].values

for key in f.keys():
    isrepeat = False
    for j in range(class4_names.shape[0]):
        if key in class4_names[j]:
            if not isrepeat:
                isrepeat = True
                f[key] = f[key]+1


class5_Series = pd.read_excel(io='data/24/24-10-10.xls')
class5_names = class5_Series['姓名'].values

for key in f.keys():
    isrepeat = False
    for j in range(class5_names.shape[0]):
        if key in class5_names[j]:
            if not isrepeat:
                isrepeat = True
                f[key] = f[key]+1


class6_Series = pd.read_excel(io='data/24/24-10-17.xls')
class6_names = class6_Series['姓名'].values

for key in f.keys():
    isrepeat = False
    for j in range(class6_names.shape[0]):
        if key in class6_names[j]:
            if not isrepeat:
                isrepeat = True
                f[key] = f[key]+1


class7_Series = pd.read_excel(io='data/24/24-10-24.xls')
class7_names = class7_Series['姓名'].values

for key in f.keys():
    isrepeat = False
    for j in range(class7_names.shape[0]):
        if key in class7_names[j]:
            if not isrepeat:
                isrepeat = True
                f[key] = f[key]+1

# print(f)

# print(names_Series)
for index, row in names_Series.iterrows():
    names_Series.iloc[index,5] = f[row['姓名']]
    print(names_Series.iloc[index,6])

print(names_Series)
names_Series.to_csv('Result_24.csv')
