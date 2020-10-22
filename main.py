import datetime as dt
import notification
import store_data as sd


def help():
    print("To begin your counter please enter: Start\n"
          "To end your day please enter: END\n"
          )


class Pomodoro:
    def __init__(self):
        self.begin = dt.datetime.now()
        self.total_sessions = 0

    def ask_question(self):
        self.question = input("Are You Ready To Begin?: ").upper()

    def track_work_time(self):
        #  check if the user is ready to start his/her 25 minute increment
        if self.question == "START":
            #  if user is ready set a timer
            self.work_time_start = dt.datetime.now()
            print(f"Start Time: {self.work_time_start.strftime('%H:%M')}")
            #  when 25 minutes are up alert user
            while True:
                #  25 minute work increment
                if dt.datetime.now() > self.work_time_start + dt.timedelta(minutes=25):
                    self.total_sessions += 1
                    print(f"\nTotal Sessions: {self.total_sessions}\n")
                    break

    def break_time(self):
        self.break_time_start = dt.datetime.now()
        if timer.total_sessions % 3 == 0:
            notification.notify.long_break()
        else:
            notification.notify.short_break()
        while True:
            if timer.total_sessions % 3 == 0:
                #  Long Break
                if dt.datetime.now() > self.break_time_start + dt.timedelta(minutes=30):
                    break
            else:
                #  Short Break
                if dt.datetime.now() > self.break_time_start + dt.timedelta(minutes=5):
                    break


help()
timer = Pomodoro()
sd.writing_to_file(dt.date.today().strftime('%m-%d-%Y'))
while True:
    timer.ask_question()
    if timer.question != "END":
        timer.track_work_time()
        timer.break_time()
        notification.notify.get_back_to_work()
    else:
        if timer.total_sessions > 1:
            print(f"\n{dt.date.today()}\nYou have worked a total of: {timer.total_sessions * 25} Minutes\n"
                  f"Great Job!")
            sd.writing_to_file("\nTotal Time Coding: {} Minutes\n".format(timer.total_sessions * 25))
            input("Please X out to leave :)")
        break
