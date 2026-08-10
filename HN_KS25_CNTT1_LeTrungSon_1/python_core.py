raw_rooms = [
    {"room_no": "R301", "type": "deluxe", "price": 1200000, "status": "available"},
    {"room_no": " r101 ", "type": "standard", "price": 500000, "status": "available"},
    {"room_no": "R202", "type": "suite", "price": 2500000, "status": "occupied"},
    {"room_no": "R102", "type": "standard", "price": 600000, "status": "maintenance"},
    {"room_no": "R302", "type": "deluxe", "price": 1500000, "status": "available"},
]


def clean_and_validate_rooms(rooms):
    result = []
    for r in rooms:
        code = r["room_no"].strip().upper()
        if code.startswith("R") and code[1:].isdigit():
            new_room = dict(r)
            new_room["room_no"] = code
            result.append(new_room)
    return result


def search_rooms(room_price, room_status, rooms):
    result = []
    for r in rooms:
        if r["price"] <= room_price:
            if room_status is None or r["status"] == room_status:
                result.append(r)
    return result


def sort_rooms_by_price_desc(rooms):
    data = list(rooms)
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j]["price"] < data[j + 1]["price"]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data