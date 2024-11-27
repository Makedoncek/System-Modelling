import random_gen


class Model:
    def __init__(self, delay_create, delay_process, max_queue_size=0):
        self.delay_create = delay_create
        self.delay_process = delay_process
        self.tnext = 0.0
        self.tcurr = 0.0
        self.t0 = self.tcurr
        self.t1 = float('inf')
        self.max_queue_size = max_queue_size
        self.state = 0
        self.queue = 0
        self.next_event = 0
        self.num_create = 0
        self.num_process = 0
        self.failure = 0
        self.avg_load = 0

    def simulate(self, time_modeling):
        while self.tcurr < time_modeling:
            self.tnext = self.t0
            self.next_event = 0

            if self.t1 < self.tnext:
                self.tnext = self.t1
                self.next_event = 1

            self.avg_load += self.state * (self.tnext - self.tcurr)
            self.tcurr = self.tnext
            if self.next_event == 0:
                self.event0()
                pass
            elif self.next_event == 1:
                self.event1()
                pass
            self.print_info()
        self.avg_load /= self.tcurr
        self.print_result()

    def print_result(self):
        print(f'Create: {self.num_create} Processed: {self.num_process} Failure: {self.failure}')
        print(f'Average load: {self.avg_load}')

    def print_info(self):
        print(f'Time: {self.tcurr} State: {self.state} Queue: {self.queue}')

    def event0(self):
        self.t0 = self.tcurr + self.get_delay_create()
        self.num_create += 1
        if self.state == 0:
            self.state = 1
            self.t1 = self.tcurr + self.get_delay_process()
        else:
            if self.queue < self.max_queue_size:
                self.queue += 1
            else:
                self.failure += 1

    def event1(self):
        self.t1 = float('inf')
        self.state = 0
        if self.queue > 0:
            self.queue -= 1
            self.state = 1
            self.t1 = self.tcurr + self.get_delay_process()
        self.num_process += 1

    def get_delay_create(self):
        return random_gen.generate_exponential(self.delay_create)

    def get_delay_process(self):
        return random_gen.generate_exponential(self.delay_process)
