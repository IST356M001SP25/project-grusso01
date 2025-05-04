import sys
import os
sys.path.append(os.path.abspath('code'))

from transform import compute_metrics
import pandas as pd
import time

print("🧪 test file is running", flush=True)

def test_compute_metrics():
    print("Running test_compute_metrics()", flush=True)

    data = {
        'BOROUGH': ['Manhattan'],
        'MONTH': ['2022 / 04'],
        'REFUSE_TONS_COLLECTED': [1200],
        'PAPER_TONS_COLLECTED': [250],
        'MGP_TONS_COLLECTED': [150]
    }

    df = pd.DataFrame(data)
    result = compute_metrics(df)

    expected_total = 1200 + 250 + 150
    expected_rate = (250 + 150) / expected_total
    actual_total = result.iloc[0]['TOTAL_WASTE_TONS']
    actual_rate = result.iloc[0]['CAPTURE_RATE']

    assert actual_total == expected_total
    assert abs(actual_rate - expected_rate) < 0.0001

    print("test_compute_metrics passed.", flush=True)
    time.sleep(1)

if __name__ == '__main__':
    test_compute_metrics()