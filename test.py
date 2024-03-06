import linear_motion

missing_value = "initial velocity"
givens = {
    "final velocity" : 10,
    "time" : 4,
    "acceleration" : 5
    }

linear_motion.determine_equation(missing_value, givens)