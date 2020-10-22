from wintoast import ToastNotifier
import time


class Notifier:
    def __init__(self):
        self.toaster = ToastNotifier()

    def short_break(self):
        self.toaster.show_toast("5 Minute Break",
                                "Take a 5 minute break and return",
                                icon_path="bank.ico",
                                duration=1)
        while self.toaster.notification_active(): time.sleep(0.1)

    def long_break(self):
        self.toaster.show_toast("30 minute Break",
                                "Take a 30 minute break and return",
                                icon_path="bank.ico",
                                duration=1)
        while self.toaster.notification_active(): time.sleep(0.1)

    def get_back_to_work(self):
        self.toaster.show_toast("Back To Work",
                                "GET BACK TO WORK !",
                                icon_path="bank.ico",
                                duration=1)


notify = Notifier()



