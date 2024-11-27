from create import Create
from process import Process
from model import Model

creator = Create(2.0)
processor_1 = Process(2.0)
processor_2 = Process(2.0)
processor_3 = Process(3.0)

creator.next_element = processor_1
processor_1.next_element = processor_2
processor_2.next_element = processor_3
processor_1.max_queue = 5
processor_2.max_queue = 8
processor_3.max_queue = 5

creator.name = 'Creator'
processor_1.name = 'Processor 1'
processor_2.name = 'Processor 2'
processor_3.name = 'Processor 3'
creator.distribution = 'exp'
processor_1.distribution = 'exp'
processor_2.distribution = 'exp'
processor_3.distribution = 'exp'

elements = [creator, processor_1, processor_2, processor_3]
model = Model(elements)
model.simulate(1000.0)
