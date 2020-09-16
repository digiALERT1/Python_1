import pytest


class BaseTriggerTest(object):
    @property
    def trigger_func(self):
        raise NotImplementedError(
            "This method should be implemented by each concrete subclass"
        )

    @property
    def good_input(self):
        raise NotImplementedError(
            "This method should be implemented by each concrete subclass"
        )

    @property
    def exception_input(self):
        raise NotImplementedError(
            "This method should be implemented by each concrete subclass"
        )

    @property
    def exception_raised(self):
        return TypeError

    def test_good_input(self):
        assert self.trigger_func(self.good_input[0]) == self.good_input[1]

    def test_exception(self):
        with pytest.raises(self.exception_raised):
            self.trigger_func(self.exception_input)
