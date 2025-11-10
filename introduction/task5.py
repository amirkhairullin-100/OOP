class BigBell:
    def __init__(self):
        self._is_ding = True  # Начинаем с "ding"
    def sound(self):
        if self._is_ding:
            print("ding")
            self._is_ding = False
        else:
            print("dong")
            self._is_ding = True
bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
