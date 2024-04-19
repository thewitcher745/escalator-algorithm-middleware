from django.db import models


# Create your models here.

class GeneralReport(models.Model):
    """
    Model that stores general report data from the backtest
    """
    strategy = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)
    timeframe = models.IntegerField(max_length=200)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    momentum_ratio = models.FloatField()
    atr_range = models.IntegerField()
    ma_range = models.IntegerField()
    validity_period = models.IntegerField()  # the period of time an order remains valid before entering a position,
    # in number of candles
    risk_reward = models.FloatField()
    order_deviation = models.FloatField()
    tp_deviation = models.FloatField()
    sl_deviation = models.FloatField()
    order_count = models.IntegerField()
    profit = models.FloatField()
    loss = models.FloatField()
    win_rate = models.FloatField()
    max_drawdown = models.FloatField()
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '_'.join([self.strategy, self.symbol, str(self.timeframe)])

    def calc_score(self):
        """
        Calculate the score of the general report
        :return:
        """
        pass

# class MonthlyReport(models.Model):
#     """
#     Model that stores monthly report data from the backtest
#     """
#     input = models.ForeignKey(GeneralReport, on_delete=models.CASCADE)
