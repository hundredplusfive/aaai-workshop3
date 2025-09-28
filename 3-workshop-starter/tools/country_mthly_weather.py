def country_mthly_weather() -> str:
    weather_data = {
        "Malaysia": {
            m: {"temp": "27-31°C", "season": "Hot & humid, frequent rain"} for m in range(1, 13)
        },
        "Japan": {
            1: {"temp": "-1 to 5°C", "season": "Cold & snowy"},
            2: {"temp": "0 to 6°C", "season": "Cold & snowy"},
            3: {"temp": "5 to 12°C", "season": "Spring blossoms"},
            4: {"temp": "12 to 19°C", "season": "Mild & sunny"},
            5: {"temp": "17 to 23°C", "season": "Pleasant & sunny"},
            6: {"temp": "21 to 25°C", "season": "Rainy season"},
            7: {"temp": "25 to 30°C", "season": "Hot & humid"},
            8: {"temp": "26 to 31°C", "season": "Hot & humid"},
            9: {"temp": "22 to 27°C", "season": "Cooling down"},
            10: {"temp": "15 to 21°C", "season": "Autumn foliage"},
            11: {"temp": "8 to 15°C", "season": "Cool & crisp"},
            12: {"temp": "1 to 7°C", "season": "Cold & snowy"},
        },
        "Australia": {
            1: {"temp": "20 to 30°C", "season": "Summer - hot & sunny"},
            2: {"temp": "20 to 29°C", "season": "Summer - hot & sunny"},
            3: {"temp": "17 to 26°C", "season": "Early autumn"},
            4: {"temp": "14 to 22°C", "season": "Autumn"},
            5: {"temp": "10 to 18°C", "season": "Cool & mild"},
            6: {"temp": "7 to 15°C", "season": "Winter - cool"},
            7: {"temp": "6 to 14°C", "season": "Winter - cool"},
            8: {"temp": "8 to 16°C", "season": "Late winter"},
            9: {"temp": "11 to 20°C", "season": "Spring warming"},
            10: {"temp": "14 to 22°C", "season": "Spring"},
            11: {"temp": "17 to 25°C", "season": "Late spring"},
            12: {"temp": "19 to 28°C", "season": "Early summer"},
        },
        "Brazil": {
            1: {"temp": "25 to 30°C", "season": "Summer - hot & humid"},
            2: {"temp": "25 to 30°C", "season": "Summer - hot & humid"},
            3: {"temp": "24 to 29°C", "season": "Warm & humid"},
            4: {"temp": "22 to 27°C", "season": "Autumn"},
            5: {"temp": "20 to 25°C", "season": "Mild & dry"},
            6: {"temp": "18 to 23°C", "season": "Winter - cooler"},
            7: {"temp": "17 to 22°C", "season": "Winter - cooler"},
            8: {"temp": "18 to 23°C", "season": "Late winter"},
            9: {"temp": "20 to 25°C", "season": "Spring warming"},
            10: {"temp": "22 to 27°C", "season": "Spring"},
            11: {"temp": "23 to 28°C", "season": "Warm & humid"},
            12: {"temp": "24 to 29°C", "season": "Warm & humid"},
        },
        "Vietnam": {
            1: {"temp": "15 to 20°C", "season": "Cool & dry"},
            2: {"temp": "17 to 22°C", "season": "Cool & dry"},
            3: {"temp": "20 to 27°C", "season": "Warm & dry"},
            4: {"temp": "23 to 31°C", "season": "Hot & humid"},
            5: {"temp": "25 to 33°C", "season": "Hot & humid"},
            6: {"temp": "25 to 32°C", "season": "Rainy season"},
            7: {"temp": "24 to 31°C", "season": "Rainy season"},
            8: {"temp": "24 to 31°C", "season": "Rainy season"},
            9: {"temp": "24 to 30°C", "season": "Less rain"},
            10: {"temp": "23 to 29°C", "season": "Cool & dry"},
            11: {"temp": "20 to 26°C", "season": "Cool & dry"},
            12: {"temp": "17 to 23°C", "season": "Cool & dry"},
        },
        "Portugal": {
            1: {"temp": "8 to 15°C", "season": "Mild & rainy"},
            2: {"temp": "9 to 16°C", "season": "Mild & rainy"},
            3: {"temp": "11 to 18°C", "season": "Spring begins"},
            4: {"temp": "13 to 20°C", "season": "Spring"},
            5: {"temp": "16 to 23°C", "season": "Warm & sunny"},
            6: {"temp": "20 to 28°C", "season": "Warm & sunny"},
            7: {"temp": "22 to 30°C", "season": "Hot & sunny"},
            8: {"temp": "22 to 30°C", "season": "Hot & sunny"},
            9: {"temp": "20 to 27°C", "season": "Cooling down"},
            10: {"temp": "16 to 22°C", "season": "Mild & rainy"},
            11: {"temp": "12 to 18°C", "season": "Cool & rainy"},
            12: {"temp": "9 to 15°C", "season": "Cool & rainy"},
        }
    }

    result = ""
    for country, months in weather_data.items():
        result += f"--- {country} ---\n"
        for month in range(1, 13):
            data = months[month]
            result += f"Month {month}: Avg Temp {data['temp']}, Season: {data['season']}\n"
        result += "\n"
    return result
