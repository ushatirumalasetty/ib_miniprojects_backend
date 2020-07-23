from slot_booking.interactors.storages.dtos import *
import pytest
from slot_booking.constants.enums import *
from datetime import time

@pytest.fixture()
def washing_machine_dtos():
    washing_machine_dtos = [WashingMachineDto(
        washing_machine_id="wm1",
        status=Days.SUNDAY.value

    )]
    return washing_machine_dtos

@pytest.fixture()
def previous_or_upcomming_slots_dto():
    previous_or_upcomming_slots_dto = [
            PreviousOrUpcommingSlotsDto(
                start_time=time(8).strftime("%H:%M%p"),
                end_time=time(9).strftime("%H:%M%p"),
                washing_machine_id="wm1",
                date=date(2020,12,2)),
            PreviousOrUpcommingSlotsDto(
                start_time=time(9).strftime("%H:%M%p"),
                end_time=time(10).strftime("%H:%M%p"),
                washing_machine_id="wm2",
                date=date(2020,12,2))
        ]
    return previous_or_upcomming_slots_dto