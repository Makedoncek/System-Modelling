from task_1.element import Element


class Create(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def out_act(self):
        # виконуємо збільшення лічильника кількості
        super().out_act()
        # встановлюємо коли пристрій буде вільним
        self.t_next[0] = self.t_curr + super().get_delay()

        # пріоритетність чи ймовірність
        next_element = self.choose_next_element()
        next_element.in_act()