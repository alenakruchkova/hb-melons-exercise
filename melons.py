"""This file should have our order classes in it."""

import random
from datetime import datetime

class AbstractMelonOrder(object):
    """An abstract class for melon ordering."""

    def __init__(self, species, qty, country_code=None, day_of_week, time):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.passed_inspection = False
        self.day_of_week = day_of_week
        self.time = time

    def get_base_price(self):
        """Generates a random int between 5-9. And assigns the value to price"""

        self.price = random.randint(5,9)
        
        if day_of_week.isoweekday is in range(1, 5):
            if time.daytime.hour is in range(8, 11):
                self.price = self.price + 4
                return self.price
        else:        
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

    def __init__(self):
        super(DomesticMelonOrder, self).__init__()
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self):
        super(InternationalMelonOrder, self).__init__()
        self.order_type = "international"
        self.tax = 0.17   

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
        
