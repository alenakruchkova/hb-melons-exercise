"""This file should have our order classes in it."""

import random

class AbstractMelonOrder(object):
    """An abstract class for melon ordering."""

    def __init__(self, species, qty, country_code=None):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.passed_inspection = False

    def get_base_price(self):
        """Generates a random int between 5-9. And assigns the value to base_price"""

        self.price = random.randint(5,9)
        return self.price

    def get_total(self):
        """Calculate price."""

        if self.species == "Christmas melon":
            self.price = self.price * 1.5
        else:
            self.price = self.price
        total = (1 + self.tax) * self.qty * self.price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17   

    def get_total(self):
        """Calculate price."""
        if self.qty >= 10:
            return super(InternationalMelonOrder, self).get_total()
        else:
            total = super(InternationalMelonOrder, self).get_total() 
            return total + 3

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""

    order_type = "government"
    tax = 0.0

    def inspect_melons(self):
        """Set passed_inspection to true."""

        self.passed_inspection = True
        
