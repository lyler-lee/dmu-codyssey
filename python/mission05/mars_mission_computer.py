import random   # 랜덤한 난수 생성을 위해 내장 객체 random 모듈 임포트 
import platform # 파이썬 버전, 윈도우 등의 버전 정보를 가져오기 위해 내장 객체 platform 모듈 임포트
import os       # 운영체제를 활용하기 위해 내장 객체인 os 모듈 임포트
import json     # json 형태의 데이터를 처리하기 위해 내장 객체 json 모듈 임포트
import ctypes   # python에서 c의 기능를 사용하기 위해 내장 라이브러리 ctypes 사용
import sys      # 


# 더미 센서 클래스 정의
class DummySensor:
    def __init__(self):
        # 센서 값들을 저장할 딕셔너리 초기화
        self.env_values = {
            "mars_base_internal_temperature": 0,
            "mars_base_external_temperature": 0,
            "mars_base_internal_humidity": 0,
            "mars_base_external_illuminance": 0,
            "mars_base_internal_co2": 0,
            "mars_base_internal_oxygen": 0
        }

    # 랜덤한 환경 값을 설정하는 메서드
    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = random.uniform(18, 30)
        self.env_values["mars_base_external_temperature"] = random.uniform(0, 21)
        self.env_values["mars_base_internal_humidity"] = random.uniform(50, 60)
        self.env_values["mars_base_external_illuminance"] = random.uniform(500, 715)
        self.env_values["mars_base_internal_co2"] = random.uniform(0.02, 0.1)
        self.env_values["mars_base_internal_oxygen"] = random.uniform(4, 7)

    # 환경 값을 반환하는 메서드
    def get_env(self):
        return self.env_values

# 미션 컴퓨터 정보와 부하를 확인하는 클래스 정의
class MissionComputer:
    # 시스템 정보를 가져오는 메서드
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

    # 시스템 부하 정보를 가져오는 메서드
    def get_mission_computer_load(self):
        try:
            cpu_load = self._get_cpu_load()
            mem_usage = self._get_memory_usage()
            load = {
                "CPU Load": cpu_load,
                "Memory Usage": mem_usage
            }
            print(json.dumps(load, indent=4))
            return load
        except Exception as e:
            print(f"Error retrieving system load: {e}")
            return {}

    # 플랫폼에 따라 CPU 부하를 가져오는 보조 메서드
    def _get_cpu_load(self):
        if platform.system() == "Windows":
            try:
                return f"{os.getloadavg()} (Not supported on Windows, showing dummy value)"
            except:
                return "Unavailable on Windows"
        else:
            return os.getloadavg()[0]

    # 플랫폼에 따라 메모리 총량을 가져오는 보조 메서드
    def _get_memory_size(self):
        if platform.system() == "Windows":
            try:
                kernel32 = ctypes.windll.kernel32
                c_ulonglong = ctypes.c_ulonglong
                class MEMORYSTATUSEX(ctypes.Structure):
                    _fields_ = [
                        ('dwLength', ctypes.c_ulong),
                        ('dwMemoryLoad', ctypes.c_ulong),
                        ('ullTotalPhys', c_ulonglong),
                        ('ullAvailPhys', c_ulonglong),
                        ('ullTotalPageFile', c_ulonglong),
                        ('ullAvailPageFile', c_ulonglong),
                        ('ullTotalVirtual', c_ulonglong),
                        ('ullAvailVirtual', c_ulonglong),
                        ('sullAvailExtendedVirtual', c_ulonglong),
                    ]
                stat = MEMORYSTATUSEX()
                stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
                kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))
                return f"{stat.ullTotalPhys // (1024 * 1024)} MB"
            except:
                return "Unknown"
        else:
            try:
                with open('/proc/meminfo', 'r') as mem:
                    for line in mem:
                        if 'MemTotal' in line:
                            return line.split(':')[1].strip()
            except:
                return "Unknown"

    # 플랫폼에 따라 메모리 사용량을 가져오는 보조 메서드
    def _get_memory_usage(self):
        if platform.system() == "Windows":
            try:
                kernel32 = ctypes.windll.kernel32
                c_ulonglong = ctypes.c_ulonglong
                class MEMORYSTATUSEX(ctypes.Structure):
                    _fields_ = [
                        ('dwLength', ctypes.c_ulong),
                        ('dwMemoryLoad', ctypes.c_ulong),
                        ('ullTotalPhys', c_ulonglong),
                        ('ullAvailPhys', c_ulonglong),
                        ('ullTotalPageFile', c_ulonglong),
                        ('ullAvailPageFile', c_ulonglong),
                        ('ullTotalVirtual', c_ulonglong),
                        ('ullAvailVirtual', c_ulonglong),
                        ('sullAvailExtendedVirtual', c_ulonglong),
                    ]
                stat = MEMORYSTATUSEX()
                stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
                kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))
                used = stat.ullTotalPhys - stat.ullAvailPhys
                return f"{used / stat.ullTotalPhys * 100:.2f}%"
            except:
                return "Unknown"
        else:
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

# 실행 시 테스트 코드
if __name__ == "__main__":
    # 더미 센서 인스턴스 생성 및 사용
    ds = DummySensor()
    ds.set_env()
    print(ds.get_env())

    # 미션 컴퓨터 인스턴스 생성 및 시스템 정보/부하 출력
    runComputer = MissionComputer()
    runComputer.get_mission_computer_info()
    runComputer.get_mission_computer_load()
