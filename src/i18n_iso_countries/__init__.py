import json
import os

codes = [
    ["AF", "AFG", "004", "ISO 3166-2:AF"],
    ["AL", "ALB", "008", "ISO 3166-2:AL"],
    ["DZ", "DZA", "012", "ISO 3166-2:DZ"],
    ["AS", "ASM", "016", "ISO 3166-2:AS"],
    ["AD", "AND", "020", "ISO 3166-2:AD"],
    ["AO", "AGO", "024", "ISO 3166-2:AO"],
    ["AI", "AIA", "660", "ISO 3166-2:AI"],
    ["AQ", "ATA", "010", "ISO 3166-2:AQ"],
    ["AG", "ATG", "028", "ISO 3166-2:AG"],
    ["AR", "ARG", "032", "ISO 3166-2:AR"],
    ["AM", "ARM", "051", "ISO 3166-2:AM"],
    ["AW", "ABW", "533", "ISO 3166-2:AW"],
    ["AU", "AUS", "036", "ISO 3166-2:AU"],
    ["AT", "AUT", "040", "ISO 3166-2:AT"],
    ["AZ", "AZE", "031", "ISO 3166-2:AZ"],
    ["BS", "BHS", "044", "ISO 3166-2:BS"],
    ["BH", "BHR", "048", "ISO 3166-2:BH"],
    ["BD", "BGD", "050", "ISO 3166-2:BD"],
    ["BB", "BRB", "052", "ISO 3166-2:BB"],
    ["BY", "BLR", "112", "ISO 3166-2:BY"],
    ["BE", "BEL", "056", "ISO 3166-2:BE"],
    ["BZ", "BLZ", "084", "ISO 3166-2:BZ"],
    ["BJ", "BEN", "204", "ISO 3166-2:BJ"],
    ["BM", "BMU", "060", "ISO 3166-2:BM"],
    ["BT", "BTN", "064", "ISO 3166-2:BT"],
    ["BO", "BOL", "068", "ISO 3166-2:BO"],
    ["BA", "BIH", "070", "ISO 3166-2:BA"],
    ["BW", "BWA", "072", "ISO 3166-2:BW"],
    ["BV", "BVT", "074", "ISO 3166-2:BV"],
    ["BR", "BRA", "076", "ISO 3166-2:BR"],
    ["IO", "IOT", "086", "ISO 3166-2:IO"],
    ["BN", "BRN", "096", "ISO 3166-2:BN"],
    ["BG", "BGR", "100", "ISO 3166-2:BG"],
    ["BF", "BFA", "854", "ISO 3166-2:BF"],
    ["BI", "BDI", "108", "ISO 3166-2:BI"],
    ["KH", "KHM", "116", "ISO 3166-2:KH"],
    ["CM", "CMR", "120", "ISO 3166-2:CM"],
    ["CA", "CAN", "124", "ISO 3166-2:CA"],
    ["CV", "CPV", "132", "ISO 3166-2:CV"],
    ["KY", "CYM", "136", "ISO 3166-2:KY"],
    ["CF", "CAF", "140", "ISO 3166-2:CF"],
    ["TD", "TCD", "148", "ISO 3166-2:TD"],
    ["CL", "CHL", "152", "ISO 3166-2:CL"],
    ["CN", "CHN", "156", "ISO 3166-2:CN"],
    ["CX", "CXR", "162", "ISO 3166-2:CX"],
    ["CC", "CCK", "166", "ISO 3166-2:CC"],
    ["CO", "COL", "170", "ISO 3166-2:CO"],
    ["KM", "COM", "174", "ISO 3166-2:KM"],
    ["CG", "COG", "178", "ISO 3166-2:CG"],
    ["CD", "COD", "180", "ISO 3166-2:CD"],
    ["CK", "COK", "184", "ISO 3166-2:CK"],
    ["CR", "CRI", "188", "ISO 3166-2:CR"],
    ["CI", "CIV", "384", "ISO 3166-2:CI"],
    ["HR", "HRV", "191", "ISO 3166-2:HR"],
    ["CU", "CUB", "192", "ISO 3166-2:CU"],
    ["CY", "CYP", "196", "ISO 3166-2:CY"],
    ["CZ", "CZE", "203", "ISO 3166-2:CZ"],
    ["DK", "DNK", "208", "ISO 3166-2:DK"],
    ["DJ", "DJI", "262", "ISO 3166-2:DJ"],
    ["DM", "DMA", "212", "ISO 3166-2:DM"],
    ["DO", "DOM", "214", "ISO 3166-2:DO"],
    ["EC", "ECU", "218", "ISO 3166-2:EC"],
    ["EG", "EGY", "818", "ISO 3166-2:EG"],
    ["SV", "SLV", "222", "ISO 3166-2:SV"],
    ["GQ", "GNQ", "226", "ISO 3166-2:GQ"],
    ["ER", "ERI", "232", "ISO 3166-2:ER"],
    ["EE", "EST", "233", "ISO 3166-2:EE"],
    ["ET", "ETH", "231", "ISO 3166-2:ET"],
    ["FK", "FLK", "238", "ISO 3166-2:FK"],
    ["FO", "FRO", "234", "ISO 3166-2:FO"],
    ["FJ", "FJI", "242", "ISO 3166-2:FJ"],
    ["FI", "FIN", "246", "ISO 3166-2:FI"],
    ["FR", "FRA", "250", "ISO 3166-2:FR"],
    ["GF", "GUF", "254", "ISO 3166-2:GF"],
    ["PF", "PYF", "258", "ISO 3166-2:PF"],
    ["TF", "ATF", "260", "ISO 3166-2:TF"],
    ["GA", "GAB", "266", "ISO 3166-2:GA"],
    ["GM", "GMB", "270", "ISO 3166-2:GM"],
    ["GE", "GEO", "268", "ISO 3166-2:GE"],
    ["DE", "DEU", "276", "ISO 3166-2:DE"],
    ["GH", "GHA", "288", "ISO 3166-2:GH"],
    ["GI", "GIB", "292", "ISO 3166-2:GI"],
    ["GR", "GRC", "300", "ISO 3166-2:GR"],
    ["GL", "GRL", "304", "ISO 3166-2:GL"],
    ["GD", "GRD", "308", "ISO 3166-2:GD"],
    ["GP", "GLP", "312", "ISO 3166-2:GP"],
    ["GU", "GUM", "316", "ISO 3166-2:GU"],
    ["GT", "GTM", "320", "ISO 3166-2:GT"],
    ["GN", "GIN", "324", "ISO 3166-2:GN"],
    ["GW", "GNB", "624", "ISO 3166-2:GW"],
    ["GY", "GUY", "328", "ISO 3166-2:GY"],
    ["HT", "HTI", "332", "ISO 3166-2:HT"],
    ["HM", "HMD", "334", "ISO 3166-2:HM"],
    ["VA", "VAT", "336", "ISO 3166-2:VA"],
    ["HN", "HND", "340", "ISO 3166-2:HN"],
    ["HK", "HKG", "344", "ISO 3166-2:HK"],
    ["HU", "HUN", "348", "ISO 3166-2:HU"],
    ["IS", "ISL", "352", "ISO 3166-2:IS"],
    ["IN", "IND", "356", "ISO 3166-2:IN"],
    ["ID", "IDN", "360", "ISO 3166-2:ID"],
    ["IR", "IRN", "364", "ISO 3166-2:IR"],
    ["IQ", "IRQ", "368", "ISO 3166-2:IQ"],
    ["IE", "IRL", "372", "ISO 3166-2:IE"],
    ["IL", "ISR", "376", "ISO 3166-2:IL"],
    ["IT", "ITA", "380", "ISO 3166-2:IT"],
    ["JM", "JAM", "388", "ISO 3166-2:JM"],
    ["JP", "JPN", "392", "ISO 3166-2:JP"],
    ["JO", "JOR", "400", "ISO 3166-2:JO"],
    ["KZ", "KAZ", "398", "ISO 3166-2:KZ"],
    ["KE", "KEN", "404", "ISO 3166-2:KE"],
    ["KI", "KIR", "296", "ISO 3166-2:KI"],
    ["KP", "PRK", "408", "ISO 3166-2:KP"],
    ["KR", "KOR", "410", "ISO 3166-2:KR"],
    ["KW", "KWT", "414", "ISO 3166-2:KW"],
    ["KG", "KGZ", "417", "ISO 3166-2:KG"],
    ["LA", "LAO", "418", "ISO 3166-2:LA"],
    ["LV", "LVA", "428", "ISO 3166-2:LV"],
    ["LB", "LBN", "422", "ISO 3166-2:LB"],
    ["LS", "LSO", "426", "ISO 3166-2:LS"],
    ["LR", "LBR", "430", "ISO 3166-2:LR"],
    ["LY", "LBY", "434", "ISO 3166-2:LY"],
    ["LI", "LIE", "438", "ISO 3166-2:LI"],
    ["LT", "LTU", "440", "ISO 3166-2:LT"],
    ["LU", "LUX", "442", "ISO 3166-2:LU"],
    ["MO", "MAC", "446", "ISO 3166-2:MO"],
    ["MG", "MDG", "450", "ISO 3166-2:MG"],
    ["MW", "MWI", "454", "ISO 3166-2:MW"],
    ["MY", "MYS", "458", "ISO 3166-2:MY"],
    ["MV", "MDV", "462", "ISO 3166-2:MV"],
    ["ML", "MLI", "466", "ISO 3166-2:ML"],
    ["MT", "MLT", "470", "ISO 3166-2:MT"],
    ["MH", "MHL", "584", "ISO 3166-2:MH"],
    ["MQ", "MTQ", "474", "ISO 3166-2:MQ"],
    ["MR", "MRT", "478", "ISO 3166-2:MR"],
    ["MU", "MUS", "480", "ISO 3166-2:MU"],
    ["YT", "MYT", "175", "ISO 3166-2:YT"],
    ["MX", "MEX", "484", "ISO 3166-2:MX"],
    ["FM", "FSM", "583", "ISO 3166-2:FM"],
    ["MD", "MDA", "498", "ISO 3166-2:MD"],
    ["MC", "MCO", "492", "ISO 3166-2:MC"],
    ["MN", "MNG", "496", "ISO 3166-2:MN"],
    ["MS", "MSR", "500", "ISO 3166-2:MS"],
    ["MA", "MAR", "504", "ISO 3166-2:MA"],
    ["MZ", "MOZ", "508", "ISO 3166-2:MZ"],
    ["MM", "MMR", "104", "ISO 3166-2:MM"],
    ["NA", "NAM", "516", "ISO 3166-2:NA"],
    ["NR", "NRU", "520", "ISO 3166-2:NR"],
    ["NP", "NPL", "524", "ISO 3166-2:NP"],
    ["NL", "NLD", "528", "ISO 3166-2:NL"],
    ["NC", "NCL", "540", "ISO 3166-2:NC"],
    ["NZ", "NZL", "554", "ISO 3166-2:NZ"],
    ["NI", "NIC", "558", "ISO 3166-2:NI"],
    ["NE", "NER", "562", "ISO 3166-2:NE"],
    ["NG", "NGA", "566", "ISO 3166-2:NG"],
    ["NU", "NIU", "570", "ISO 3166-2:NU"],
    ["NF", "NFK", "574", "ISO 3166-2:NF"],
    ["MP", "MNP", "580", "ISO 3166-2:MP"],
    ["MK", "MKD", "807", "ISO 3166-2:MK"],
    ["NO", "NOR", "578", "ISO 3166-2:NO"],
    ["OM", "OMN", "512", "ISO 3166-2:OM"],
    ["PK", "PAK", "586", "ISO 3166-2:PK"],
    ["PW", "PLW", "585", "ISO 3166-2:PW"],
    ["PS", "PSE", "275", "ISO 3166-2:PS"],
    ["PA", "PAN", "591", "ISO 3166-2:PA"],
    ["PG", "PNG", "598", "ISO 3166-2:PG"],
    ["PY", "PRY", "600", "ISO 3166-2:PY"],
    ["PE", "PER", "604", "ISO 3166-2:PE"],
    ["PH", "PHL", "608", "ISO 3166-2:PH"],
    ["PN", "PCN", "612", "ISO 3166-2:PN"],
    ["PL", "POL", "616", "ISO 3166-2:PL"],
    ["PT", "PRT", "620", "ISO 3166-2:PT"],
    ["PR", "PRI", "630", "ISO 3166-2:PR"],
    ["QA", "QAT", "634", "ISO 3166-2:QA"],
    ["RE", "REU", "638", "ISO 3166-2:RE"],
    ["RO", "ROU", "642", "ISO 3166-2:RO"],
    ["RU", "RUS", "643", "ISO 3166-2:RU"],
    ["RW", "RWA", "646", "ISO 3166-2:RW"],
    ["SH", "SHN", "654", "ISO 3166-2:SH"],
    ["KN", "KNA", "659", "ISO 3166-2:KN"],
    ["LC", "LCA", "662", "ISO 3166-2:LC"],
    ["PM", "SPM", "666", "ISO 3166-2:PM"],
    ["VC", "VCT", "670", "ISO 3166-2:VC"],
    ["WS", "WSM", "882", "ISO 3166-2:WS"],
    ["SM", "SMR", "674", "ISO 3166-2:SM"],
    ["ST", "STP", "678", "ISO 3166-2:ST"],
    ["SA", "SAU", "682", "ISO 3166-2:SA"],
    ["SN", "SEN", "686", "ISO 3166-2:SN"],
    ["SC", "SYC", "690", "ISO 3166-2:SC"],
    ["SL", "SLE", "694", "ISO 3166-2:SL"],
    ["SG", "SGP", "702", "ISO 3166-2:SG"],
    ["SK", "SVK", "703", "ISO 3166-2:SK"],
    ["SI", "SVN", "705", "ISO 3166-2:SI"],
    ["SB", "SLB", "090", "ISO 3166-2:SB"],
    ["SO", "SOM", "706", "ISO 3166-2:SO"],
    ["ZA", "ZAF", "710", "ISO 3166-2:ZA"],
    ["GS", "SGS", "239", "ISO 3166-2:GS"],
    ["ES", "ESP", "724", "ISO 3166-2:ES"],
    ["LK", "LKA", "144", "ISO 3166-2:LK"],
    ["SD", "SDN", "729", "ISO 3166-2:SD"],
    ["SR", "SUR", "740", "ISO 3166-2:SR"],
    ["SJ", "SJM", "744", "ISO 3166-2:SJ"],
    ["SZ", "SWZ", "748", "ISO 3166-2:SZ"],
    ["SE", "SWE", "752", "ISO 3166-2:SE"],
    ["CH", "CHE", "756", "ISO 3166-2:CH"],
    ["SY", "SYR", "760", "ISO 3166-2:SY"],
    ["TW", "TWN", "158", "ISO 3166-2:TW"],
    ["TJ", "TJK", "762", "ISO 3166-2:TJ"],
    ["TZ", "TZA", "834", "ISO 3166-2:TZ"],
    ["TH", "THA", "764", "ISO 3166-2:TH"],
    ["TL", "TLS", "626", "ISO 3166-2:TL"],
    ["TG", "TGO", "768", "ISO 3166-2:TG"],
    ["TK", "TKL", "772", "ISO 3166-2:TK"],
    ["TO", "TON", "776", "ISO 3166-2:TO"],
    ["TT", "TTO", "780", "ISO 3166-2:TT"],
    ["TN", "TUN", "788", "ISO 3166-2:TN"],
    ["TR", "TUR", "792", "ISO 3166-2:TR"],
    ["TM", "TKM", "795", "ISO 3166-2:TM"],
    ["TC", "TCA", "796", "ISO 3166-2:TC"],
    ["TV", "TUV", "798", "ISO 3166-2:TV"],
    ["UG", "UGA", "800", "ISO 3166-2:UG"],
    ["UA", "UKR", "804", "ISO 3166-2:UA"],
    ["AE", "ARE", "784", "ISO 3166-2:AE"],
    ["GB", "GBR", "826", "ISO 3166-2:GB"],
    ["US", "USA", "840", "ISO 3166-2:US"],
    ["UM", "UMI", "581", "ISO 3166-2:UM"],
    ["UY", "URY", "858", "ISO 3166-2:UY"],
    ["UZ", "UZB", "860", "ISO 3166-2:UZ"],
    ["VU", "VUT", "548", "ISO 3166-2:VU"],
    ["VE", "VEN", "862", "ISO 3166-2:VE"],
    ["VN", "VNM", "704", "ISO 3166-2:VN"],
    ["VG", "VGB", "092", "ISO 3166-2:VG"],
    ["VI", "VIR", "850", "ISO 3166-2:VI"],
    ["WF", "WLF", "876", "ISO 3166-2:WF"],
    ["EH", "ESH", "732", "ISO 3166-2:EH"],
    ["YE", "YEM", "887", "ISO 3166-2:YE"],
    ["ZM", "ZMB", "894", "ISO 3166-2:ZM"],
    ["ZW", "ZWE", "716", "ISO 3166-2:ZW"],
    ["AX", "ALA", "248", "ISO 3166-2:AX"],
    ["BQ", "BES", "535", "ISO 3166-2:BQ"],
    ["CW", "CUW", "531", "ISO 3166-2:CW"],
    ["GG", "GGY", "831", "ISO 3166-2:GG"],
    ["IM", "IMN", "833", "ISO 3166-2:IM"],
    ["JE", "JEY", "832", "ISO 3166-2:JE"],
    ["ME", "MNE", "499", "ISO 3166-2:ME"],
    ["BL", "BLM", "652", "ISO 3166-2:BL"],
    ["MF", "MAF", "663", "ISO 3166-2:MF"],
    ["RS", "SRB", "688", "ISO 3166-2:RS"],
    ["SX", "SXM", "534", "ISO 3166-2:SX"],
    ["SS", "SSD", "728", "ISO 3166-2:SS"],
    ["XK", "XKX", "983", "ISO 3166-2:XK"]
  ]

__lang_data_path = os.path.dirname(os.path.realpath(__file__))

def get_country_name(code=None, language='en', select='official'):
    """
    Get the country for `code`

    Parameters:
    - code (str): 2 letter iso-3166-1 country code
    - language (str): 2 letter language code. (only availtable option is "en" which is also the default)
    - select (str): official/alias/all

    Returns:
    - str/dict/list: The country name data
    """
    if select not in ('official', 'alias', 'all'):
         raise ValueError("""select must be one of the avalable options: official/alias/all""")

    data = {}
    
    available_locales = get_supported_languages()
    if language not in available_locales:
        raise ValueError(
            f"""language must be one of the avalable options: {", ".join(available_locales)}"""
        )

    with open(os.path.join(__lang_data_path, f"langs/{language}.json")) as json_file:
        data[language] = json.load(json_file)

    if code is None and select ==  'official':
        official_codes = {}
        for key, value in data[language]["countries"].items():
            if isinstance(value, list):
                official_codes[key] = value[0]
            else:
                official_codes[key] = value
        
        return official_codes
    
    if code is None and select ==  'alias':
        official_codes = {}
        for key, value in data[language]["countries"].items():
            if isinstance(value, list) and len(value) >=2:
                official_codes[key] = value[1]
            else:
                official_codes[key] = value
        
        return official_codes

    if code is None and select ==  'all':
        official_codes = {}
        for key, value in data[language]["countries"].items():
            if isinstance(value, list):
                official_codes[key] = value
            else:
                official_codes[key] = [value,]
        
        return official_codes  

    code = code.upper()
    # 2 letter code to name
    if code and len(code) == 2 and select == 'official':
        name = data[language]["countries"][code]
        if isinstance(name, list):
            return name[0]
        return name
    
    if code and len(code) == 2 and select == 'alias':
        name = data[language]["countries"][code]
        if isinstance(name, list) and len(name) >=2:
            return name[1]
        return name

    if code and len(code) == 2 and select == 'all':
        name = data[language]["countries"][code]
        if isinstance(name, list):
            return name
        return [name,]
    
    # 3 letter code to name
    if code and len(code) == 3 and not code.isdigit():
        
        for code2, code3, _, _ in codes:
            if code == code3:
                code = code2
        if len(code) == 3:
            raise ValueError("""country 3 letter code parameters error""")
        if select == 'official':
            name = data[language]["countries"][code]

            if isinstance(name, list):
                return name[0]
            return name
    
        if select == 'alias':
            name = data[language]["countries"][code]
            if isinstance(name, list) and len(name) >=2:
                return name[1]
            return name

        if select == 'all':
            name = data[language]["countries"][code]
            if isinstance(name, list):
                return name
            return [name,]

    # numeric code to name
    if code and len(code) == 3 and code.isdigit():
        for code2, _, num, _ in codes:
            if code == num:
                code = code2
        if len(code) == 3:
            raise ValueError("""country numeric code parameters error""")
        if select == 'official':
            name = data[language]["countries"][code]

            if isinstance(name, list):
                return name[0]
            return name
    
        if select == 'alias':
            name = data[language]["countries"][code]
            if isinstance(name, list) and len(name) >=2:
                return name[1]
            return name

        if select == 'all':
            name = data[language]["countries"][code]
            if isinstance(name, list):
                return name
            return [name,]

    raise ValueError("""parameters error""")


def get_supported_languages():
    """
    Get all supported languages (ISO 639-1)

    Returns:
    - list: ["af","az","bn","cs",...]
    """

    languages = os.listdir(os.path.join(__lang_data_path, "langs"))
    languages = [ code.replace(".json", "") for code in languages]
    return languages


def alpha3_to_alpha2(code):
    """
    Convert Alpha-3 to Alpha-2 code
    Parameters:
    - code (str): 3 letter iso-3166-1 country code

    Returns:
    - str: US
    """

    for code2, code3, _, _ in codes:
        if code == code3:
            return code2
    return None


def numeric_to_alpha2(code):
    """
    Convert Numeric to Alpha-2 code
    Parameters:
    - code (str): numberic iso-3166-1 country code, eg: 840

    Returns:
    - str: US
    """

    for code2, _, num, _ in codes:
        if code == num:
            return code2
    return None


def alpha2_to_alpha3(code):
    """
    Convert Alpha-2 to Alpha-3 code
    Parameters:
    - code (str): 2 letter iso-3166-1 country code, eg: US

    Returns:
    - str: USA
    """

    for code2, code3, _, _ in codes:
        if code == code2:
            return code3
    return None


def numeric_to_alpha3(code):
    """
    Convert Numeric to Alpha-3 code
    Parameters:
    - code (str): numberic iso-3166-1 country code, eg:840

    Returns:
    - str: USA
    """

    for _, code3, num, _ in codes:
        if code == num:
            return code3
    return None


def alpha3_to_numeric(code):
    """
    Convert Alpha-3 to Numeric code
    Parameters:
    - code (str): 3 letter iso-3166-1 country code, eg:SWE

    Returns:
    - str: 752
    """

    for _, code3, num, _ in codes:
        if code == code3:
            return num
    return None

def alpha2_to_numeric(code):
    """
     Convert Alpha-2 to Numeric code
    Parameters:
    - code (str): 2 letter iso-3166-1 country code, eg:SE

    Returns:
    - str: 752
    """

    for code2, _, num, _ in codes:
        if code == code2:
            return num
    return None


def get_alpha2_codes():
    """
     Get all Alpha-2 codes
    

    Returns:
    - dict: { 'AF': 'AFG', 'AX': 'ALA', [...], 'ZM': 'ZMB', 'ZW': 'ZWE' }
    """

    data={}
    for code2, code3, _, _ in codes:
        data[code2] = code3
    return data


def get_alpha3_codes():
    """
     Get all Alpha-3 codes
    

    Returns:
    - dict: { 'AFG': 'AF', 'ALA': 'AX', [...], 'ZMB': 'ZM', 'ZWE': 'ZW' }
    """

    data={}
    for code2, code3, _, _ in codes:
        data[code3] = code2
    return data


def get_numeric_codes():
    """
     Get all Numeric codes
    

    Returns:
    - dict: { '004': 'AF', '008': 'AL', [...], '887': 'YE', '894': 'ZM' }
    """

    data={}
    for code2, _, num, _ in codes:
        data[num] = code2
    return data


def is_valid_country_code(code):
    """
    Validate country code
    

    Returns:
    - boolean: False/True
    """

    if len(code) == 2:
        code = code.upper()
        for code2, _, _, _ in codes:
            if code2 == code:
                return True
    if len(code) == 3 and code.isdigit():
        for _, _, num, _ in codes:
            if code == num:
                return True
    if len(code) == 3 and not code.isdigit():
        code = code.upper()
        for _, code3, _, _ in codes:
            if code3 == code:
                return True
    return False