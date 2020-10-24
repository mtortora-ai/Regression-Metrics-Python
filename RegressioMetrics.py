import numpy as np


class RegressionMetrics:
    @staticmethod
    def metric_rss(observed, estimated):
        # Residual Sum of Squares
        rss = np.sum(np.square(observed - estimated))
        return rss

    @staticmethod
    def metric_mse(observed, estimated):
        # Mean Squared Error
        mse = np.mean((np.square(observed - estimated)))
        return mse

    @staticmethod
    def metric_mspe(observed, estimated):
        # Mean Squared Percentage Error
        mspe = np.mean(
            np.divide(np.square(observed - estimated), np.square(observed)))
        return mspe

    @classmethod
    def metric_rmse(cls, observed, estimated):
        # Root Mean Square Error
        rmse = np.square(cls.metric_mse(observed, estimated))
        return rmse

    @classmethod
    def metric_rmspe(cls, observed, estimated):
        # Root Mean Square Percentage Error
        rmspe = np.square(cls.metric_mspe(observed, estimated))
        return rmspe

    @staticmethod
    def metric_mae(observed, estimated):
        # Mean Absolute Error
        mae = np.mean(np.abs(observed - estimated))
        return mae

    @staticmethod
    def metric_mape(observed, estimated):
        # Mean Absolute Percentage Error
        mape = np.mean(np.abs(np.divide((observed - estimated), observed)))
        return mape

    @staticmethod
    def metric_rse(observed, estimated):
        # Relative Squared Error
        rse = np.divide(np.sum(np.square(observed - estimated)),
                        np.sum(np.square(observed - np.mean(observed))))
        return rse

    @staticmethod
    def metric_rae(observed, estimated):
        # Relative Absolute Error
        rae = np.divide(np.sum(np.abs(observed - estimated)),
                        np.sum(np.abs(observed - np.mean(observed))))
        return rae

    @classmethod
    def metric_r2(cls, observed, estimated):
        r2 = 1 - cls.metric_rse(observed, estimated)
        return r2
