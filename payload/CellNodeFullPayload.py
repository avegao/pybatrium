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

        data_parsed['MinCellVolt'] = Payload.clean_voltage(data_parsed.get('MinCellVolt'))
        data_parsed['MaxCellVolt'] = Payload.clean_voltage(data_parsed.get('MaxCellVolt'))
        data_parsed['MinCellTemp'] = Payload.clean_temperature(data_parsed.get('MinCellTemp'))
        data_parsed['BypassTemp'] = Payload.clean_temperature(data_parsed.get('BypassTemp'))
        data_parsed['BypassAmp'] = Payload.clean_voltage(data_parsed.get('BypassAmp'))
        data_parsed['LoCellVoltAlert'] = Payload.clean_voltage(data_parsed.get('LoCellVoltAlert'))
        data_parsed['HiCellVoltAlert'] = Payload.clean_voltage(data_parsed.get('HiCellVoltAlert'))
        data_parsed['BypassVoltLevel'] = Payload.clean_voltage(data_parsed.get('BypassVoltLevel'))
        data_parsed['BypassAmpLimit'] = Payload.clean_voltage(data_parsed.get('BypassAmpLimit'))
        data_parsed['BypassTempLimit'] = Payload.clean_temperature(data_parsed.get('BypassTempLimit'))
        data_parsed['HiCellTempAlert'] = Payload.clean_temperature(data_parsed.get('HiCellTempAlert'))
        data_parsed['BypassSessionAh'] = Payload.clean_voltage(data_parsed.get('BypassSessionAh'))

        return data_parsed
