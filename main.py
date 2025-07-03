import streamlit as st
from triangle_area import Triangle

# Create object of Triangle class
tri = Triangle()

st.title("Triangle Area Calculator")

option = st.selectbox(
    "Choose the method to calculate the area:",
    ("Base and Height", "Three Sides", "Two Sides and Included Angle")
)

if option == "Base and Height":
    base = st.number_input("Enter base", min_value=0.0, format="%.2f")
    height = st.number_input("Enter height", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        area = 0.5 * base * height
        st.success(f"Area using base and height: {area:.2f}")

elif option == "Three Sides":
    a = st.number_input("Enter side a", min_value=0.0, format="%.2f")
    b = st.number_input("Enter side b", min_value=0.0, format="%.2f")
    c = st.number_input("Enter side c", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        try:
            area = tri.area_sides(a, b, c)
            st.success(f"Area using sides ({a}, {b}, {c}): {area:.2f}")
        except ValueError:
            st.error("Invalid triangle sides. Please check the values.")

elif option == "Two Sides and Included Angle":
    a = st.number_input("Enter side a", min_value=0.0, format="%.2f")
    b = st.number_input("Enter side b", min_value=0.0, format="%.2f")
    angle = st.number_input("Enter included angle (in degrees)", min_value=0.0, max_value=180.0, format="%.2f")
    if st.button("Calculate Area"):
        area = tri.area_included_angle(a, b, angle)
        st.success(f"Area using sides {a}, {b} and angle {angle}°: {area:.2f}")
