# Motion Type Identifier Template

 

# Function 1: Convert velocity to m/s

def convert_velocity(value, unit):
    if unit == "m/s":
        return value
    elif unit == "ft/s":
        return value
    elif unit == "km/s":
        return value
    elif unit == "mi/s":
        return value
print("Invalid velocity unit")




 

# Function 2: Convert acceleration to m/s²

def convert_acceleration(value, unit):
    if unit == "m/s²":
        return value
    elif unit == "ft/s²":
        return value * 0.3048
    elif unit == "km/s²":
        return value * 1000
    elif unit == "mi/s²":
        return value * 1609.344
    else:
        raise ValueError("Unsupported acceleration unit. Please use m/s², ft/s², km/s², or mi/s².")

    """

    Convert acceleration to meters per second squared (m/s²)

    Supported units: m/s², ft/s², km/s², mi/s²

    """

   

 

# Function 3: Determine motion type

def motion_type(v, a):
    if abs(v) < 1e-9:
        return "At Rest"
    elif v > 0 and abs(a) < 1e-9:
        return "Uniform Motion"
    elif v > 0 and a > 0:
        return "Accelerated Motion"
    elif v > 0 and a < 0:
        return "Decelerated Motion"
    else:
        return "Complex or non-standard motion"





# --- Main Program ---

 

# Step 1: Input velocity

v_value = float(input("Enter velocity value: "))

v_unit = input("Enter velocity unit (m/s, ft/s, km/s, mi/s): ")

 

# Step 2: Input acceleration

a_value = float(input("Enter acceleration value: "))

a_unit = input("Enter acceleration unit (m/s², ft/s², km/s², mi/s²): ")

 

# Step 3: Convert to SI units

v_si = convert_velocity(v_value, v_unit)      # TODO: Call the conversion function

a_si = convert_acceleration(a_value, a_unit)  # TODO: Call the conversion function

 

# Step 4: Determine motion type

motion = motion_type(v_si, a_si)              # TODO: Call the motion type function

 

# Step 5: Display results

print("\n--- Results ---")

print(f"Velocity = {v_si:.3f} m/s")

print(f"Acceleration = {a_si:.3f} m/s²")

print(f"Motion Type = {motion}")