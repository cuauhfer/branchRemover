
import os
from traceback import print_list

BRANCH_LIST = ['master', 'QA', 'dev', 'miLocalBranch']
PROTECTED_BRANCHES = ['master', 'dev', 'QA']

print('The next branches will be deleted: ')
for branch in BRANCH_LIST:
    print('\t - ' + branch)

confirmation = input('Continue? Y/N ')

if confirmation != 'Y' and confirmation != 'y':
    exit()

for branch in BRANCH_LIST:
    if branch in PROTECTED_BRANCHES:
        print('Branch ' + branch + ' can not be deleted')
        continue

    os.system('git branch -D ' + branch)
    os.system('git push origin --delete ' + branch)
    os.system('git branch -a')