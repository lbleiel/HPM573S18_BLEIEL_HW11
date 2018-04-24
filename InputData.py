POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 15  # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1/52        # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03

# PROBLEM 1 MATRIX
RATE_MATRIX = [
    [None, 0.0136, 0, 0.00151, 0.0178], # Well
    [0, None, 52, 0, 0], # Stroke
    [0, 0.000408, None, 0.000102, 0.0178], # Post-Stroke
    [0, 0, 0, None, 0], #Stroke Death
    [0, 0, 0, 0, None], #Non-stroke death
]

# PROBLEM 2
RATE_ANTICOAG_MATRIX = [
    [None, 0.0136, 0, 0.00151, 0.0178], # Well
    [0, None, 52, 0, 0 ], # Stroke
    [0, 0.00036, None, 0.000102, 0.0187], # Post-Stroke
    [0, 0, 0, None, 0], #Stroke Death
    [0, 0, 0, 0, None], #Non-stroke death
]

# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05


### NEW FOR THIS PROBLEM 5
HEALTH_UTILITY = [
    1,  # well
    0.2,  # stroke
    0.9,  # post-stroke
    0  # dead
]

HEALTH_COST = [
    0,
    5000,  # stroke
    200,  # post-stroke /year
    0
]

ANTICOAG_HEALTH_COST = [
    0,
    5000,  # stroke
    750,  # post-stroke /year
    0
]

Anticoag_COST = 2000