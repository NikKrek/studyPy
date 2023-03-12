import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


def estimate_score(attendance_value, activity_value):
    # Definition of input and output data
    # Setting attendance ranges in the range of 0 - 100 with a step of 1
    attendance = ctrl.Antecedent(np.arange(0, 100, 1), 'attendance')
    # Setting activity ranges in the range of 1 - 5 with a step of 0.1
    activity = ctrl.Antecedent(np.arange(1, 5, 0.1), 'activity')
    # Setting the rating range in the range of 1 - 5 with a step of 0.1
    mark = ctrl.Consequent(np.arange(2, 5, 0.1), 'mark')

    # Define attendance functions
    # gaussmf (Gauss function) with 3 dependence functions was applied
    attendance['bad'] = fuzz.gaussmf(attendance.universe, 0, 21.23)
    attendance['average'] = fuzz.gaussmf(attendance.universe, 50, 21.23)
    attendance['well'] = fuzz.gaussmf(attendance.universe, 100.634249471459, 21.23)

    # Define attendance functions
    # gaussmf (Gauss function) with 3 dependence functions was applied
    activity['low'] = fuzz.gaussmf(activity.universe, 1, 0.8492)
    activity['moderate'] = fuzz.gaussmf(activity.universe, 3, 0.8492)
    activity['high'] = fuzz.gaussmf(activity.universe, 5, 0.8492)

    # Define attendance functions
    # trapmf (trapezium membership function) with 4 dependence functions was applied
    mark['unsatisfactory'] = fuzz.trapmf(mark.universe, [1.1, 1.9, 2.1, 2.9])
    mark['satisfactory'] = fuzz.trapmf(mark.universe, [2.1, 2.9, 3.1, 3.9])
    mark['very satisfactory'] = fuzz.trapmf(mark.universe, [3.1, 3.9, 4.1, 4.9])
    mark['excellent'] = fuzz.trapmf(mark.universe, [4.1, 4.9, 5.1, 5.9])

    # Definition of rules
    rule1 = ctrl.Rule(attendance['bad'] & activity['low'], mark['unsatisfactory'])
    rule2 = ctrl.Rule(attendance['bad'] & activity['moderate'], mark['satisfactory'])
    rule3 = ctrl.Rule(attendance['bad'] & activity['high'], mark['very satisfactory'])
    rule4 = ctrl.Rule(attendance['average'] & activity['low'], mark['satisfactory'])
    rule5 = ctrl.Rule(attendance['average'] & activity['moderate'], mark['very satisfactory'])
    rule6 = ctrl.Rule(attendance['average'] & activity['high'], mark['excellent'])
    rule7 = ctrl.Rule(attendance['well'] & activity['low'], mark['very satisfactory'])
    rule8 = ctrl.Rule(attendance['well'] & activity['moderate'], mark['excellent'])
    rule9 = ctrl.Rule(attendance['well'] & activity['high'], mark['excellent'])

    # Define the management system
    system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
    simulator = ctrl.ControlSystemSimulation(system)

    # Simulation
    simulator.input['attendance'] = attendance_value
    simulator.input['activity'] = activity_value
    simulator.compute()

    # Evaluation data output
    print('Estimated score:', simulator.output['mark'])

    # Graphing membership and outcome functions
    attendance.view()
    activity.view()
    mark.view()
    plt.axvline(x=simulator.output['mark'], color='r')
    plt.show()


if __name__ == "__main__":
    estimate_score(84.3, 1.57)
