from manim import *

class NeuralNetwork(Scene):
    def construct(self):
        layers = [3, 4, 2]
        layer_spacing = 2.5
        neuron_radius = 0.3
        neuron_spacing = 1
        
        layers_circles = []
        
        # Draw the neurons
        for layer_index, layer_size in enumerate(layers):
            layer_neurons = []
            for neuron_index in range(layer_size):
                neuron = Circle(radius=neuron_radius, fill_color=BLUE, fill_opacity=0.8)
                neuron.shift(LEFT * layer_spacing * (len(layers) - 1) / 2 + layer_index * layer_spacing)
                neuron.shift(UP * neuron_spacing * (layer_size - 1) / 2 - neuron_spacing * neuron_index)
                layer_neurons.append(neuron)
                self.play(Create(neuron))
            layers_circles.append(layer_neurons)
        
        # Draw the connections
        for layer_index in range(len(layers) - 1):
            for neuron1 in layers_circles[layer_index]:
                for neuron2 in layers_circles[layer_index + 1]:
                    connection = Line(neuron1.get_center(), neuron2.get_center(), buff=neuron_radius)
                    self.play(Create(connection))

        self.wait(2)
