from wire import Wire
import gate


def make_wire(start_gate, start_port_num, end_gate, end_port_num):
    return Wire(start_gate.get_output_connector(start_port_num),
                end_gate.get_input_connector(end_port_num))


def main():
    '''
    input_bar = gate.UserInputBar(2)
    input_bar.set_content(0, True)
    input_bar.set_content(1, False)
    output_bar = gate.UserOutputBar(1)
    output_bar.set_print(True)
    # Or combine the above two line into output_bar = gate.UserOutputBar(1, True)
    or_gate1 = gate.OrGate()
    or_gate2 = gate.OrGate()
    and_gate = gate.AndGate()
    not_gate1 = gate.NotGate()
    not_gate2 = gate.NotGate()
    wires = []
    wires.append(make_wire(input_bar, 0, or_gate1, 0))
    wires.append(make_wire(input_bar, 1, or_gate1, 1))
    wires.append(make_wire(input_bar, 0, not_gate1, 0))
    wires.append(make_wire(input_bar, 1, not_gate2, 0))
    wires.append(make_wire(not_gate1, 0, or_gate2, 0))
    wires.append(make_wire(not_gate2, 0, or_gate2, 1))
    wires.append(make_wire(or_gate1, 0, and_gate, 0))
    wires.append(make_wire(or_gate2, 0, and_gate, 1))
    wires.append(make_wire(and_gate, 0, output_bar, 0))
    input_bar.start_sending()
    '''
    input_bar=gate.UserInputBar(2)
    output_bar=gate.UserOutputBar(2, print_out=True, print_format=1)
    wires = []
    wires.append(make_wire(input_bar, 0, output_bar, 0))
    wires.append(make_wire(input_bar, 1, output_bar, 1))
    input_bar.set_content(0, True)
    input_bar.start_sending()


if __name__ == '__main__':
    main()
