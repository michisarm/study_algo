import psutil
import os
import time


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # MB 단위로 변환


def measure_performance(func):
    """
    함수의 실행 시간과 메모리 사용량을 측정하는 데코레이터
    """

    def wrapper(*args, **kwargs):
        # 메모리 사용량 측정 시작
        start_mem = get_memory_usage()
        start_time = time.time()

        # 원본 함수 실행
        result = func(*args, **kwargs)

        # 메모리 사용량 측정 종료
        end_mem = get_memory_usage()
        end_time = time.time()

        # 성능 정보 출력
        print(f"\n{'='*50}")
        print(f"함수: {func.__name__}")
        print(f"메모리 사용량: {end_mem - start_mem:.6f} MB")
        print(f"실행 시간: {(end_time - start_time) * 1000:.6f} ms")
        print(f"{'='*50}\n")

        return result

    return wrapper
