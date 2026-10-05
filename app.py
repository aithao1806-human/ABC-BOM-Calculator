import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="ABC Company - BOM Calculator",
    page_icon="📦",
    layout="wide"
)

# =========================================================
# TITLE
# =========================================================

st.title("📦 ABC Company - BOM Material Calculator")

st.markdown(
    """
    **Bill of Materials (BOM), Material Requirement and Cost Planning**

    Use the inputs below to simulate different production demand,
    BOM quantities and material prices.
    """
)

# =========================================================
# CASE INFORMATION
# =========================================================

st.header("1. Case Information")

col1, col2 = st.columns(2)

with col1:
    capacity = st.number_input(
        "Maximum production capacity (CPU / quarter)",
        min_value=0,
        value=1_000_000,
        step=100_000,
        format="%d"
    )

with col2:
    lead_time = st.number_input(
        "Lead time (weeks)",
        min_value=0,
        value=5,
        step=1
    )

# =========================================================
# PRODUCTION DEMAND
# =========================================================

st.header("2. Production Demand")

st.write("Enter the planned CPU production for each quarter.")

q1, q2, q3, q4 = st.columns(4)

with q1:
    demand_q1 = st.number_input(
        "Q1 CPU Demand",
        min_value=0,
        max_value=capacity,
        value=capacity,
        step=100_000,
        format="%d"
    )

with q2:
    demand_q2 = st.number_input(
        "Q2 CPU Demand",
        min_value=0,
        max_value=capacity,
        value=capacity,
        step=100_000,
        format="%d"
    )

with q3:
    demand_q3 = st.number_input(
        "Q3 CPU Demand",
        min_value=0,
        max_value=capacity,
        value=capacity,
        step=100_000,
        format="%d"
    )

with q4:
    demand_q4 = st.number_input(
        "Q4 CPU Demand",
        min_value=0,
        max_value=capacity,
        value=capacity,
        step=100_000,
        format="%d"
    )

demand = {
    "Q1": demand_q1,
    "Q2": demand_q2,
    "Q3": demand_q3,
    "Q4": demand_q4
}

# =========================================================
# BOM INPUT
# =========================================================

st.header("3. Bill of Materials (BOM)")

st.write(
    "Adjust the quantity required per CPU and the unit price. "
    "The total cost will update automatically."
)

# Create columns
col1, col2, col3 = st.columns([2, 2, 2])

with col1:
    st.markdown("### Material")

with col2:
    st.markdown("### Quantity / CPU")

with col3:
    st.markdown("### Unit Price (USD)")

# -------------------------
# SUBSTRATE
# -------------------------

col1, col2, col3 = st.columns([2, 2, 2])

with col1:
    st.write("Substrate")

with col2:
    substrate_qty = st.number_input(
        "Substrate quantity",
        min_value=0.0,
        value=1.0,
        step=1.0,
        key="substrate_qty",
        label_visibility="collapsed"
    )

with col3:
    substrate_price = st.number_input(
        "Substrate price",
        min_value=0.0,
        value=3.00,
        step=0.10,
        format="%.2f",
        key="substrate_price",
        label_visibility="collapsed"
    )

# -------------------------
# CAPACITOR A
# -------------------------

col1, col2, col3 = st.columns([2, 2, 2])

with col1:
    st.write("Capacitor A")

with col2:
    cap_a_qty = st.number_input(
        "Capacitor A quantity",
        min_value=0.0,
        value=10.0,
        step=1.0,
        key="cap_a_qty",
        label_visibility="collapsed"
    )

with col3:
    cap_a_price = st.number_input(
        "Capacitor A price",
        min_value=0.0,
        value=0.10,
        step=0.01,
        format="%.2f",
        key="cap_a_price",
        label_visibility="collapsed"
    )

# -------------------------
# CAPACITOR B
# -------------------------

col1, col2, col3 = st.columns([2, 2, 2])

with col1:
    st.write("Capacitor B")

with col2:
    cap_b_qty = st.number_input(
        "Capacitor B quantity",
        min_value=0.0,
        value=4.0,
        step=1.0,
        key="cap_b_qty",
        label_visibility="collapsed"
    )

with col3:
    cap_b_price = st.number_input(
        "Capacitor B price",
        min_value=0.0,
        value=0.10,
        step=0.01,
        format="%.2f",
        key="cap_b_price",
        label_visibility="collapsed"
    )

# -------------------------
# SOLDER BALL
# -------------------------

col1, col2, col3 = st.columns([2, 2, 2])

with col1:
    st.write("Solder ball")

with col2:
    solder_qty = st.number_input(
        "Solder ball quantity",
        min_value=0.0,
        value=30.0,
        step=1.0,
        key="solder_qty",
        label_visibility="collapsed"
    )

with col3:
    solder_price = st.number_input(
        "Solder ball price",
        min_value=0.0,
        value=0.05,
        step=0.01,
        format="%.2f",
        key="solder_price",
        label_visibility="collapsed"
    )

# -------------------------
# DIE
# -------------------------

col1, col2, col3 = st.columns([2, 2, 2])

with col1:
    st.write("Die")

with col2:
    die_qty = st.number_input(
        "Die quantity",
        min_value=0.0,
        value=1.0,
        step=1.0,
        key="die_qty",
        label_visibility="collapsed"
    )

with col3:
    die_price = st.number_input(
        "Die price",
        min_value=0.0,
        value=10.00,
        step=0.10,
        format="%.2f",
        key="die_price",
        label_visibility="collapsed"
    )

# =========================================================
# STORE BOM DATA
# =========================================================

bom = {
    "Substrate": {
        "qty_per_cpu": substrate_qty,
        "unit_price": substrate_price
    },
    "Capacitor A": {
        "qty_per_cpu": cap_a_qty,
        "unit_price": cap_a_price
    },
    "Capacitor B": {
        "qty_per_cpu": cap_b_qty,
        "unit_price": cap_b_price
    },
    "Solder ball": {
        "qty_per_cpu": solder_qty,
        "unit_price": solder_price
    },
    "Die": {
        "qty_per_cpu": die_qty,
        "unit_price": die_price
    }
}

# =========================================================
# CALCULATE BOM COST PER CPU
# =========================================================

material_cost_per_cpu = 0

for item, data in bom.items():

    material_cost_per_cpu += (
        data["qty_per_cpu"] * data["unit_price"]
    )

# =========================================================
# KEY METRICS
# =========================================================

total_annual_cpu = sum(demand.values())

total_annual_cost = (
    total_annual_cpu * material_cost_per_cpu
)

st.header("4. Key Results")

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        "Total Annual CPU",
        f"{total_annual_cpu:,.0f}"
    )

with m2:
    st.metric(
        "Material Cost / CPU",
        f"${material_cost_per_cpu:,.2f}"
    )

with m3:
    st.metric(
        "Annual Material Budget",
        f"${total_annual_cost:,.2f}"
    )

# =========================================================
# MATERIAL REQUIREMENT BY QUARTER
# =========================================================

st.header("5. Material Requirement by Quarter")

quarterly_data = []

for quarter, cpu_demand in demand.items():

    for item, data in bom.items():

        required_quantity = (
            cpu_demand * data["qty_per_cpu"]
        )

        material_cost = (
            required_quantity * data["unit_price"]
        )

        quarterly_data.append({
            "Quarter": quarter,
            "Material": item,
            "CPU Demand": cpu_demand,
            "Qty / CPU": data["qty_per_cpu"],
            "Required Quantity": required_quantity,
            "Unit Price ($)": data["unit_price"],
            "Material Cost ($)": material_cost
        })

quarterly_df = pd.DataFrame(quarterly_data)

st.dataframe(
    quarterly_df,
    use_container_width=True,
    hide_index=True
)

# =========================================================
# QUARTERLY COST SUMMARY
# =========================================================

st.header("6. Quarterly Material Budget")

quarterly_summary = []

for quarter, cpu_demand in demand.items():

    quarter_cost = (
        cpu_demand * material_cost_per_cpu
    )

    quarterly_summary.append({
        "Quarter": quarter,
        "CPU Demand": cpu_demand,
        "Material Cost ($)": quarter_cost,
        "Cost / CPU ($)": material_cost_per_cpu
    })

quarterly_summary_df = pd.DataFrame(quarterly_summary)

st.dataframe(
    quarterly_summary_df,
    use_container_width=True,
    hide_index=True
)

# =========================================================
# ANNUAL MATERIAL BUDGET
# =========================================================

st.header("7. Annual Material Budget")

annual_data = []

for item, data in bom.items():

    annual_quantity = (
        total_annual_cpu * data["qty_per_cpu"]
    )

    annual_cost = (
        annual_quantity * data["unit_price"]
    )

    annual_data.append({
        "Material": item,
        "Qty / CPU": data["qty_per_cpu"],
        "Annual Quantity": annual_quantity,
        "Unit Price ($)": data["unit_price"],
        "Annual Cost ($)": annual_cost
    })

annual_df = pd.DataFrame(annual_data)

st.dataframe(
    annual_df,
    use_container_width=True,
    hide_index=True
)

# =========================================================
# PURCHASE RELEASE PLAN
# =========================================================

st.header("8. Purchase Release Plan")

quarter_start_dates = {
    "Q1": datetime(2027, 1, 1),
    "Q2": datetime(2027, 4, 1),
    "Q3": datetime(2027, 7, 1),
    "Q4": datetime(2027, 10, 1)
}

purchase_plan = []

for quarter in ["Q1", "Q2", "Q3", "Q4"]:

    production_date = quarter_start_dates[quarter]

    purchase_date = (
        production_date
        - timedelta(weeks=lead_time)
    )

    purchase_plan.append({
        "Quarter": quarter,
        "Production Start": production_date.strftime("%d-%b-%Y"),
        "PO Release Date": purchase_date.strftime("%d-%b-%Y"),
        "CPU Demand": demand[quarter]
    })

purchase_df = pd.DataFrame(purchase_plan)

st.dataframe(
    purchase_df,
    use_container_width=True,
    hide_index=True
)

# =========================================================
# BOM COST BREAKDOWN
# =========================================================

st.header("9. BOM Cost Breakdown per CPU")

cost_breakdown = []

for item, data in bom.items():

    cost_per_cpu = (
        data["qty_per_cpu"] *
        data["unit_price"]
    )

    cost_breakdown.append({
        "Material": item,
        "Qty / CPU": data["qty_per_cpu"],
        "Unit Price ($)": data["unit_price"],
        "Cost / CPU ($)": cost_per_cpu
    })

cost_df = pd.DataFrame(cost_breakdown)

st.dataframe(
    cost_df,
    use_container_width=True,
    hide_index=True
)

# =========================================================
# FINAL SUMMARY
# =========================================================

st.success(
    f"""
    **Total 2027 CPU production:** {total_annual_cpu:,.0f} CPU

    **Material cost per CPU:** ${material_cost_per_cpu:,.2f}

    **Total annual material budget:** ${total_annual_cost:,.2f}

    **Lead time:** {lead_time} weeks
    """
)
