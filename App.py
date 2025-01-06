import Chawakorn 
from time import sleep
bot = Chawakorn.Bot('https://docs.google.com/forms/d/e/1FAIpQLSeum8ozQyGW58_REybnQ-7AxSSWFQPRrzQeKNKiqAS5f6kU_g/viewform?usp=preview')
def scroll_to_element(xpath):
    try:
        element = bot.find_element(xpath)
        bot.driver.execute_script("arguments[0].scrollIntoView();", element)
        sleep(1)  
    except Exception as e:
        print(f"Error scrolling to element: {e}")
target_iterations = 40  #เลือกจำนวนครั้ง
count = 0
success_count = 0
failure_count = 0
while count < target_iterations:
    try:
        bot.Start()

        #1
        bot.send_Random_Click([
            '//*[@id="i9"]/div[3]/div',
            '//*[@id="i12"]/div[3]/div',
        ])
        #2
        bot.send_Random_Click([
            '//*[@id="i20"]/div[3]/div',
            '//*[@id="i23"]/div[3]/div',
            '//*[@id="i26"]/div[3]/div',
            '//*[@id="i29"]/div[3]/div',
        ])
        #3
        bot.send_Random_Click([
            '//*[@id="i37"]/div[3]/div',
            '//*[@id="i40"]/div[3]/div',
            '//*[@id="i46"]/div[3]/div',
            '//*[@id="i49"]/div[3]/div',
        ])

        #4
        bot.send_Random_Click([
            '//*[@id="i57"]/div[3]/div',
            '//*[@id="i60"]/div[3]/div',
            '//*[@id="i63"]/div[3]/div',
            '//*[@id="i66"]/div[3]/div',
            '//*[@id="i69"]/div[3]/div',
        ])

   #1
        bot.send_Random_Click([
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div',
    ])

    #2
        bot.send_Random_Click([
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div',
    ])

    #3
        bot.send_Random_Click([
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div',
    ])

    #4
        bot.send_Random_Click([
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div',
    ])

    #5
        bot.send_Random_Click([
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div',
    ])

    #6
        bot.send_Random_Click([
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div',
    ])


        bot.send_Click('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        bot.close()
        count += 1
        success_count += 1
        print(f'สำเร็จครั้งที่ {count}')
    except Exception as e:
        failure_count += 1
        print(f"Error occurred during iteration {count + 1}: {e}")
        bot.close()
print(f"จำนวนครั้งที่สำเร็จ: {success_count}")
print(f"จำนวนครั้งที่ไม่สำเร็จ: {failure_count}")
