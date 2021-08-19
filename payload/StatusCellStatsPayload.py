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
        data['MinCellVolt'] = data.get('MinCellVolt') / 1000
        data['MaxCellVolt'] = data.get('MaxCellVolt') / 1000
        data['MinCellTemp'] = data.get('MinCellTemp') - 40
        data['MaxCellTemp'] = data.get('MaxCellTemp') - 40
        data['MinBypassAmp'] = data.get('MinBypassAmp') / 1000
        data['MaxBypassAmp'] = data.get('MaxBypassAmp') / 1000
        data['MinBypassTemp'] = data.get('MinBypassTemp') - 40
        data['MaxBypassTemp'] = data.get('MaxBypassTemp') - 40
        data['MinBypassTempId'] = data.get('MinBypassTempId') - 40
        data['MaxBypassTempId'] = data.get('MaxBypassTempId') - 40
