from abc import ABCMeta, abstractmethod


class RiskModel(object):
    """
    Abstract interface for an RiskModel callable.

    A derived-class instance of RiskModel takes in an Asset
    Universe and an optional DataHandler instance in order
    to modify weights on Assets generated by an AlphaModel.

    These adjusted weights are used within the PortfolioConstructionModel
    to generate new target weights for the portfolio.

    Implementing __call__ produces a dictionary keyed by
    Asset and with a scalar value as the signal.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def __call__(self, dt, weights):
        raise NotImplementedError(
            "Should implement __call__()"
        )
