import shutil
from time import sleep

file = 'D:\\em_ppp_22_06_2024_upper.mpg'
location = 'Z:\\em_ppp_22_06_2024_upper.mpg'

sleep(960)
shutil.copyfile(file,location)
