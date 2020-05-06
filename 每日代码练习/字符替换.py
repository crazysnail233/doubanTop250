import re

str1 = '永远$$$都要相信自己@#@#能克服一切&%&%&困难'
str2 = re.sub('[$@#%&]+','_',str1)
print(str2)