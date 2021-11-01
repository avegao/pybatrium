from enum import Enum, unique
from typing import Dict

from payload.CellNodeFullPayload import CellNodeFullPayload
from payload.CellNodeStatusPayload import CellNodeStatusPayload
from payload.ControlRemoteStatusPayload import ControlRemoteStatusPayload
from payload.StatusCellStatsPayload import StatusCellStatsPayload
from payload.StatusCommsPayload import StatusCommsPayload
from payload.StatusControlLogicPayload import StatusControlLogicPayload
from payload.StatusShuntPayload import StatusShuntPayload


@unique
class PayloadEnum(Enum):
    # STATUS_RAPID = '3e5a'
    STATUS_RAPID = '3e32'
    STATUS_CELL_STATS = '3e33'
    # STATUS_FAST = '3f33'
    STATUS_SHUNT = '3f34'
    HW_SYSTEM_SETUP = '4a36'
    HW_CELL_GROUP_SETUP = '4b36'
    HW_SHUNT_SETUP = '4c34'
    HW_EXPANSION_SETUP = '4d34'
    CONTROL_REMOTE_SETUP = '4e58'
    CONTROL_CRITICAL_SETUP = '4f33'
    CELL_NODE_STATUS = '415a'
    STATUS_CONTROL_LOGIC = '4733'
    LIVE_DISPLAY = '3233'
    STATUS_SLOW = '4033'
    CELL_NODE_FULL = '4232'
    CONTROL_REMOTE_STATUS = '4932'
    CONTROL_CHARGE_SETUP = '5033'
    CONTROL_DISCHARGE_SETUP = '5158'
    CONTROL_THERMAL_SETUP = '5233'
    HW_INTEGRATION_SETUP = '5335'
    SESSION_METRICS = '5431'
    DAILY_SESSION = '5432'
    LIFETIME_METRICS = '5633'
    LIFETIME_METRICS_A = '5635'
    LIFETIME_METRICS_B = '5634'
    SYSTEM_DISCOVERY = '5732'  # deprecated ?
    DAILY_SESSION_HIST = '5831'
    STATUS_COMMS = '6133'
    QUICK_SESSION_HIST = '6861'
    HW_SHUNT_METRICS = '7832'

    @staticmethod
    def parse(message_id: Enum, data: bytes) -> Dict:
        if message_id is PayloadEnum.CELL_NODE_FULL:
            return CellNodeFullPayload.parse(data)
        if message_id is PayloadEnum.CELL_NODE_STATUS:
            return CellNodeStatusPayload.parse(data)
        if message_id is PayloadEnum.STATUS_CELL_STATS:
            return StatusCellStatsPayload.parse(data)
        if message_id is PayloadEnum.STATUS_SHUNT:
            return StatusShuntPayload.parse(data)
        if message_id is PayloadEnum.STATUS_COMMS:
            return StatusCommsPayload.parse(data)
        if message_id is PayloadEnum.CONTROL_REMOTE_STATUS:
            return ControlRemoteStatusPayload.parse(data)
        if message_id is PayloadEnum.STATUS_CONTROL_LOGIC:
            return StatusControlLogicPayload.parse(data)
        else:
            # raise NotImplementedError(f'MessageId {message_id} not implemented')
            pass
