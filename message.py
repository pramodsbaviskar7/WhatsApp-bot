from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
name = input("enter the users name")
message = input("enter your message")
count = int(input("etner the count"))
input('enter anything after scanning QR code')
user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name('DuUXI')
for i in range(count):
    msg_box.send_keys(message)
    button= driver.find_element_by_class_name('_2Ujuu')
    button.click()
