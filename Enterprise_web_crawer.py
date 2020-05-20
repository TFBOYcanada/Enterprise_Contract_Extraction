import logging

pkd='//*[@id="book"]/div/div[2]/div[2]/div[1]/div/div[{LR:}]/table/tbody/tr[{row:}]/td[{col:}]/button'



print(pkd.format(LR=1,row=1,col=7))