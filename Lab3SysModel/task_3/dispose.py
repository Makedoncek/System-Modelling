import numpy as np
from task_3.element import ElementHospital


class DisposeHospital(ElementHospital):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.t_next = [np.inf]
        self.delta_t_finished1 = 0
        self.delta_t_finished2 = 0
        self.delta_t_finished3 = 0
        self.type1_cnt = 0
        self.type2_cnt = 0
        self.type3_cnt = 0

    def in_act(self, next_type_element, t_start):
        if next_type_element == 1:
            self.delta_t_finished1 += self.t_curr - t_start
            self.type1_cnt += 1
        elif next_type_element == 2:
            self.delta_t_finished2 += self.t_curr - t_start
            self.type2_cnt += 1
        elif next_type_element == 3:
            self.delta_t_finished3 += self.t_curr - t_start
            self.type3_cnt += 1
        # виконуємо збільшення лічильника кількості
        super().out_act()