def country_activities() -> str:
    activities_data = {
        "Malaysia": [
            "Explore Kuala Lumpur’s Petronas Towers",
            "Visit Langkawi beaches",
            "Trek in Cameron Highlands",
            "Discover street food in Penang",
            "Explore Borneo’s rainforests"
        ],
        "Japan": [
            "Visit historic temples in Kyoto",
            "Experience cherry blossom season",
            "Explore Tokyo’s vibrant districts",
            "Relax in hot springs (onsen)",
            "Ski in Hokkaido during winter"
        ],
        "Australia": [
            "Dive the Great Barrier Reef",
            "Visit Sydney Opera House",
            "Explore the Outback",
            "Surf at Bondi Beach",
            "Hike in Blue Mountains"
        ],
        "Brazil": [
            "Visit Christ the Redeemer statue",
            "Enjoy Rio Carnival",
            "Explore Amazon rainforest",
            "Relax on Copacabana beach",
            "Discover Iguazu Falls"
        ],
        "Vietnam": [
            "Cruise Ha Long Bay",
            "Explore ancient Hoi An town",
            "Visit Cu Chi Tunnels",
            "Taste street food in Hanoi",
            "Trek in Sapa mountains"
        ],
        "Portugal": [
            "Tour Lisbon’s historic neighborhoods",
            "Relax on Algarve beaches",
            "Visit Porto’s wine cellars",
            "Explore Sintra castles",
            "Enjoy Fado music performances"
        ],
    }

    result = "--- Popular Activities by Country ---\n"
    for country, activities in activities_data.items():
        result += f"\n{country}:\n"
        for activity in activities:
            result += f"- {activity}\n"
    return result

