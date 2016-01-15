"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """An abstract class for melon ordering."""

    def __init__(self, species, qty, country_code=None):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.passed_inspection = False


    def get_total(self ):
        """Calculate price."""

        if self.species == "Christmas melon":
            base_price = 5 * 1.5
        else:
            base_price = 5
        total = (1 + self.tax) * self.qty * base_price
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
        
