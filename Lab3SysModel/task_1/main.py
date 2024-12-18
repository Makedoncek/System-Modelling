from task_1.create import Create
from task_1.model import Model
from task_1.process import Process


def channel_model():
    print('Channel model')
    c1 = Create(delay_mean=5, name='CREATOR', distribution='exp')
    p1 = Process(max_queue=3, n_channel=2, delay_mean=5, distribution='exp')

    c1.next_element = [p1]
    elements = [c1, p1]
    model = Model(elements)
    model.simulate(1000)


def simple_model():
    print('Simple model')
    c1 = Create(delay_mean=5, name='CREATOR', distribution='exp')
    p1 = Process(max_queue=3, delay_mean=5, distribution='exp')

    c1.next_element = [p1]
    elements = [c1, p1]
    model = Model(elements)
    model.simulate(1000)


def probability_model():
    print('Probability model')
    p1 = Process(max_queue=3, delay_mean=5, distribution='exp')

    p1.probability = [0.9, 0.1]
    base_model(p1)


def priority_model():
    print('Priority model')
    p1 = Process(max_queue=3, delay_mean=5, distribution='exp')
    p1.priority = [2, 1]

    base_model(p1)


def base_model(p1):
    c1 = Create(delay_mean=5, name='CREATOR', distribution='exp')
    p2 = Process(max_queue=3, delay_mean=5, distribution='exp')
    p3 = Process(max_queue=3, delay_mean=5, distribution='exp')

    c1.next_element = [p1]
    p1.next_element = [p2, p3]
    elements = [c1, p1, p2, p3]
    model = Model(elements)
    model.simulate(1000)


def main():
    continue_test = "Press Enter to continue..."
    simple_model()
    print("Simple model Results")
    input(continue_test)
    channel_model()
    print("Channel model Results")
    input(continue_test)
    probability_model()
    print("Probability model Results")
    input(continue_test)
    priority_model()
    print("Priority model Results")


if __name__ == "__main__":
    main()