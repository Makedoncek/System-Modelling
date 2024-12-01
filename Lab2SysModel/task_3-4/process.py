import sys
from element import Element


class Process(Element):

    def __init__(self, delay):
        super().__init__(delay)
        self.queue = 0
        self.max_queue = sys.maxsize
        self.mean_queue = 0.0
        self.tnext = float('inf')
        self.failure = 0
        self.processed = 0

    def in_act(self):
        if self.state == 0:
            self.state = 1
            self.tnext = self.tcurr + self.get_delay()
        else:
            if self.queue < self.max_queue:
                self.queue += 1
            else:
                self.failure += 1

    def out_act(self):
        super().out_act()
        self.processed += 1
        self.tnext = float('inf')
        self.state = 0
        if self.queue > 0:
            self.queue -= 1
            self.state = 1
            self.tnext = self.tcurr + self.get_delay()
        if self.next_element:
            self.next_element.in_act()

    def print_info(self):
        super().print_info()
        print(f'queue: {self.queue}, failure: {self.failure}')

    def do_statistics(self, delta):
        self.mean_queue += self.queue * delta

    def get_mean_queue(self, total_time):
        return self.mean_queue / total_time if total_time > 0 else 0

    def get_failure_probability(self):
        return self.failure / (self.failure + self.processed) if self.processed > 0 else 0
