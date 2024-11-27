from process import Process


class Model:
    def __init__(self, elements):
        self.elements = elements
        self.tnext = 0.0
        self.tcurr = 0.0
        self.event = None

    def simulate(self, time_modeling):
        while self.tcurr < time_modeling:
            self.tnext = float('inf')
            for element in self.elements:
                if isinstance(element, Process):
                    min_device_time = min(element.tnext_devices)
                    if min_device_time < self.tnext:
                        self.tnext = min_device_time
                        self.event = element
                elif element.tnext < self.tnext:
                    self.tnext = element.tnext
                    self.event = element

            if self.tnext == float('inf'):
                break

            self.tcurr = self.tnext
            for element in self.elements:
                element.do_statistics(self.tcurr - element.tcurr)
                element.tcurr = self.tcurr

            if isinstance(self.event, Process):
                for i, tnext_device in enumerate(self.event.tnext_devices):
                    if tnext_device == self.tcurr:
                        self.event.out_act()
                        break
            else:
                self.event.out_act()

            for element in self.elements:
                if element.tnext == self.tcurr:
                    element.out_act()

            self.print_info()

        print('------------RESULTS------------')
        for element in self.elements:
            element.print_result()
            if isinstance(element, Process):
                mean_queue = element.get_mean_queue(self.tcurr)
                failure_prob = element.get_failure_probability()
                print(f'Mean length of queue = {mean_queue}')
                print(f'Failure probability = {failure_prob}')

    def print_info(self):
        for element in self.elements:
            element.print_info()
        print(f'Time: {self.tcurr}')

