from task_2.create import Create
from task_2.model import ModelBank
from task_2.process import Process
import task_2.random_gen as random_gen


print('Bank model')
c1 = Create(delay_mean=0.5, name='CREATOR', distribution='exp')
p1 = Process(max_queue=3, delay_mean=0.3, name='CASHIER_1', distribution='exp')
p2 = Process(max_queue=3, delay_mean=0.3, name='CASHIER_2', distribution='exp')

c1.next_element = [p1, p2]

# Обидва касири зайняті
p1.state[0] = 1
p2.state[0] = 1

# Тривалість
# обслуговування для кожного касира нормально розподілена з
# математичним очікуванням, рівним 1 од. часу, і середньоквадратичним
# відхиленням, рівним 0,3 од. часу
p1.t_next[0] = random_gen.norm(1, 0.3)
p2.t_next[0] = random_gen.norm(1, 0.3)

# Прибуття першого клієнта заплановано на момент часу 0,1 од. часу
c1.t_next[0] = 0.1

# У кожній черзі очікують по два автомобіля.
p1.queue = 2
p2.queue = 2

element_list = [c1, p1, p2]
bank = ModelBank(element_list, balancing=[p1, p2])
bank.simulate(1000)

