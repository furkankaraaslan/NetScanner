import scapy.all as scapy
# from scapy.layers.l2 import ARP, Ether
import optparse


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-r", "--range", dest="packet_destination", help="Destination of ARP packet")
    (users_input, arguments) = parse_object.parse_args()

    if not users_input.packet_destination:
        print("Enter IP address")

    return users_input


# Create ARP packet
def create_arp_packet(arp_destination):
    arp_request_packet = scapy.ARP(pdst=arp_destination)
    return arp_request_packet


# Broadcast
def create_broadcast_packet():
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    return broadcast_packet


# Response
# Combine ARP and broadcast packet and send the combined packet
def get_response(arp_request_packet, broadcast_packet):

    combined_packet = broadcast_packet/arp_request_packet
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
    answered_list.summary()


user_input = get_user_input()
arp_packet = create_arp_packet(user_input.packet_destination)
broadcast = create_broadcast_packet()
get_response(arp_packet, broadcast)
