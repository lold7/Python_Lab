zodiac_constellations = (
    ("Aries"),
    ("Taurus"),
    ("Gemini"),
    ("Cancer"),
    ("Leo"),
    ("Virgo"),
    ("Libra"),
    ("Scorpio"),
    ("Sagittarius"),
    ("Capricorn"),
    ("Aquarius"),
    ("Pisces")
)
symbol = (
    ("Ram"),
    ("Bull"),
    ("Twins"),
    ("Crab"),
    ("Lion"),
    ("Maiden"),
    ("Scales"),
    ("Scorpion"),
    ("Archer"),
    ("Goat"),
    ("Water Bearer"),
    ("Fish")
)

for i in range(2565,2571):
    index = (i + 5) % 12
    print(f"Year: {i} Zodiac: {zodiac_constellations[index]} Symbol: {symbol[index]}")