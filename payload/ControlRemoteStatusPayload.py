from typing import Dict

from construct import Struct, Padding, Int8ul, Timestamp, Int32ul, Int16ul

from payload import Payload


class ControlRemoteStatusPayload(Payload):
    @staticmethod
    def parse(data: bytes) -> Dict:
        parser = Struct(
            Padding(8),
            'CanbusRxStatusTicks' / Int8ul,
            'CanbusRxUnknownTicks' / Int8ul,
            'CanbusTxCmdTicks' / Int8ul,
            'RemoteChargeActualCelcius' / Int8ul,
            'RemoteChargeTargetVolt' / Int16ul,
            'RemoteChargeTargetAmp' / Int16ul,
            'RemoteChargeTargetVA' / Int16ul,
            'RemoteChargeActualVolt' / Int16ul,
            'RemoteChargeActualAmp' / Int16ul,
            'RemoteChargeActualVA' / Int16ul,
            'RemoteChargeActualFlag1' / Int32ul,
            'RemoteChargeActualFlag2' / Int32ul,
            'RemoteChargeActualRxTime' / Timestamp(Int32ul, 1., 1970),
            Padding(1),
            'RemoteDishargeActualCelcius' / Int8ul,
            'RemoteDischargeTargetVolt' / Int16ul,
            'RemoteDischargeTargetAmp' / Int16ul,
            'RemoteDischargeTargetVA' / Int16ul,
            'RemoteDischargeActualVolt' / Int16ul,
            'RemoteDischargeActualAmp' / Int16ul,
            'RemoteDischargeActualVA' / Int16ul,
            'RemoteDischargeActualFlag1' / Int32ul,
            'RemoteDischargeActualFlag2' / Int32ul,
            'RemoteDischargeActualRxTime' / Timestamp(Int32ul, 1., 1970),
        )

        data_parsed = parser.parse(data)
        ControlRemoteStatusPayload.clean_data(data_parsed)

        return data_parsed

    @staticmethod
    def clean_data(data: Dict) -> None:
        data['RemoteChargeActualCelcius'] = Payload.clean_temperature(data.get('RemoteChargeActualCelcius'))
        data['RemoteDishargeActualCelcius'] = Payload.clean_temperature(data.get('RemoteDishargeActualCelcius'))
