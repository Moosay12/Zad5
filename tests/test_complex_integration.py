from src.models import Apartment
from src.manager import Manager 
from src.manager import Parameters
def test_get_apartment_costs():
    parameters = Parameters()
    manager = Manager(parameters)
    assert manager.get_apartment_costs('apart-polanka', 2025, 1) == 910.00
    assert manager.get_apartment_costs('apart-polanka', 2025, 20) == 0
    assert manager.get_apartment_costs('nic', 2025, 1) == None