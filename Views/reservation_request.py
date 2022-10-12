RESERVATIONS = [
    {
        "id": 1,
        "parent": "Brad",
        "child": "Billy",
        "childAttendees": 17,
        "address": "123 Risk Way",
        "date": "October 3, 2022",
        "hours": 4
    },
    {
        "parent": "Ed",
        "child": "Eddie",
        "childAttendees": "17",
        "address": "123 Howling Way",
        "date": "2022-09-23",
        "hours": "7",
        "id": 2
    },
    {
        "parent": "Vick",
        "child": "Victor",
        "childAttendees": "18",
        "address": "67 Wolf Street",
        "date": "2022-08-17",
        "hours": "9",
        "id": 3
    },
    {
        "parent": "Leo",
        "child": "Lex",
        "childAttendees": "6",
        "address": "34 Ro Way",
        "date": "2022-08-30",
        "hours": "3",
        "id": 4
    },
    {
        "parent": "Arthur",
        "child": "Willow",
        "childAttendees": "4",
        "address": "56 Hope Hw",
        "date": "2022-08-31",
        "hours": "4",
        "id": 5
    },
    {
        "parent": "Christine",
        "child": "Amanda",
        "childAttendees": "15",
        "address": "45 go way",
        "date": "2022-08-30",
        "hours": "5",
        "id": 6
    }
]

def get_all_reservations():
    return RESERVATIONS

def get_single_reservation(id):
    requested_reservation = None

    for reservation in RESERVATIONS:
        if reservation["id"] == id:
            requested_reservation = reservation

    return requested_reservation

