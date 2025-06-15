
# mars_mission_computer.py

import random


class DummySensor:
    """
    테스트용 더미 센서 클래스.
    화성 기지의 내부/외부 환경 데이터를 무작위로 생성한다.
    """

    def __init__(self):
        """
        DummySensor 클래스의 생성자.
        환경 데이터를 저장하는 사전 객체를 초기화한다.
        """
        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illuminance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None
        }

    def set_env(self):
        """
        센서 데이터를 무작위(random)로 설정한다.
        주어진 범위 내에서 환경 값을 생성하여 env_values에 저장한다.
        """
        self.env_values["mars_base_internal_temperature"] = round(random.uniform(18, 30), 2)
        self.env_values["mars_base_external_temperature"] = round(random.uniform(0, 21), 2)
        self.env_values["mars_base_internal_humidity"] = round(random.uniform(50, 60), 2)
        self.env_values["mars_base_external_illuminance"] = round(random.uniform(500, 715), 2)
        self.env_values["mars_base_internal_co2"] = round(random.uniform(0.02, 0.1), 4)
        self.env_values["mars_base_internal_oxygen"] = round(random.uniform(4, 7), 2)

    def get_env(self):
        """
        현재 설정된 환경 데이터를 반환한다.
        """
        return self.env_values
    


# DummySensor 클래스 인스턴스 생성
ds = DummySensor()

# 환경 설정 값 무작위로 생성
ds.set_env()

# 생성된 센서 값을 출력
env_data = ds.get_env()

if __name__ == "__main__":
    print("현재 센서 데이터:")
    for key, value in env_data.items():
        print(f"{key}: {value}")
>>>>>>> a029a8ba511f05667e290a601196bf2545d1a7fa
