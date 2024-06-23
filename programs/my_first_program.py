from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform addition on the secret integers
    sum_ints = my_int1 + my_int2

    # Output the result of the addition
    return [Output(sum_ints, "sum_output", party1)]
