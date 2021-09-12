from connector import InputConnector, OutputConnector


class Gate:
    def __init__(self, input_count, output_count):
        self.id = hash(self)
        self.input_connector_count = input_count
        self.output_connector_count = output_count
        self.input_connectors = [InputConnector(self) for i in range(input_count)]
        self.output_connectors = [OutputConnector(self) for i in range(output_count)]

    def check_all_received(self):
        all_received = True
        for connector in self.input_connectors:
            if not connector.received:
                all_received = False
                break
        return all_received

    def get_input_connector(self, number):
        return self.input_connectors[number]

    def get_output_connector(self, number):
        return self.output_connectors[number]

    def reset_input(self):
        for connector in self.input_connectors:
            connector.reset()


class UserInputBar(Gate):
    def __init__(self, connector_number):
        super(UserInputBar, self).__init__(0, connector_number)
        self.connector_count = connector_number

    def start_sending(self):
        for i in range(self.connector_count):
            self.get_output_connector(i).send_signal()

    def set_content(self, serial_number, signal):
        self.get_output_connector(serial_number).set_content(signal)


class UserOutputBar(Gate):
    def __init__(self, connector_number, print_out=False, print_format=0):
        """print format 0: Boolean 1: binary 2: number in decimal"""
        super(UserOutputBar, self).__init__(connector_number, connector_number)
        self.connector_count = connector_number
        self.print_out_received = print_out
        self.print_out_format = print_format

    def set_print(self, print_out):
        self.print_out_received = print_out

    def check_input(self):
        if self.check_all_received():
            if self.print_out_received:
                print("Output Bar #%s received: " % self.id, end="")
                output = ""
                if self.print_out_format == 2:
                    output += "(base 10) "
                    for i in range(self.connector_count-1, -1, -1):
                        if self.get_input_connector(i).get_content():
                            output += "1"
                        else:
                            output += "0"
                    print(int(output, 2))
                elif self.print_out_format == 1:
                    output += "0b"
                    for i in range(self.connector_count-1, -1, -1):
                        if self.get_input_connector(i).get_content():
                            output += "1"
                        else:
                            output += "0"
                    print(output)
                elif self.print_out_format == 0:
                    print("\n")
                    for i in range(self.connector_count):
                        print("Connector #%s:%s" % (self.get_input_connector(i).id,
                                                    self.get_input_connector(i).get_content()))

            for i in range(self.connector_count):
                # print(self.get_input_connector(i).get_content())
                self.get_output_connector(i).set_content(self.get_input_connector(i).get_content())
                self.get_input_connector(i).reset()
                self.get_output_connector(i).send_signal()


class NotGate(Gate):
    def __init__(self):
        super(NotGate, self).__init__(1, 1)

    def check_input(self):
        if self.check_all_received():
            signal = not self.get_input_connector(0).get_content()
            self.reset_input()
            self.get_output_connector(0).set_content(signal)
            self.get_output_connector(0).send_signal()


class AndGate(Gate):
    def __init__(self):
        super(AndGate, self).__init__(2, 1)

    def check_input(self):
        if self.check_all_received():
            signal = self.get_input_connector(0).get_content() and self.get_input_connector(1).get_content()
            self.reset_input()
            self.get_output_connector(0).set_content(signal)
            self.get_output_connector(0).send_signal()


class OrGate(Gate):
    def __init__(self):
        super(OrGate, self).__init__(2, 1)

    def check_input(self):
        if self.check_all_received():
            signal = self.get_input_connector(0).get_content() or self.get_input_connector(1).get_content()
            self.reset_input()
            self.get_output_connector(0).set_content(signal)
            self.get_output_connector(0).send_signal()


class NotAndGate(Gate):
    def __init__(self):
        super(NotAndGate, self).__init__(2, 1)

    def check_input(self):
        if self.check_all_received():
            signal = not (self.get_input_connector(0).get_content() and self.get_input_connector(1).get_content())
            self.reset_input()
            self.get_output_connector(0).set_content(signal)
            self.get_output_connector(0).send_signal()


class NotOrGate(Gate):
    def __init__(self):
        super(NotOrGate, self).__init__(2, 1)

    def check_input(self):
        if self.check_all_received():
            signal = not (self.get_input_connector(0).get_content() or self.get_input_connector(1).get_content())
            self.reset_input()
            self.get_output_connector(0).set_content(signal)
            self.get_output_connector(0).send_signal()


class XorGate(Gate):
    def __init__(self):
        super(XorGate, self).__init__(2, 1)

    def check_input(self):
        if self.check_all_received():
            signal = self.get_input_connector(0).get_content() ^ self.get_input_connector(1).get_content()
            self.reset_input()
            self.get_output_connector(0).set_content(signal)
            self.get_output_connector(0).send_signal()


class XNorGate(Gate):
    def __init__(self):
        super(XNorGate, self).__init__(2, 1)

    def check_input(self):
        if self.check_all_received():
            signal = not (self.get_input_connector(0).get_content() ^ self.get_input_connector(1).get_content())
            self.reset_input()
            self.get_output_connector(0).set_content(signal)
            self.get_output_connector(0).send_signal()


class HalfAdder(Gate):
    """
    Output side:
    connector 0:unit
    connector 1:carry
    """
    def __init__(self):
        super(HalfAdder, self).__init__(2, 2)

    def check_input(self):
        if self.check_all_received():
            sig1 = self.get_input_connector(0).get_content()
            sig2 = self.get_input_connector(1).get_content()
            self.reset_input()
            unit = sig1 ^ sig2
            carry = sig1 and sig2
            self.get_output_connector(0).set_content(unit)
            self.get_output_connector(1).set_content(carry)
            self.get_output_connector(0).send_signal()
            self.get_output_connector(1).send_signal()


class FullAdder(Gate):
    """
    Output side:
    connector 0:unit
    connector 1:carry
    """
    def __init__(self):
        super(FullAdder, self).__init__(3, 2)

    def check_input(self):
        if self.check_all_received():
            sig1 = self.get_input_connector(0).get_content()
            sig2 = self.get_input_connector(1).get_content()
            sig3 = self.get_input_connector(2).get_content()
            self.reset_input()
            temp_unit = sig1 ^ sig2
            temp_carry = sig1 and sig2
            unit = temp_unit ^ sig3
            carry = temp_carry or (temp_unit and sig3)
            self.get_output_connector(0).set_content(unit)
            self.get_output_connector(1).set_content(carry)
            self.get_output_connector(0).send_signal()
            self.get_output_connector(1).send_signal()
