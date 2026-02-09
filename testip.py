from scapy.all import ICMP, IP ,sr1
def ping_host(target_ip):
    packet =IP(dst=target_ip)/ICMP()
    reply = sr1(packet,timeout=2,verbose=0)
    if reply:
        print(f"{target_ip} is alive")
    else:
        print(f"{target_ip} is down or not responding")
ip=input("enter the ip:")
ping_host(ip)
