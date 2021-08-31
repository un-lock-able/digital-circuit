class Wire:
    def __init__(self, connect_from, connect_to):
        if connect_to.is_available:
            self.id = hash(self)
            self.start = connect_from
            self.end = connect_to
            self.start.connect_to_sender(self)
            self.end.connect_to_receiver(self)
        else:
            pass

    def send_to_connector(self, signal):
        print("Wire id#%s: sending %s from connector id#%s to connector id#%s" %
              (self.id, signal, self.start.id, self.end.id))
        self.end.receive_from_wire(signal)
        # print("Receiving %s, sending..." % signal)

    def remove_self(self):
        self.start.remove_wire(self)
        self.end.remove_wire(self)
        del self
