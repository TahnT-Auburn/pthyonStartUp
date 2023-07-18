# %%
import yaml

with open('configtest.yaml', 'r') as f:
    data = yaml.safe_load_all(f)

    # specify desried set
    setDesired = 3
    iter = 0
    versNum = 0
    for vers in data:
        versNum += 1
        print('This should repeat 4 times')
        if iter == setDesired-1:
            dataUse = vers
        iter += 1
print('set specified:',setDesired,'out of',versNum,'sets')
print(dataUse['username'])
print(dataUse['path'][0])
print(dataUse['test']['test2'])

    #print(data['username'])
    #print(data['path'][0])  # path is a list, must use integer indices

   # print(data['test']['test1']) # test is a dict, must specify respective names