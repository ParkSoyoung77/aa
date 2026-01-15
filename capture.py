import socket

import struct

import time

import csv

​

def start_summary(interface="eth0", log_file="packets.csv"):

    # 소켓 설정

    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    s.bind((interface, 0))

​

    print(f"{'TIME':<10} | {'TYPE':<6} | {'SRC IP':<15} | {'DST IP':<15} | {'TTL':<4} | {'SIZE':<6}")

    print("-" * 75)

​

    # CSV 헤더 생성

    with open(log_file, 'w', newline='') as f:

        writer = csv.writer(f)

        writer.writerow(["time", "type", "src", "dst", "ttl", "size"])

​

    while True:

        raw_data, _ = s.recvfrom(65535)

        eth_proto = struct.unpack('!6s6sH', raw_data[:14])[2]

​

        if eth_proto == 0x0800: # IPv4

            ip_h = struct.unpack('!BBHHHBBH4s4s', raw_data[14:34])

            src = socket.inet_ntoa(ip_h[8])

            dst = socket.inet_ntoa(ip_h[9])

            ttl = ip_h[5]

            protocol_num = ip_h[6]

            p_size = len(raw_data)

​

            if protocol_num == 6: p_type = "TCP"

            elif protocol_num == 17: p_type = "UDP"

            elif protocol_num == 1: p_type = "ICMP"

            else: p_type = f"P-{protocol_num}"

​

            curr_time = time.strftime('%H:%M:%S')

            

            # 화면 출력

            print(f"{curr_time:<10} | {p_type:<6} | {src:<15} | {dst:<15} | {ttl:<4} | {p_size:<6}")

​

            # 분석용 파일 저장

            with open(log_file, 'a', newline='') as f:

                writer = csv.writer(f)

                writer.writerow([curr_time, p_type, src, dst, ttl, p_size])

        

        # CPU 점유율 방지를 위해 sleep 제거하거나 아주 짧게 설정

        # time.sleep(0.1) 

​

if __name__ == "__main__":

    # 인터페이스 이름을 본인 환경에 맞춰 수정 (예: eth0, enp0s3, wlan0)

    start_summary("eth0")
