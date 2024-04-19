import csv
from backend_api.models import *

csv_path = r"C:\Users\Hamed\Documents\mt_strategy\data\results\backtest\backtest_results.csv"
with open(csv_path) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        _, created = GeneralReport.objects.get_or_create(
            strategy=row[14],
            symbol=row[1],
            timeframe=row[3],
            momentum_ratio=row[2],
            atr_range=row[4],
            ma_range=row[11],
            validity_period=row[5],
            risk_reward=row[9],
            order_deviation=row[8],
            tp_deviation=row[6],
            sl_deviation=row[7],
            order_count=row[12],
            profit=row[15],
            loss=row[16],
            win_rate=row[17],
            max_drawdown=row[18],
            score=row[19]
        )
        # creates a tuple of the new object or
        # current object and a boolean of if it was created
