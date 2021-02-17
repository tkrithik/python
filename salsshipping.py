def ground_shipping(weight):
    flat_charge = 20.00
    if weight <= 2:
        price_per_lbs = 1.50
    elif weight <= 6:
        price_per_lbs = 3.00
    elif weight <= 10:
        price_per_lbs = 4.00
    else:
        price_per_lbs = 4.75
    before = weight * price_per_lbs
    cost = before + flat_charge
    return cost


# print(ground_shipping(8.4))

def drone_shipping(weight):
    if weight <= 2:
        price_per_lbs = 4.50
    elif weight <= 6:
        price_per_lbs = 9.00
    elif weight <= 10:
        price_per_lbs = 12.00
    else:
        price_per_lbs = 14.25
    cost = weight * price_per_lbs
    return cost


# print(drone_shipping(1.5))

weight = 1
ground = ground_shipping(weight)
premium_ground_shipping = 125.00
drone = drone_shipping(weight)


def best_shipping():
    if ground < premium_ground_shipping and ground < drone:
        method = "Ground shipping"
        cost = ground
    elif premium_ground_shipping < ground and premium_ground_shipping < drone:
        method = "Premium ground shipping"
        cost = premium_ground_shipping
    elif drone < premium_ground_shipping and drone < ground:
        method = "Drone shipping"
        cost = drone
    elif ground == premium_ground_shipping:
        method = "Ground shipping or premium ground shipping"
        cost = ground
    elif ground == drone and ground < premium_ground_shipping:
        method = "Ground shipping or drone shipping"
        cost = ground
    elif premium_ground_shipping == drone and premium_ground_shipping < ground:
        method = "Premium ground shipping or drone shipping"
        cost = premium_ground_shipping
    else:
        method = "Any method"
        cost = ground

    return method + " is the best option, as it only costs " + str(cost) + " to ship a " + str(
        weight) + " pound package!"


print(best_shipping)