from gen1 import Generator1
from gen2 import Generator2
from gen3 import Generator3

num_of_values = 10000
bins = 20
num_of_test = 2
list_of_lambda = [0.5, 1, 2]

for lambda_val in list_of_lambda:
    print(f'\t###__Lambda = {lambda_val}__###')
    generator_1 = Generator1(lambda_val, num_of_values)
    generator_1.analyze(bins)
    print()

list_of_alpha = [0, 5]
list_of_sigma = [1, 2]

for i in range(0, len(list_of_alpha)):
    for j in range(0, len(list_of_sigma)):
        print(f'\t###__Alpha = {list_of_alpha[i]}; Sigma = {list_of_sigma[j]}__###')
        generator_2 = Generator2(list_of_alpha[i], list_of_sigma[j], num_of_values)
        generator_2.analyze(bins)
        print()


list_of_a = [5**13, 7**5]
list_of_c = [2**31, 2**29]

for i in range(0, len(list_of_a)):
    for j in range(0, len(list_of_c)):
        print(f'\t###__A = {list_of_a[i]}; C = {list_of_c[j]}__###')
        generator_3 = Generator3(num_of_values, list_of_a[i], list_of_c[j])
        generator_3.analyze(bins)
        print()

