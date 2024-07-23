invalid_token = 'qqq6oJ0R6oDqyyq'
another_user_token = 'olX6oJ0R6oDQ0La'

TEST_DATA_CREATE = [
    {
        "text": "Relax, it's not a competition",
        "url": "https://i.pinimg.com/474x/95/7d/ee/957dee125eeec88b8c4b2ba493d13182.jpg",
        "tags": ["squirrel_1", "squirrel_2", "squirrel_3"],
        "info": {"squirrel": ["healthy", "sporty"]}
    },
    {
        "text": "How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["password", "shrek"],
        "info": {"password": ["new_password", "wrong_password"]}
    }
]

NEGATIVE_DATA_CREATE = [
    {
        "text": 123,
        "url": "https://i.pinimg.com/474x/95/7d/ee/957dee125eeec88b8c4b2ba493d13182.jpg",
        "tags": ["password", "shrek"],
        "info": {"squirrel": ["healthy", "sporty"]}
    },
    {
        "text": ["password", "shrek"],
        "url": "https://i.pinimg.com/474x/95/7d/ee/957dee125eeec88b8c4b2ba493d13182.jpg",
        "tags": ["password", "shrek"],
        "info": {"squirrel": ["healthy", "sporty"]}
    },
    {
        "text": (1,),
        "url": "https://i.pinimg.com/474x/95/7d/ee/957dee125eeec88b8c4b2ba493d13182.jpg",
        "tags": ["password", "shrek"],
        "info": {"squirrel": ["healthy", "sporty"]}
    },
    {
        "text": None,
        "url": "https://i.pinimg.com/474x/95/7d/ee/957dee125eeec88b8c4b2ba493d13182.jpg",
        "tags": ["password", "shrek"],
        "info": {"squirrel": ["healthy", "sporty"]}
    },
    {
        "url": "https://i.pinimg.com/474x/95/7d/ee/957dee125eeec88b8c4b2ba493d13182.jpg",
        "tags": ["password", "shrek"],
        "info": {"squirrel": ["healthy", "sporty"]}
    },
    {
        "text": "How to enter a password",
        "url": {"squirrel": ["healthy", "sporty"]},
        "tags": ["password", "shrek"],
        "info": {"squirrel": ["healthy", "sporty"]}
    },
    {
        "text": "How to enter a password",
        "url": 123,
        "tags": ["password", "shrek"],
        "info": {"password": ["new_password", "wrong_password"]}
    },
    {
        "text": "Relax, it's not a competition",
        "url": ["password", "shrek"],
        "tags": ["password", "shrek"],
        "info": {"squirrel": ["healthy", "sporty"]}
    },
    {
        "text": "Relax, it's not a competition",
        "url": None,
        "tags": ["password", "shrek"],
        "info": {"squirrel": ["healthy", "sporty"]}
    },
    {
        "text": "Relax, it's not a competition",
        "tags": ["password", "shrek"],
        "info": {"squirrel": ["healthy", "sporty"]}
    },
    {
        "text": "How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": 123,
        "info": {"password": ["new_password", "wrong_password"]}
    },
    {
        "text": "How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": "string",
        "info": {"password": ["new_password", "wrong_password"]}
    },
    {
        "text": "How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": {"squirrel": ["healthy", "sporty"]},
        "info": {"password": ["new_password", "wrong_password"]}
    },
    {
        "text": "How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": None,
        "info": {"password": ["new_password", "wrong_password"]}
    },
    {
        "text": "How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "info": {"password": ["new_password", "wrong_password"]}
    },
    {
        "text": "How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["password", "shrek"],
        "info": 123
    },
    {
        "text": "How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["password", "shrek"],
        "info": ["password", "shrek"]
    },
    {
        "text": "How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["password", "shrek"],
        "info": (1, 2, 3)
    },
    {
        "text": "How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["password", "shrek"],
        "info": None
    },
    {
        "text": "How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["password", "shrek"],
    },
    {
        "text": "How to enter a password"
    }
]

TEST_DATA_UPDATE = {
    "id": 100,
    "text": "Updated - How to enter a password",
    "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
    "tags": ["updated - password", "updated - shrek"],
    "info": {"000": ["111", "222"]}
}

NEGATIVE_DATA_UPDATE = [
    {
        "text": "Updated - How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"000": ["111", "222"]}
    },
    {
        "id": {"000": ["111", "222"]},
        "text": "Updated - How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"000": ["111", "222"]}
    },
    {
        "id": None,
        "text": "Updated - How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"000": ["111", "222"]}
    },
    {
        "id": "string",
        "text": "Updated - How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"000": ["111", "222"]}
    },
    {
        "id": 1,
        "text": 123,
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"000": ["111", "222"]}
    },
    {
        "id": 1,
        "text": {"000": ["111", "222"]},
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"000": ["111", "222"]}
    },
    {
        "id": 1,
        "text": None,
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"000": ["111", "222"]}
    },
    {
        "id": 1,
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"000": ["111", "222"]}
    },
    {
        "id": 1,
        "text": "string",
        "url": 123,
        "tags": ["updated - password", "updated - shrek"],
        "info": {"000": ["111", "222"]}
    },
    {
        "id": 1,
        "text": "string",
        "url": None,
        "tags": ["updated - password", "updated - shrek"],
        "info": {"000": ["111", "222"]}
    },
    {
        "id": 1,
        "text": "string",
        "url": ["updated - password", "updated - shrek"],
        "tags": ["updated - password", "updated - shrek"],
        "info": {"000": ["111", "222"]}
    },
    {
        "id": 1,
        "text": "string",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"000": ["111", "222"]}
    },
    {
        "id": 1,
        "text": "string",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": 123,
        "info": {"000": ["111", "222"]}
    },
    {
        "id": 1,
        "text": "string",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": "string",
        "info": {"000": ["111", "222"]}
    },
    {
        "id": 1,
        "text": "string",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": None,
        "info": {"000": ["111", "222"]}
    },
    {
        "id": 1,
        "text": "string",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "info": {"000": ["111", "222"]}
    },
    {
        "id": 1,
        "text": "string",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": 123
    },
    {
        "id": 1,
        "text": "string",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": None
    },
    {
        "id": 1,
        "text": "string",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": "string"
    },
    {
        "id": 1,
        "text": "string",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["updated - password", "updated - shrek"],
    }
]
