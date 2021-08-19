from typing import Dict

from construct import Struct, Padding, Int8ub, Int16ul, Enum, Array, this

from payload.Payload import Payload


class CellNodeStatusPayload(Payload):
    @staticmethod
    def parse(data: bytes) -> Dict:
        parser = Struct(
            Padding(8),
            'CmuRxOpStatusNodeID' / Int8ub,
            'Records' / Int8ub,
            'FirstNodeID' / Int8ub,
            'LastNodeID' / Int8ub,
            'nodes' / Array(this.Records, Struct(
                'ID' / Int8ub,
                'USN' / Int8ub,
                'MinCellVolt' / Int16ul,
                'MaxCellVolt' / Int16ul,
                'MinCellTemp' / Int8ub,
                'BypassTemp' / Int8ub,
                'BypassAmp' / Int16ul,
                'Status' / Enum(Int8ub,
                                NONE=0,
                                HighVolt=1,
                                HighTemp=2,
                                Ok=3,
                                Timeout=4,
                                LowVolt=5,
                                Disabled=6,
                                InBypass=7,
                                InitialBypass=8,
                                FinalBypass=9,
                                MissingSetup=10,
                                NoConfig=11,
                                CellOutLimits=12,
                                Undefined=255,
                                ),
            )),
        )

        data_parsed = parser.parse(data)

        for node in data_parsed.get('nodes'):
            node['MinCellVolt'] = Payload.clean_voltage(node.get('MinCellVolt'))
            node['MaxCellVolt'] = Payload.clean_voltage(node.get('MaxCellVolt'))
            node['MinCellTemp'] = Payload.clean_temperature(node.get('MinCellTemp'))
            node['BypassTemp'] = Payload.clean_temperature(node.get('BypassTemp'))
            node['BypassAmp'] = Payload.clean_voltage(node.get('BypassAmp'))

        return data_parsed
