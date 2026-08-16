import streamlit as st
import joblib
import pandas as pd


# -----------------------------
# Load files
# -----------------------------

model = joblib.load("xgb_capped_model.pkl")
features = joblib.load("final_features.pkl")
results = pd.read_csv("final_predictions.csv")


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="AI Predictive Maintenance",
    page_icon="⚙️",
    layout="wide"
)


# -----------------------------
# Custom styling
# -----------------------------

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    font-size: 18px;
    margin-bottom: 25px;
}

.card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #ddd;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Title
# -----------------------------

st.markdown(
    '<div class="main-title">⚙️ AI Predictive Maintenance System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-powered Remaining Useful Life prediction and machine health monitoring'
    '</div>',
    unsafe_allow_html=True
)


st.success("AI model loaded successfully!")


# -----------------------------
# Fleet overview
# -----------------------------

st.header("📊 Fleet Overview")


healthy_count = (results["status"] == "Healthy").sum()
warning_count = (results["status"] == "Warning").sum()
critical_count = (results["status"] == "Critical").sum()

total_machines = len(results)


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Total Machines",
        total_machines
    )

with col2:
    st.metric(
        "🟢 Healthy",
        healthy_count
    )

with col3:
    st.metric(
        "🟡 Warning",
        warning_count
    )

with col4:
    st.metric(
        "🔴 Critical",
        critical_count
    )


# -----------------------------
# Machine selection
# -----------------------------

st.sidebar.header("🏭 Machine Selection")

machine_id = st.sidebar.selectbox(
    "Select Machine ID",
    sorted(results["unit_id"].unique())
)


machine = results[
    results["unit_id"] == machine_id
].iloc[0]


# -----------------------------
# Machine report
# -----------------------------

st.header(f"🔍 Machine {machine_id} Health Report")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Predicted RUL",
        f"{machine['predicted_RUL']:.1f} cycles"
    )


with col2:

    st.metric(
        "Health Status",
        machine["status"]
    )


with col3:

    st.metric(
        "Estimated Degradation",
        machine["estimated_fault_mode"]
    )


# -----------------------------
# Degradation indicators
# -----------------------------

st.header("📈 Degradation Indicators")


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "HPC Recent Score",
        f"{machine['HPC_recent_score']:.2f}"
    )


with col2:

    st.metric(
        "Fan Recent Score",
        f"{machine['Fan_recent_score']:.2f}"
    )


# -----------------------------
# Compare degradation
# -----------------------------

score_data = pd.DataFrame({
    "Subsystem": ["HPC", "Fan"],
    "Score": [
        machine["HPC_recent_score"],
        machine["Fan_recent_score"]
    ]
})

st.bar_chart(
    score_data.set_index("Subsystem")
)


# -----------------------------
# Maintenance recommendation
# -----------------------------

st.header("🔧 Maintenance Recommendation")


if machine["status"] == "Critical":

    st.error(
        "🔴 CRITICAL: Immediate maintenance inspection is recommended."
    )

elif machine["status"] == "Warning":

    st.warning(
        "🟡 WARNING: Schedule maintenance inspection soon."
    )

else:

    st.success(
        "🟢 HEALTHY: Continue normal monitoring."
    )


# -----------------------------
# Machine details
# -----------------------------

st.header("📋 Machine Details")


details = pd.DataFrame({
    "Parameter": [
        "Machine ID",
        "Last Operating Cycle",
        "Predicted RUL",
        "Health Status",
        "HPC Score",
        "Fan Score",
        "Estimated Degradation"
    ],

    "Value": [
        machine["unit_id"],
        machine["cycle"],
        f"{machine['predicted_RUL']:.2f} cycles",
        machine["status"],
        f"{machine['HPC_recent_score']:.2f}",
        f"{machine['Fan_recent_score']:.2f}",
        machine["estimated_fault_mode"]
    ]
})


st.table(details)


# -----------------------------
# Footer
# -----------------------------

st.markdown("---")

st.caption(
    "AI Predictive Maintenance | XGBoost-based RUL Prediction | NASA C-MAPSS FD004"
)