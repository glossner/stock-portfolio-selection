"""
    Use this file for testing out different portfolio optimization strategies

    Note that some of the stocks do not have data for the beginning
    of the time period. For example, CFN (the 88th stock name)
    does not have any data until day 827.

"""

from ucrp import UniformConstantRebalancedPortfolio
from ubah import UniformBuyAndHoldPortfolio
from util import load_matlab_sp500_data
from expert_pool import ExpertPool
from olmar import OLMAR
from rmr import RMR


"""
*********************
        Main
*********************
"""
if __name__ == "__main__":

    # Load the training data from MATLAB file
    train_data = load_matlab_sp500_data('data/portfolio.mat')

    num_stocks = len(train_data.stock_names)  # Number of stocks in the dataset
    num_train_days = train_data.raw['vol'].shape[0]
    print 'Number of stocks in training set: ', num_stocks
    print 'Number of days in training set: ', num_train_days

    """
    olmar = OLMAR(market_data=train_data)
    olmar.run()

    ucrp = UniformConstantRebalancedPortfolio(market_data=train_data)
    ucrp.run()

    ubah = UniformBuyAndHoldPortfolio(market_data=train_data)
    ubah.run()
    """

    rmr = RMR(market_data=train_data)
    rmr.run()
    """
    # Expert Pooling
    ucrp2 = UniformConstantRebalancedPortfolio(market_data=train_data)
    ubah2 = UniformBuyAndHoldPortfolio(market_data=train_data)
    olmar2 = OLMAR(market_data=train_data)
    pool = ExpertPool(market_data=train_data, experts=[ucrp2, ubah2, olmar2])
    pool.run()
    """

    # TODO: cross-validation for hyperparameters (e.g. window size)

    # TODO: Robust Median Reversion (follow the loser method)
    # (Robust Median Reversion Strategy for On-Line Portfolio Selection, 2013)

    # TODO: follow the loser, but probably need to use some interval b/c you shouldn't
    # necessarily be fluctuating every day. Stock prices may continue on their trend
    # for several days before moving in the other direction
    # todo: maybe anticor

