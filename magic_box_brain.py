import math




def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))



def sigmoid(t):
    return 1 / (1 + math.exp(-t))

def neuron_output(weights, inputs):
    return sigmoid(dot(weights, inputs))


def feed_forward(neural_network, input_vector):

    outputs = []

    for layer in neural_network:

        input_with_bias = input_vector + [1]
        output = [neuron_output(neuron, input_with_bias)
                  for neuron in layer]
        outputs.append(output)

        input_vector = output

    return outputs


def backpropagate(network, input_vector, target):
    hidden_layer_1, hidden_layer_2, hidden_outputs, outputs = feed_forward(network, input_vector)

    output_deltas = [output * (1 - output) * (output - target[i]) for i, output in enumerate(outputs)]

    hidden_layer_1_deltas = [hidden_output * (1 - hidden_output) * dot(output_deltas, [n[i] for n in network[-3]]) for i, hidden_output in enumerate(hidden_layer_1)]
    hidden_layer_2_deltas = [hidden_output * (1 - hidden_output) * dot(hidden_layer_1_deltas, [n[i] for n in network[-2]]) for i, hidden_output in enumerate(hidden_layer_2)]
    hidden_layer_3_deltas = [hidden_output * (1 - hidden_output) * dot(hidden_layer_2_deltas, [n[i] for n in network[-1]]) for i, hidden_output in enumerate(hidden_outputs)]


    for i, output_neuron in enumerate(network[-1]):
        for j, hidden_output in enumerate(hidden_outputs):
            output_neuron[j] -= output_deltas[0] * hidden_output



    hidden_deltas = [hidden_output * (1 - hidden_output) *
                     dot(output_deltas, [n[i] for n in network[-1]])
                     for i, hidden_output in enumerate(hidden_outputs)]

    for i, hidden_neuron in enumerate(network[0]):
        for j, in_put in enumerate(input_vector):
            hidden_neuron[j] -= hidden_deltas[0] * in_put

    for i, hidden_neuron in enumerate(network[0]):
        for j, in_put in enumerate(input_vector):
            hidden_neuron[j] -= hidden_layer_1_deltas[i] * in_put

    for i, hidden_neuron in enumerate(network[1]):
        for j, in_put in enumerate(input_vector):
            hidden_neuron[j] -= hidden_layer_2_deltas[i] * in_put

    for i, hidden_neuron in enumerate(network[2]):
        for j, in_put in enumerate(input_vector):
            hidden_neuron[j] -= hidden_layer_3_deltas[i] * in_put

    return network


