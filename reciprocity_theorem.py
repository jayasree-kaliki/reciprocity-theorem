# Python Program to Verify Reciprocity Theorem
# Electrical Engineering - Network Analysis

print("==============================================")
print("           RECIPROCITY THEOREM")
print("==============================================")

# Input circuit values
V1 = float(input("Enter source voltage V1 (V): "))
R1 = float(input("Enter R1 (ohm): "))
R2 = float(input("Enter R2 (ohm): "))
R3 = float(input("Enter R3 (ohm): "))

# ------------------------------------------------
# Case 1:
# Source V1 is connected at input side
# Calculate current through output branch
# ------------------------------------------------

I1 = V1 / (R1 + R2 + R3)

# Current response at output
I_output_1 = I1

# ------------------------------------------------
# Case 2:
# Interchange source and response positions
# Apply the same voltage at output side
# ------------------------------------------------

I2 = V1 / (R1 + R2 + R3)

# Current response at original source position
I_output_2 = I2

# ------------------------------------------------
# Compare the two responses
# ------------------------------------------------

print("\n------------- RESULTS ----------------")
print(f"Current in Case 1 = {I_output_1:.4f} A")
print(f"Current in Case 2 = {I_output_2:.4f} A")

print("--------------------------------------")

if abs(I_output_1 - I_output_2) < 0.000001:
    print("Reciprocity Theorem is VERIFIED")
else:
    print("Reciprocity Theorem is NOT VERIFIED")

print("======================================")
