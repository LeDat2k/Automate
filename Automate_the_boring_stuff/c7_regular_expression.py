#!/usr/bin/env python3

# from distutils.filelist import findall
import re
from icecream import ic

regex_var = re.compile(r'(\+?(\d){2,3})-(\d{9})')
str = 'So dien thoai trong string la: +84-869570027'

phone_number = regex_var.split(str)
ic(phone_number)
ic(phone_number.group(0))
ic(phone_number.group(1))
ic(phone_number.group(2))
ic(phone_number.groups()) # use when (() ()) in the string

#----------------------------------------------
regex_var = re.compile(r'(v|V)ietnam|(c|C)hina')
str = 'Dat nuoc cua toi la Vietnam, ke thu cua dat nuoc toi la China'
country = regex_var.search(str)
ic(country.group(0))
ic(country.group(2))

# (mongo)*DB none or many
# (mongo)+DB one or many

# matching everything (.*)
# [jfijig] find all charater in the list
# [^jfijig] find all charater not in the list

regex_var.findall(str) #find all groups in str either has or not

re.compile('.*') # search the first line of esssay-string

begin_with = re.compile(r'^spam')
end_with = re.compile(r'spam$')




