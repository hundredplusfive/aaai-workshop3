def country_cost() -> dict:
    """
    Returns a detailed cost breakdown per country (in USD).
    Prices are rough averages and meant for demonstration.
    """
    cost_data = {
        "Malaysia": {
            "average_flight": 400,
            "hotel_per_night": 150,
            "food_per_day": 40,
            "local_transport_per_day": 15,
            "daily_budget": 205,  # hotel + food + transport
            "recommended_trip_days": 5,
            "currencies": "SGD",
        },
        "Japan": {
            "average_flight": 700,
            "hotel_per_night": 120,
            "food_per_day": 35,
            "local_transport_per_day": 20,
            "daily_budget": 175,
            "recommended_trip_days": 7,
            "currencies": "SGD",
        },
        "Australia": {
            "average_flight": 900,
            "hotel_per_night": 130,
            "food_per_day": 30,
            "local_transport_per_day": 18,
            "daily_budget": 178,
            "recommended_trip_days": 7,
            "currencies": "SGD",
        },
        "Brazil": {
            "average_flight": 800,
            "hotel_per_night": 90,
            "food_per_day": 25,
            "local_transport_per_day": 12,
            "daily_budget": 127,
            "recommended_trip_days": 6,
            "currencies": "SGD",
        },
        "Vietnam": {
            "average_flight": 600,
            "hotel_per_night": 40,
            "food_per_day": 15,
            "local_transport_per_day": 8,
            "daily_budget": 63,
            "recommended_trip_days": 5,
            "currencies": "SGD",
        },
        "Portugal": {
            "average_flight": 750,
            "hotel_per_night": 100,
            "food_per_day": 30,
            "local_transport_per_day": 10,
            "daily_budget": 140,
            "recommended_trip_days": 6,
            "currencies": "SGD",
        },
    }
    return cost_data