import sys
import random
from element import Element


class Process(Element):

    def __init__(self, delay, num_devices=1):
        super().__init__(delay)
        self.queue = 0
        self.max_queue = sys.maxsize
        self.mean_queue = 0.0
        self.failure = 0
        self.processed = 0
        self.num_devices = num_devices
        self.devices_state = [0] * self.num_devices
        self.tnext_devices = [float('inf')] * self.num_devices
        self.next_elements = []
        self.reverse_element = None
        self.reverse_probability = 0.0

    def in_act(self):
        free_device = next((i for i, state in enumerate(self.devices_state) if state == 0), None)
        if free_device is not None:
            self.devices_state[free_device] = 1
            self.tnext_devices[free_device] = self.tcurr + self.get_delay()
        else:
            if self.queue < self.max_queue:
                self.queue += 1
            else:
                self.failure += 1

    def out_act(self):
        device = self.tnext_devices.index(min(self.tnext_devices))
        super().out_act()
        self.processed += 1
        self.devices_state[device] = 0
        self.tnext_devices[device] = float('inf')
        if self.queue > 0:
            self.queue -= 1
            self.devices_state[device] = 1
            self.tnext_devices[device] = self.tcurr + self.get_delay()
        if self.reverse_element and random.random() < self.reverse_probability:
            self.reverse_element.in_act()
        else:
            if self.next_elements:
                next_element = random.choice(self.next_elements)
                next_element.in_act()

    def add_next_element(self, element):
        self.next_elements.append(element)

    def set_reverse_route(self, element, probability):
        self.reverse_element = element
        self.reverse_probability = probability

    def print_info(self):
        super().print_info()
        print(f'queue: {self.queue}, failure: {self.failure}, devices: {self.devices_state}')

    def do_statistics(self, delta):
        self.mean_queue += self.queue * delta

    def get_mean_queue(self, total_time):
        return self.mean_queue / total_time if total_time > 0 else 0

    def get_failure_probability(self):
        return self.failure / self.processed if self.processed > 0 else 0

    def has_pending_events(self):
        return self.queue > 0 or any(state == 1 for state in self.devices_state)

