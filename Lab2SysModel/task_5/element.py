from random_gen import generate_exponential, generate_normal, generate_uniform


class Element:
    next_id = 0

    def __init__(self, delay=1.0):
        self.tnext = 0.0
        self.delay_mean = delay
        self.distribution = 'exp'
        self.tcurr = self.tnext
        self.state = 0
        self.next_element = None
        self.id_ = Element.next_id
        Element.next_id += 1
        self.delay_std = 0.0
        self.quantity = 0

    def get_delay(self):
        if self.distribution == 'exp':
            return generate_exponential(self.delay_mean)
        elif self.distribution == 'norm':
            return generate_normal(self.delay_mean, self.delay_std)
        elif self.distribution == 'unif':
            return generate_uniform(self.delay_mean, self.delay_std)
        return self.delay_mean

    def out_act(self):
        self.quantity += 1

    def print_result(self):
        print(f'{self.name} quantity = {self.quantity}')

    def print_info(self):
        print(f'{self.name} state: {self.state}, quantity: {self.quantity}, tnext: {self.tnext}, tcurr: {self.tcurr}')

    def do_statistics(self, delta):
        pass
