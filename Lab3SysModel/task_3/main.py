from task_3.create import CreateHospital
from task_3.dispose import DisposeHospital
from task_3.model import ModelHospital
from task_3.process import ProcessHospital


print('Hospital model')
c1 = CreateHospital(delay_mean=15.0, name='CREATOR_1', distribution='exp')
p1 = ProcessHospital(max_queue=100, n_channel=2, name='RECEPTION', distribution='exp')
p2 = ProcessHospital(max_queue=100, delay_mean=3.0, delay_dev=8, n_channel=3, name='FOLLOWING_TO_THE_WARD',
                     distribution='unif')
p3 = ProcessHospital(max_queue=0, delay_mean=2.0, delay_dev=5, n_channel=10, name='FOLLOWING_TO_THE_LAB_RECEPTION',
                     distribution='unif')
p4 = ProcessHospital(max_queue=100, delay_mean=4.5, delay_dev=3, n_channel=1, name='LAB_REGISTRY',
                     distribution='erlang')
p5 = ProcessHospital(max_queue=100, delay_mean=4.0, delay_dev=2, n_channel=2, name='EXAMINATION',
                     distribution='erlang')
p6 = ProcessHospital(max_queue=0, delay_mean=2.0, delay_dev=5, n_channel=10, name='FOLLOWING_TO_THE_RECEPTION',
                     distribution='unif')

d1 = DisposeHospital(name='EXIT1')
d2 = DisposeHospital(name='EXIT2')

c1.next_element = [p1]
p1.next_element = [p2, p3]
p2.next_element = [d1]
p3.next_element = [p4]
p4.next_element = [p5]
p5.next_element = [d2, p6]
p6.next_element = [p1]

p1.prior_types = [1]

p1.required_path = [[1], [2, 3]]
p5.required_path = [[3], [2]]

elements = [c1, p1, p2, p3, p4, p5, p6, d1, d2]

model = ModelHospital(elements)
model.simulate(1000)

