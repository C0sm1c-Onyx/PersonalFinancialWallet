import pytest
from datetime import datetime as dt
from PersonalFinancialWallet import PersonalWallet


@pytest.fixture
def wallet():
    return PersonalWallet()


def test_insert(wallet):
    before_balance = wallet.balance
    before_trackings_count = len(wallet.trackings)
    wallet.insert('Доход', 100, '****')
    assert wallet.balance == before_balance + 100
    assert len(wallet.trackings) == before_trackings_count + 1


def test_update(wallet):
    wallet.insert('Расход', 100, 'Description')
    before_balance = wallet.balance
    wallet.update(1, 'Доход', 200, 'New Description')
    assert wallet.balance == before_balance + 200


def test_search(wallet):
    wallet.insert('Доход', 500, '****')
    results = wallet.search('500')
    assert len(list(results)) == 1


if __name__ == "__main__":
    pytest.main()
