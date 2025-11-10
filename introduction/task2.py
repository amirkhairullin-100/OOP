class Button:
    def __init__(self):
        self.clicks = 0
    def click(self):
        self.clicks += 1
    def click_count(self):
        return self.clicks
    def reset(self):
        self.clicks = 0
button1 = Button()
button1.click()
button1.click()
print(button1.click_count())
button1.click()
print(button1.click_count())
print()
button2 = Button()
button2.click()
button2.click()
print(button2.click_count())
button2.reset()
button2.click()
print(button2.click_count())
print()
button3 = Button()
button3.click()
print(button3.click_count())