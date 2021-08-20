from typing import Dict

from construct import Padding, Struct, Int8ub, Int16ul, Flag, Float32l, Int16sl

from payload import Payload


class StatusShuntPayload(Payload):
    @staticmethod
    def parse(data: bytes) -> Dict:
        parser = Struct(
            Padding(8),
            'SupplyVolt' / Int16ul,
            'AmbientTemp' / Int8ub,
            'ShuntTemp' / Int8ub,
            'ShuntVoltage' / Int16ul,
            'ShuntCurrent' / Float32l,
            'ShuntPowerVA' / Float32l,
            'ShuntSOC' / Int16sl,
            Padding(1),
            'hasShuntSocCountLo' / Flag,
            'hasShuntSocCountHi' / Flag,
            'hasShuntLoSocRecal' / Flag,
            'hasShuntHiSocRecal' / Flag,
            # 'reserved' / Padding(4), # TODO This reserved field broke the next fields
            # 'NomCapacityToFull' / Float32l,
            # 'NomCapacityToEmpty' / Float32l,
            # 'EstDurationToFullmins' / Int16sl,
            # 'EstDurationToEmptymins' / Int16sl,
            # 'ShuntAcculmAvgCharge' / Float32l,
            # 'ShuntAcculmAvgDischg' / Float32l,
            # 'ShuntAcculmAvgNett' / Float32l,
        )

        data_parsed = parser.parse(data)
        StatusShuntPayload.clean_data(data_parsed)

        return data_parsed

    @staticmethod
    def clean_data(data: Dict) -> None:
        data['SupplyVolt'] = Payload.clean_percentage(data.get('SupplyVolt'))
        data['AmbientTemp'] = Payload.clean_temperature(data.get('AmbientTemp'))
        data['ShuntTemp'] = Payload.clean_temperature(data.get('ShuntTemp'))
        data['ShuntVoltage'] = Payload.clean_percentage(data.get('ShuntVoltage'))
        data['ShuntCurrent'] = Payload.clean_amperes(data.get('ShuntCurrent'))
        data['ShuntPowerVA'] = Payload.clean_voltage(data.get('ShuntPowerVA'))
        data['ShuntSOC'] = Payload.clean_percentage(data.get('ShuntSOC'))
        # data['NomCapacityToFull'] = Payload.clean_amperes(data.get('NomCapacityToFull'))
        # data['NomCapacityToEmpty'] = Payload.clean_amperes(data.get('NomCapacityToEmpty'))
        # data['ShuntAcculmAvgCharge'] = Payload.clean_amperes(data.get('ShuntAcculmAvgCharge'))
        # data['ShuntAcculmAvgDischg'] = Payload.clean_amperes(data.get('ShuntAcculmAvgDischg'))
        # data['ShuntAcculmAvgNett'] = Payload.clean_amperes(data.get('ShuntAcculmAvgNett'))
