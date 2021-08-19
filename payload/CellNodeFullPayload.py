from typing import Dict

from construct import Padding, Int8ub, Int16ul, Enum, Struct, Flag, Timestamp, Int32ul

from payload.Payload import Payload


class CellNodeFullPayload(Payload):
    @staticmethod
    def parse(data: bytes) -> Dict:
        parser = Struct(
            Padding(8),
            'ID' / Int8ub,
            'USN' / Int8ub,
            'MinCellVolt' / Int16ul,
            'MaxCellVolt' / Int16ul,
            'MinCellTemp' / Int8ub,
            'BypassTemp' / Int8ub,
            'BypassAmp' / Int16ul,
            'DataErrorCounter' / Int8ub,
            'ResetCounter' / Int8ub,
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
            'IsOverdue' / Flag,
            'LoCellVoltAlert' / Int16ul,
            'HiCellVoltAlert' / Int16ul,
            'BypassVoltLevel' / Int16ul,
            'BypassAmpLimit' / Int16ul,
            'BypassTempLimit' / Int8ub,
            'HiCellTempAlert' / Int8ub,
            'RawVoltCalOffset' / Int8ub,
            'FwVers' / Int16ul,
            'HwVers' / Int16ul,
            'BootVers' / Int16ul,
            'SerialNo' / Int32ul,
            'BypassInitialDate' / Timestamp(Int32ul, 1., 1970),
            # 'BypassInitialDate' / Int32ul,
            'BypassSessionAh' / Int8ub,
            'RepeatCellV' / Int8ub,
        )

        data_parsed = parser.parse(data)

        data_parsed['MinCellVolt'] = data_parsed.get('MinCellVolt') / 1000
        data_parsed['MaxCellVolt'] = data_parsed.get('MaxCellVolt') / 1000
        data_parsed['MinCellTemp'] = data_parsed.get('MinCellTemp') - 40
        data_parsed['BypassTemp'] = data_parsed.get('BypassTemp') - 40
        data_parsed['BypassAmp'] = data_parsed.get('BypassAmp') / 1000
        data_parsed['LoCellVoltAlert'] = data_parsed.get('LoCellVoltAlert') / 1000
        data_parsed['HiCellVoltAlert'] = data_parsed.get('HiCellVoltAlert') / 1000
        data_parsed['BypassVoltLevel'] = data_parsed.get('BypassVoltLevel') / 1000
        data_parsed['BypassAmpLimit'] = data_parsed.get('BypassAmpLimit') / 1000
        data_parsed['BypassTempLimit'] = data_parsed.get('BypassTempLimit') - 40
        data_parsed['HiCellTempAlert'] = data_parsed.get('HiCellTempAlert') - 40
        data_parsed['BypassSessionAh'] = data_parsed.get('BypassSessionAh') / 1000

        return data_parsed
