import random

import pytest


@pytest.fixture
def random_seed():
    state = random.getstate()
    random.seed(1234)
    yield
    random.setstate(state)
