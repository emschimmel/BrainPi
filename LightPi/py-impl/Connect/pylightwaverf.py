import socket
import re
import sys
sys.path.append('../../')
import config

# werkend commando:
# echo -ne '100,!F*p' | nc -u 192.168.0.102 9760

class LightWaveRF:

    SOCKET_TIMEOUT = 2.0
    RX_PORT        = 9761
    TX_PORT        = 9760
    WTF            = '0,' # No clue why, with this added it worked...

    def __init__(self):

        # Set up transmission socket (allow broadcasting)
        tx_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        tx_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        tx_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tx_sock.settimeout(self.SOCKET_TIMEOUT)
        self.tx_sock = tx_sock

        # Set up receive socket
        rx_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        tx_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        rx_sock.settimeout(self.SOCKET_TIMEOUT)
        rx_sock.bind(('0.0.0.0', self.RX_PORT))
        self.rx_sock = rx_sock

        # Set the initial msg_id
        self.msg_id = 1

        # Find the WiFiLink
        try:
            self.wifilink_ip = config.lightwaveRfIp
        except:
            self.wifilink_ip = self.locate_wifilink()


    def locate_wifilink(self):
        msg_data = self.WTF+'@?v'
        try:
            data, ip = self.send(msg_data, broadcast=True)
        except socket.timeout:
            return None
        valid    = re.compile(r'^\d{1,3},\?V=(.*)\r\n$')
        match    = valid.match(data)
        if match:
            return ip
        return None

    def register_device(self):
        msg_data = self.WTF+'!F*p'
        data, ip = self.send(msg_data)
        print(data)
        print(ip)

    def get_power(self):
        msg_data = self.WTF+'@?W'
        data, ip = self.send(msg_data)
        valid    = re.compile(r'^\d{1,3},\?W=([0-9,]+)\r\n$')
        match    = valid.match(data)
        if match:
            power = match.group(1).split(',')
            return {
                'current':         power[0],
                'max_today':       power[1],
                'total_today':     power[2],
                'total_yesterday': power[3],
            }
        return None


    def control(self, room=None, device=None, state=None, msg1=None, msg2=None):
        room   = 'R%d' % room   if room   is not None else ''
        device = 'D%d' % device if device is not None else ''
        state  = 'F%s' % state  if state  is not None else ''
        command  =  ''.join([self.WTF, '!', room, device, state])
        msg_data = '|'.join(filter(None,[command, msg1, msg2]))
        self.send(msg_data)



    def send(self, msg_data, broadcast=False):
        data = self.get_next_msg_id() + msg_data
        if broadcast:
            ip = '255.255.255.255'
        else:
            ip = self.wifilink_ip
        self.tx_sock.sendto(data, (ip, self.TX_PORT))

        data, addr = self.rx_sock.recvfrom(1024)
        ip, port   = addr

        return (data, ip)


    def get_next_msg_id(self):
        # Ensure we always generate msg_ids from 001-999
        msg_id = self.msg_id + 1
        if msg_id % 1000 == 0:
            msg_id = 1
        self.msg_id = msg_id
        return '%03d' % msg_id


