#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mars_mission_computer.py

화성 기지 환경 정보를 주기적으로 센서로부터 읽어와 JSON 형태로 출력하는 미션 컴퓨터 코드.
"""

import time
import json
import random


class DummySensor:
    """
    DummySensor 클래스는 화성 기지의 환경 센서 데이터를 생성하기 위한 클래스
    각 센서에 대해 임의의 값을 리턴함
    """

    def get_value(self, sensor_name):
        try:
            if sensor_name == "mars_base_internal_temperature":
                # 화성 기지 내부 온도 (섭씨)
                return round(random.uniform(18, 25), 2)
            elif sensor_name == "mars_base_external_temperature":
                # 화성 기지 외부 온도 (섭씨) 
                return round(random.uniform(-80, 0), 2)
            elif sensor_name == "mars_base_internal_humidity":
                # 화성 기지 내부 습도 (%)
                return round(random.uniform(40, 60), 2)
            elif sensor_name == "mars_base_external_illuminance":
                # 화성 기지 외부 광량 (lux)
                return round(random.uniform(0, 10000), 2)
            elif sensor_name == "mars_base_internal_co2":
                # 화성 기지 내부 이산화탄소 농도 (ppm)
                return round(random.uniform(400, 800), 2)
            elif sensor_name == "mars_base_internal_oxygen":
                # 화성 기지 내부 산소 농도 (%)
                return round(random.uniform(20, 21), 2)
            else:
                return None
            
        except Exception as e:
            print(f"{sensor_name} 센서값을 가져오는 중 오류: {e}")

        return None


# 문제 3에서 제작한 DummySensor 클래스를 ds라는 이름으로 인스턴스화
ds = DummySensor()


class MissionComputer:
    def __init__(self):
        # 화성 기지 환경 정보를 저장할 사전
        self.env_values = {
        "mars_base_internal_temperature": None,
        "mars_base_external_temperature": None,
        "mars_base_internal_humidity": None,
        "mars_base_external_illuminance": None,
        "mars_base_internal_co2": None,
        "mars_base_internal_oxygen": None
        }

    def get_sensor_data(self):
        """
        5초 간격으로 센서 데이터를 읽어 env_values에 저장하고,
        JSON 포맷으로 출력하는 메소드.
        시스템 정보(여기서는 센서 데이터)를 가져오는 부분은 예외처리 
        """

        while True:
            try:
                self.env_values["mars_base_internal_temperature"] = ds.get_value("mars_base_internal_temperature")
                self.env_values["mars_base_external_temperature"] = ds.get_value("mars_base_external_temperature")
                self.env_values["mars_base_internal_humidity"] = ds.get_value("mars_base_internal_humidity")
                self.env_values["mars_base_external_illuminance"] = ds.get_value("mars_base_external_illuminance")
                self.env_values["mars_base_internal_co2"] = ds.get_value("mars_base_internal_co2")
                self.env_values["mars_base_internal_oxygen"] = ds.get_value("mars_base_internal_oxygen")

                # 환경 정보를 json 형태로 출력
                ##  한글 문자열이 아스키 형태의 문자열로 변경되는 것을 방지하는 방법으로 ensure_ascii=false 사용
                print(json.dumps(self.env_values, ensure_ascii=False))

            except Exception as e:
                # 센서 데이터를 가져올 때 발생 가능한 모든 예외 처리
                print("센서 데이터를 가져오는 중 오류 발생:", e)
            
            # 5초마다 반복
            time.sleep(5)


if __name__ == "__main__":
    # MissionComputer 클래스를 RunComputer 라는 이름으로 인스턴스화
    RunComputer = MissionComputer()
    # RunComputer 인스턴스의 get_sensor_data() 메소드를 호출하여 지속적으로 데이터를 출력
    RunComputer.get_sensor_data()