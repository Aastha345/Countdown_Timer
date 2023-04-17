import time

class CountdownTimer:
    def _init_(self, duration):
        self.duration = duration
        self.start_time = None
        self.remaining_time = None
        self.is_running = False
        
    def start(self):
        if self.is_running:
            print("Timer is already running.")
        else:
            self.start_time = time.time()
            self.remaining_time = self.duration
            self.is_running = True
            while self.remaining_time > 0:
                if not self.is_running:
                    break
                print("Time remaining: {} seconds".format(self.remaining_time))
                time.sleep(1)
                self.remaining_time -= 1
            if self.is_running:
                print("Time's up!")
                self.is_running = False
        
    def stop(self):
        if self.is_running:
            self.remaining_time = int(self.remaining_time - (time.time() - self.start_time))
            self.is_running = False
            print("Timer stopped. Time remaining: {} seconds".format(self.remaining_time))
        else:
            print("Timer is not running.")
        
    def resume(self):
        if self.is_running:
            print("Timer is already running.")
        else:
            self.start_time = time.time()
            self.is_running = True
            while self.remaining_time > 0:
                if not self.is_running:
                    break
                print("Time remaining: {} seconds".format(self.remaining_time))
                time.sleep(1)
                self.remaining_time -= 1
            if self.is_running:
                print("Time's up!")
                self.is_running = False
        
    def reset(self):
        self.start_time = None
        self.remaining_time = None
        self.is_running = False
        print("Timer reset.")