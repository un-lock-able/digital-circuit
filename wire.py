# Copyright 2022 un-lock-able
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
