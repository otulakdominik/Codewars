def get_drink_by_profession(param):
    drinks = {
        "Jabroni": "Patron Tequila", "School counselor": "Anything with Alcohol",
        "Programmer": "Hipster Craft Beer", "Bike gang member": "Moonshine",
        "Politician": "Your tax dollars", "Rapper": "Cristal",
    }
    try:
        return drinks[param.capitalize()]
    except:
        return 'Beer'
