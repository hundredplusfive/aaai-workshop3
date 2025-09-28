from .country_activities import country_activities
from .country_cost import country_cost
from .country_mthly_weather import country_mthly_weather


def test_print_all():
    print(country_activities())
    print("\n" + country_cost())
    print("\n" + country_mthly_weather())
