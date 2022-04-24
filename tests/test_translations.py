import unittest

class TestTranslations(unittest.TestCase):

    def test_get_country_name_en_default(self):
        from i18n_iso_countries import get_country_name

        assert get_country_name(code='US', language='en') == "United States of America"
        assert get_country_name(code="is", language="en") == "Iceland"

    def test_get_country_name_en_alias(self):
        from i18n_iso_countries import get_country_name

        assert get_country_name(code='US', language='en', select="alias") == "USA"
        assert get_country_name(code="is", language="en") == "Iceland"

    def test_alpha3_to_alpha2(self):
        from i18n_iso_countries import alpha3_to_alpha2

        assert alpha3_to_alpha2('USA') == 'US'

    def test_numeric_to_alpha2(self):
        from i18n_iso_countries import numeric_to_alpha2

        assert numeric_to_alpha2('840') == 'US'

    def test_alpha2_to_alpha3(self):
        from i18n_iso_countries import alpha2_to_alpha3

        assert alpha2_to_alpha3('DE') == 'DEU'


    def test_numeric_to_alpha3(self):
        from i18n_iso_countries import numeric_to_alpha3

        assert numeric_to_alpha3('840') == 'USA'

    def test_alpha3_to_numeric(self):
        from i18n_iso_countries import alpha3_to_numeric

        assert alpha3_to_numeric('SWE') == '752'

    def test_alpha2_to_numeric(self):
        from i18n_iso_countries import alpha2_to_numeric

        assert alpha2_to_numeric('SE') == '752'

# print(get_country_name(code='US', language='en'))
# print(get_country_name(code="US", language='de'))
# print(get_country_name(code="USA", language='en'))
# print(get_country_name(code="840", language='en'))

# print(get_country_name(code="GB", language='en', select="official"))
# print(get_country_name(code="GB", language='en', select="alias"))
# print(get_country_name(code="GB", language='en', select="all"))


# print(get_country_name(code="LT", language='en', select="official"))
# print(get_country_name(code="LT", language='de', select="alias"))
# print(get_country_name(code="LT", language='en', select="all") )


# print(alpha3_to_alpha2('USA'))
# print(numeric_to_alpha2('840'))
# print(alpha2_to_alpha3('DE'))
# print(numeric_to_alpha3('840'))
# print(alpha3_to_numeric('SWE'))
# print(alpha2_to_numeric("SE") )
# print(get_alpha2_codes(self))
# print(get_alpha3_codes(self))
# print(get_numeric_codes(self))

# print(is_valid_country_code('US'))
# print(is_valid_country_code('US'))
# print(is_valid_country_code('XX'))
