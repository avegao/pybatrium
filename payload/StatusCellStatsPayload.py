from typing import Dict

from construct import Struct, Padding, Int8ub, Computed, Int16ul, Float16b

from payload import Payload


class StatusCellStatsPayload(Payload):
    @staticmethod
    def parse(data: bytes) -> Dict:
        parser = Struct(
            Padding(8),
            'MinCellVolt' / Int16ul,
            'MaxCellVolt' / Int16ul,
            'MinCellVoltId' / Int8ub,
            'MaxCellVoltId' / Int8ub,
            'MinCellTemp' / Int8ub,
            'MaxCellTemp' / Int8ub,
            'MinCellTempId' / Int8ub,
            'MaxCellTempId' / Int8ub,
            'MinBypassAmp' / Int16ul,
            'MaxBypassAmp' / Int16ul,
            'MinBypassAmpId' / Int8ub,
            'MaxBypassAmpId' / Int8ub,
            'MinBypassTemp' / Int8ub,
            'MaxBypassTemp' / Int8ub,
            'MinBypassTempId' / Int8ub,
            'MaxBypassTempId' / Int8ub,
            'AvgCellVolt' / Int16ul,
            'AvgCellTemp' / Int8ub,
            'NumOfCellsAboveInitialBypass' / Int8ub,
            'NumOfCellsAboveFinalBypass' / Int8ub,
            'NumOfCellsInBypass' / Int8ub,
            'NumOfCellsOverdue' / Int8ub,
            'NumOfCellsActive' / Int8ub,
            'NumOfCellsInSystem' / Int8ub,
            Padding(1),
            'MinBypassSession' / Float16b,
            'MaxBypassSession' / Float16b,
            'MinBypassSessionID' / Int8ub,
            'MaxBypassSessionID' / Int8ub,
        )

        data_parsed = parser.parse(data)

        StatusCellStatsPayload.clean_data(data_parsed)

        return data_parsed

    @staticmethod
    def clean_data(data: Dict) -> None:
        data['MinCellVolt'] = Payload.clean_voltage(data.get('MinCellVolt'))
        data['MaxCellVolt'] = Payload.clean_voltage(data.get('MaxCellVolt'))
        data['MinCellTemp'] = Payload.clean_temperature(data.get('MinCellTemp'))
        data['MaxCellTemp'] = Payload.clean_temperature(data.get('MaxCellTemp'))
        data['MinBypassAmp'] = Payload.clean_voltage(data.get('MinBypassAmp'))
        data['MaxBypassAmp'] = Payload.clean_voltage(data.get('MaxBypassAmp'))
        data['MinBypassTemp'] = Payload.clean_temperature(data.get('MinBypassTemp'))
        data['MaxBypassTemp'] = Payload.clean_temperature(data.get('MaxBypassTemp'))
        data['MinBypassTempId'] = Payload.clean_temperature(data.get('MinBypassTempId'))
        data['MaxBypassTempId'] = Payload.clean_temperature(data.get('MaxBypassTempId'))
        data['AvgCellVolt'] = Payload.clean_voltage(data.get('AvgCellVolt'))
        data['AvgCellTemp'] = Payload.clean_temperature(data.get('AvgCellTemp'))
