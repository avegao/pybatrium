import logging
import socket
import sys

from construct import Struct, Int16ul, PaddedString

from payload import PayloadEnum, Message

UDP_IP = '0.0.0.0'
UDP_PORT = 18542
BUFFER_SIZE = 1024


def start_server() -> socket:
    logging.debug('creating UDP server...')

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((UDP_IP, UDP_PORT))

    logging.debug(f'server listening at port {UDP_PORT}...')

    return server


def parse_data(data: bytes) -> Message:
    parser = Struct(
        "first" / PaddedString(1, "utf8"),
        'MessageId' / Int16ul,
        "nd" / PaddedString(1, "utf8"),
        'SystemId' / Int16ul,
        'hubId' / Int16ul,
    )
    data_parsed = parser.parse(data)

    logging.debug('message header', data_parsed)

    message = Message()
    message.system_id = data_parsed.get('SystemId')
    message.message_id = hex(data_parsed.get('MessageId'))[2:]

    try:
        payload_enum = PayloadEnum(message.message_id)
    except ValueError:
        logging.warning(f'message with id {message.message_id} not supported data: {data}')

        return message

    logging.debug(f'payload received: {payload_enum.value} {payload_enum.name}')

    if message.message_id == PayloadEnum.STATUS_SHUNT.value:
        payload = PayloadEnum.parse(payload_enum, data)

        logging.debug(payload)

        sys.exit(0)

    return message


def receive_message(server: socket) -> None:
    while True:
        data, addr = server.recvfrom(BUFFER_SIZE)

        logging.debug(f"received {len(data)} bytes from {addr}")

        parse_data(data)


def main():
    logging.basicConfig(level=logging.DEBUG)

    server = start_server()
    receive_message(server)

    # data = b':2B,L\t\x90\x88\x0b4L\x0eL\x0eDD\x00\x00\xe8\x0c\x03\x00T\x0bh\x10\x04\x10\xa8\x06s_\x00\x02\x02\x06\x02\x02\x003\x01\x8c\x13\x00\x00\x00\x00\x00\x00\x00\x00\xfa'
    #
    # parse_data(data)


if __name__ == '__main__':
    main()
