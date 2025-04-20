import random // 랜덤한 난수 생성을 위해 내장 객체 random 모듈 임포트 
import platform // 파이썬 버전, 윈도우 등의 버전 정보를 가져오기 위해 내장 객체 platform 모듈 임포트
import os
import json

class DummySensor:
    def __init__(self):
        self.env_values = {
        "mars_base_internal_temperature": 0,
        "mars_base_external_temperature": 0,
        "mars_base_internal_humidity": 0,
        "mars_base_external_illuminance": 0,
        "mars_base_internal_co2": 0,
        "mars_base_internal_oxygen": 0
        }

    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = random.uniform(18, 30)
        self.env_values["mars_base_external_temperature"] = random.uniform(0, 21)
        self.env_values["mars_base_internal_humidity"] = random.uniform(50, 60)
        self.env_values["mars_base_external_illuminance"] = random.uniform(500, 715)
        self.env_values["mars_base_internal_co2"] = random.uniform(0.02, 0.1)
        self.env_values["mars_base_internal_oxygen"] = random.uniform(4, 7)

    def get_env(self):
        return self.env_values

class MissionComputer:
    def get_mission_computer_info(self):
        try:
            info = {
            "Operating System": platform.system(),
            "OS Version": platform.version(),
            "CPU Type": platform.processor(),
            "CPU Cores": os.cpu_count(),
            "Memory Size": self._get_memory_size()
            }
            print(json.dumps(info, indent=4))
            return info
        except Exception as e:
            print(f"Error retrieving system info: {e}")
            return {}

    def get_mission_computer_load(self):
        try:
            load = {
            "CPU Load (1 min avg)": os.getLoadAvg()[0],
            "Memory Usage": self._get_memory_usage()
            }
            print(json.dumps(load, indent=4))
            return load
        except Exception as e:
            print(f"Error retrieving system load: {e}")
            return {}

    def _get_memory_size(self):
        try:
            with open('/proc/meminfo', 'r') as mem:
                for line in mem:
                    if 'MemTotal' in line:
                        return line.split(':')[1].strip()
        except:
            return "Unknown"

    def _get_memory_usage(self):
        try:
            with open('/proc/meminfo', 'r') as mem:
                meminfo = mem.readlines()
                mem_total = None
                mem_available = None
                for line in meminfo:
                    if 'MemTotal' in line:
                        mem_total = int(line.split()[1])
                    if 'MemAvailable' in line:
                        mem_available = int(line.split()[1])
                    if mem_total and mem_available:
                        used = mem_total - mem_available
                        return f"{used / mem_total * 100:.2f}%"
                    else:
                        return "Unknown"
        except:
            return "Unknown"

if __name__ == "__main__":
    ds = DummySensor()
    ds.set_env()
    print(ds.get_env())

    runComputer = MissionComputer()
    runComputer.get_mission_computer_info()
    runComputer.get_mission_computer_load()
