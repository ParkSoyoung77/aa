import pandas as pd

import time

import os

​

def analyze_packets(log_file="packets.csv"):

    print("실시간 패킷 분석 중...")

    

    while True:

        if os.path.exists(log_file):

            try:

                df = pd.read_csv(log_file)

                if not df.empty:

                    os.system('clear')

                    print("=== 실시간 트래픽 분석 통계 ===")

                    print(f"총 패킷 수: {len(df)}")

                    

                    print("\n[프로토콜별 비율]")

                    print(df['type'].value_counts(normalize=True) * 100)

                    

                    print("\n[상위 발신지 IP Top 5]")

                    print(df['src'].value_counts().head(5))

                    

                    print("\n[평균 패킷 크기]")

                    print(f"{df['size'].mean():.2f} bytes")

            except Exception as e:

                pass # 파일 쓰기 중 충돌 방지

        

        time.sleep(2) # 2초마다 갱신

​

if __name__ == "__main__":

    analyze_packets()
