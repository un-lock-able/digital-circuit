class Connector:
    def __init__(self, belong_to):
        self.id = hash(self)
        self.connector_of = belong_to
        self.connected_wires = []
        self.content = False
        self.connection_count = 0

    def remove_wire(self, target_wire):
        self.connected_wires.remove(target_wire)
        self.connection_count -= 1


class InputConnector(Connector):
    def __init__(self, belong_to):
        super(InputConnector, self).__init__(belong_to)
        self.received = False

    def connect_to_receiver(self, wire):
        """this is a method for wire to connect to THIS connector"""
        if self.connection_count == 0:
            self.connected_wires.append(wire)
            self.connection_count += 1
        elif self.connection_count == 1:
            print("Already Connected!")
        else:
            print("An Error has occurred")

    def is_available(self):
        if self.connection_count == 0:
            return True
        else:
            return False

    def receive_from_wire(self, signal):
        print("Connector id#%s: Receiving %s from wire id#%s" % (self.id, signal, self.connected_wires[0].id))
        self.content = signal
        self.received = True
        self.connector_of.check_input()

    def get_content(self):
        return self.content

    def reset(self):
        self.received = False


class OutputConnector(Connector):
    def __init__(self, belong_to):
        super(OutputConnector, self).__init__(belong_to)

    def connect_to_sender(self, wire):
        self.connected_wires.append(wire)

    def set_content(self, signal):
        self.content = signal

    def send_signal(self):
        for wire in self.connected_wires:
            print("Connector id#%d: Sending %s to Wire id#%s" % (self.id, self.content, wire.id))
            wire.send_to_connector(self.content)
