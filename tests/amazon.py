from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=610644601173&hvpos=&hvnetw=g&hvrand=14225108286575247184&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061994&hvtargid=kwd-10573980&hydadcr=14453_2316415")
options=driver.find_elements(By.ID,"nav-xshop")
for option in options:
    print(option.text)
