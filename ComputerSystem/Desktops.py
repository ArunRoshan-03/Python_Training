from ComputerSystem.Computer import Computer


class Desktops(Computer):

    def __init__(self, brand, model, price, USB_ports):
        super().__init__(brand, model, price)
        self.USB_ports = USB_ports

    def upgrade_ram(self, ram_size):
        print(f"Upgrading RAM to {ram_size} GB")
        