def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.
    :param :    temperature (int or float): The temperature value in kelvin.
                neutrons_emitted (int or float): The number of neutrons emitted per second.
    :return:    bool: Is criticality balanced?
    """
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True
    else:
        return False 

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param: voltage (int or float): Voltage value.
            current (int or float): Current value.
            theoretical_max_power (int or float): The power level that corresponds to a 100% efficiency.
    :return: str: One of ('green', 'orange', 'red', or 'black').
    """
    generated_power = voltage * current
    perc_value = (generated_power/theoretical_max_power)*100

    if perc_value >= 80:
        return "green"
    elif perc_value < 80 and perc_value >= 60:
        return "orange"
    elif perc_value >= 30 and perc_value < 60:
        return "red"
    else:
        return "black"
        
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.
    
    :param: temperature (int or float): The value of the temperature in kelvin.
            neutrons_produced_per_second (int or float): The neutron flux.
            threshold (int or float): The threshold for the category.
    :return: str: green, orange, red or black.
    """
    if temperature * neutrons_produced_per_second < (0.9 * threshold):    # < 90%
        return "LOW"
    elif temperature * neutrons_produced_per_second <= (1.1 * threshold): # 90%–110%
        return "NORMAL"
    else:
        return "DANGER"
