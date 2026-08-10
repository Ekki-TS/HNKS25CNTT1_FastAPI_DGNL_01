from typing import List, Optional

raw_rooms = [ 
    {"room_no": "R301", "type": "deluxe", "price": 1200000, "status": "available"}, 
    {"room_no": " r101 ", "type": "standard", "price": 500000, "status": "available"}, 
    {"room_no": "R202", "type": "suite", "price": 2500000, "status": "occupied"}, 
    {"room_no": "R102", "type": "standard", "price": 600000, "status": "maintenance"}, 
    {"room_no": "R302", "type": "deluxe", "price": 1500000, "status": "available"} 
]

def clean_and_validate_rooms(rooms):
    result = []
    
    for r in raw_rooms:
        code = r["room_no"].strip().upper()
        
        if code.startswith("R") and code[:1].isdigit():
            result.append(code)
        else:
            raw_rooms.remove(code)
    
    return result
            
def search_rooms(room_price: int, room_status: str ,rooms):
    result = []
    
    for r in raw_rooms:
        if (r["price"] <= room_price) and (r["status"] == room_status or None):
            result.append(r)
        else:
            return None
        
    return result

def sort_rooms_by_price_desc(a,b):
    swapped = False
    
    for r in raw_rooms:
        if r[n]["price"] < r[n+1]["price"]:
            a , b = b , a
        else:
            swapped=True
            break
                