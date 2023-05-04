from ComputerSystem.Desktops import Desktops
from ComputerSystem.Laptop import Laptop
from ComputerSystem.Tablets import Tablets


class RunnerClass:

    desktop = Desktops("Dell", "OptiPlex", 999.99, 4)
    print(desktop)
    desktop.upgrade_ram(8)

    laptop = Laptop("Apple", "MacBook Air", 1299.99, 12)
    print(laptop)
    laptop.hibernate()

    tablet = Tablets("Samsung", "Galaxy Tab", 499.99, 10.5)
    print(tablet)
    tablet.take_photo()
