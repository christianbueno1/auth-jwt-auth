from datetime import datetime
from pay.card import CreditCard

class PaymentProcessor:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def _check_api_key(self) -> bool:
        return self.api_key == "hello"
    
    def charge(self, card: CreditCard, amount: int) -> None:
        if not self.validate_card(card):
            raise ValueError("Invalid credit card.")
        if not self._check_api_key():
            raise ValueError(f"Invalid API key: {self.api_key}")
        print(f"Charging {amount} to card {card.number}")
        
    def validate_card(self, card: CreditCard) -> bool:
        return (
            luhn_checksum(card.number)
            and datetime(card.expiry_year, card.expiry_month, 1) > datetime.now()
        )
    
    def luhn_checksum(card_number: str) -> bool:
        def digits_of(card_nr: str) -> list[int]:
            return [int(d) for d in card_nr]
        
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]