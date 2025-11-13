"""
The Financial Gearbox - Streamlit Web Application
An interactive web app for automated budget allocation
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from financial_gearbox import FinancialGearbox

# Page configuration
st.set_page_config(
    page_title="The Financial Gearbox",
    page_icon="⚙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #7f8c8d;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #3498db;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'gearbox' not in st.session_state:
    st.session_state.gearbox = FinancialGearbox()

# Header
st.markdown('<h1 class="main-header">⚙ The Financial Gearbox</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">An Automated Budget Allocation System</p>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar for inputs
with st.sidebar:
    st.header("⚙️ Configuration")
    st.markdown("### Select Life Stage")
    
    # Life stage selector
    life_stage = st.selectbox(
        "Choose your current life stage:",
        options=list(st.session_state.gearbox.GEAR_RATIOS.keys()),
        help="Select the life stage that best describes your current situation"
    )
    
    # Display gear ratios for selected stage
    ratios = st.session_state.gearbox.GEAR_RATIOS[life_stage]
    st.markdown("**Current Gear Ratios:**")
    st.write(f"- Savings: {ratios[0]*100:.0f}%")
    st.write(f"- Expenses: {ratios[1]*100:.0f}%")
    st.write(f"- Investments: {ratios[2]*100:.0f}%")
    
    st.markdown("---")
    st.markdown("### Enter Income")
    
    # Income input
    income = st.number_input(
        "Monthly Income (₹):",
        min_value=0.0,
        value=50000.0,
        step=1000.0,
        format="%.2f",
        help="Enter your total monthly income"
    )
    
    # Calculate button
    calculate_button = st.button("🔄 Calculate Allocation", type="primary", use_container_width=True)

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📊 Budget Allocation")
    
    if calculate_button or income > 0:
        # Set life stage and calculate
        st.session_state.gearbox.set_life_stage(life_stage)
        allocations = st.session_state.gearbox.calculate_allocation(income)
        
        # Display metrics
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        
        with metric_col1:
            st.metric(
                label="💰 Savings",
                value=f"₹{allocations['Savings']:,.0f}",
                delta=f"{ratios[0]*100:.0f}%"
            )
        
        with metric_col2:
            st.metric(
                label="💳 Expenses",
                value=f"₹{allocations['Expenses']:,.0f}",
                delta=f"{ratios[1]*100:.0f}%"
            )
        
        with metric_col3:
            st.metric(
                label="📈 Investments",
                value=f"₹{allocations['Investments']:,.0f}",
                delta=f"{ratios[2]*100:.0f}%"
            )
        
        # Detailed breakdown
        st.markdown("### Detailed Breakdown")
        breakdown_df = pd.DataFrame([
            {"Category": "Savings", "Amount (₹)": allocations['Savings'], "Percentage": f"{ratios[0]*100:.1f}%"},
            {"Category": "Expenses", "Amount (₹)": allocations['Expenses'], "Percentage": f"{ratios[1]*100:.1f}%"},
            {"Category": "Investments", "Amount (₹)": allocations['Investments'], "Percentage": f"{ratios[2]*100:.1f}%"}
        ])
        st.dataframe(breakdown_df, use_container_width=True, hide_index=True)

with col2:
    st.header("📈 Visualizations")
    
    if calculate_button or income > 0:
        # Pie chart
        st.subheader("Pie Chart")
        fig_pie, ax_pie = plt.subplots(figsize=(8, 8))
        labels = list(allocations.keys())
        values = list(allocations.values())
        colors = ['#2ecc71', '#e74c3c', '#3498db']
        
        ax_pie.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
        ax_pie.set_title(f'{life_stage} Stage\nTotal Income: ₹{income:,.2f}', 
                        fontsize=12, fontweight='bold')
        st.pyplot(fig_pie)
        
        # Bar chart
        st.subheader("Bar Chart")
        fig_bar, ax_bar = plt.subplots(figsize=(8, 6))
        bars = ax_bar.bar(labels, values, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
        
        # Add value labels on bars
        for bar, value in zip(bars, values):
            height = bar.get_height()
            ax_bar.text(bar.get_x() + bar.get_width()/2., height,
                       f'₹{value:,.0f}',
                       ha='center', va='bottom', fontweight='bold')
        
        ax_bar.set_title(f'{life_stage} Stage - Budget Allocation', fontsize=12, fontweight='bold')
        ax_bar.set_ylabel('Amount (₹)', fontsize=10)
        ax_bar.set_xlabel('Category', fontsize=10)
        ax_bar.grid(axis='y', alpha=0.3, linestyle='--')
        plt.xticks(rotation=0)
        st.pyplot(fig_bar)

# Information section
st.markdown("---")
st.header("ℹ️ About The Financial Gearbox")

col_info1, col_info2 = st.columns(2)

with col_info1:
    st.markdown("""
    ### 🧠 Concept
    Just as a car uses a gearbox to shift gears depending on terrain, 
    individuals need to shift their financial strategies based on changing 
    life conditions. The Financial Gearbox automatically adjusts budget 
    allocations based on your life stage.
    """)

with col_info2:
    st.markdown("""
    ### ⚙️ How It Works
    - **Torque** → Represents financial power (income)
    - **Speed** → Represents cash flow
    - **Gears** → Represent life stages (adjusting ratios to maintain balance)
    - **Control System** → Automatically shifts to maintain financial efficiency
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #7f8c8d; padding: 1rem;'>"
    "⚙ The Financial Gearbox - Applying Mechanical and Automation Principles to Personal Finance"
    "</div>",
    unsafe_allow_html=True
)

