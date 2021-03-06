from selenium import webdriver
from time import sleep
from API import mfa


def driver():
    my_driver = webdriver.Firefox(executable_path="/Users/dordoanis/Downloads/geckodriver")

    # Open Tinder Login site
    my_driver.get("https://tinder.onelink.me/9K8a/3d4abb81")
    sleep(15)

    # Open Tinder Phone option
    my_driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[3]/button/span[2]').click()
    sleep(5)

    # Enter our Phone number 
    phone_num = my_driver.find_element_by_xpath('//*[@id="q1569938320"]/div/div/div[1]/div/div[2]/div/input')
    phone_num.send_keys('<phone>')
    login_continue = my_driver.find_element_by_xpath('//*[@id="q1569938320"]/div/div/div[1]/div/button')
    login_continue.click()

    sleep(10)


    # OTP code
    otp_code = my_driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/input[1]')
    otp_code.click()

    sleep(10)

    # The MFA code that we get from the other function.
    mfa_code = mfa()
    otp_code.send_keys(f'{mfa_code}')

    # The continue button.
    con_botton = my_driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/button')
    con_botton.click()


driver()
