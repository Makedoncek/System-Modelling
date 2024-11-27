from element import Element


class Create(Element):

    def __init__(self, delay):
        super().__init__(delay)
        self.tnext = 0.0

    def out_act(self):
        super().out_act()
        self.tnext = self.tcurr + self.get_delay()
        if self.next_element is not None:
            self.next_element.in_act()
