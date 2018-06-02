import random
import magic_box_brain as brain




def ini():


    input_size = 1

    hidden_layer_1 = 2
    hidden_layer_2 = 3
    hidden_layer_3 = 2

    output_size = 1


    layer_1 = [[random.random() for _ in range(input_size)]
                     for _ in range(hidden_layer_1)]

    layer_2 = [[random.random() for _ in range(hidden_layer_1)]
                     for _ in range(hidden_layer_2)]

    layer_3 = [[random.random() for _ in range(hidden_layer_2)]
                     for _ in range(hidden_layer_3)]

    new_output_layer = [[random.random() for _ in range(hidden_layer_3)]
                     for _ in range(output_size)]



    new_network = [layer_1, layer_2, layer_3, new_output_layer]
    return new_network


def input_feed(network, distance):
    return brain.feed_forward(network, [distance])


def learn(network, outputs):

    for output in outputs:
        if output < 0.5:
            network = brain.backpropagate(network, [output], [1])
        else:
            network = brain.backpropagate(network,[output], [0])

    return network
