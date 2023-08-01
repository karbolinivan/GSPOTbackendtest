from enum import Enum


BASE_URL = "https://payments.alpha.g-spot.website/api/v1/"


class External_Payments(str, Enum):
    ACCEPT_PAYMENT = f'{BASE_URL}external_payments/accept_payment/'
    COMISSIONS = f'{BASE_URL}external_payments/commissions/'
    SERVICES = f'{BASE_URL}external_payments/services/'

    def __str__(self) -> str:
        return self.value


class Item_Purchases(str, Enum):
    ITEM_PURCHASE_HISTORY = f'{BASE_URL}item_purchases/item-purchase-history/'
    PURCHASE = f'{BASE_URL}item_purchases/purchase/'
    REFUND = f'{BASE_URL}item_purchases/refund/'

    def __str__(self) -> str:
        return self.value


class Payment_Accounts(str, Enum):
    BALANCES = f'{BASE_URL}payment_accounts/balances/'
    CREATE_ACCOUNT = f'{BASE_URL}payment_accounts/create_account/'
    INCREASE_BALANCE = f'{BASE_URL}payment_accounts/increase_balance/'
    OWNER = f'{BASE_URL}payment_accounts/owner/'
    PAYMENT_COMMISSION = f'{BASE_URL}payment_accounts/payment_commission/'
    PAYOUT = f'{BASE_URL}payment_accounts/payout/'
    PAYOUT_DATA = f'{BASE_URL}payment_accounts/payout_data/'

    def __str__(self) -> str:
        return self.value