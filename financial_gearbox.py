"""
The Financial Gearbox - An Automated Budget Allocation System
Applies mechanical and automation principles to personal finance
"""

import matplotlib.pyplot as plt
from typing import Dict, Tuple, List


class FinancialGearbox:
    """
    A financial allocation system that automatically adjusts budget ratios
    based on life stages, similar to how a gearbox shifts gears.
    """
    
    # Gear ratios for different life stages
    GEAR_RATIOS: Dict[str, Tuple[float, float, float]] = {
        "Student": (0.10, 0.80, 0.10),      # Savings, Expenses, Investments
        "First Job": (0.30, 0.50, 0.20),
        "Family": (0.25, 0.55, 0.20),
        "Retirement": (0.50, 0.30, 0.20)
    }
    
    def __init__(self):
        """Initialize the Financial Gearbox system."""
        self.current_stage = None
        self.income = 0.0
        self.allocations = {}
    
    def set_life_stage(self, stage: str) -> bool:
        """
        Set the current life stage (gear).
        
        Args:
            stage: Life stage name (Student, First Job, Family, Retirement)
            
        Returns:
            True if stage is valid, False otherwise
        """
        if stage in self.GEAR_RATIOS:
            self.current_stage = stage
            return True
        return False
    
    def calculate_allocation(self, income: float) -> Dict[str, float]:
        """
        Calculate budget allocation based on current life stage and income.
        
        Args:
            income: Total monthly income
            
        Returns:
            Dictionary with allocations for Savings, Expenses, and Investments
        """
        if self.current_stage is None:
            raise ValueError("Life stage must be set before calculating allocation")
        
        if income < 0:
            raise ValueError("Income must be non-negative")
        
        self.income = income
        savings_ratio, expenses_ratio, investments_ratio = self.GEAR_RATIOS[self.current_stage]
        
        self.allocations = {
            "Savings": income * savings_ratio,
            "Expenses": income * expenses_ratio,
            "Investments": income * investments_ratio
        }
        
        return self.allocations
    
    def display_allocation(self) -> None:
        """Display the current allocation in text format."""
        if not self.allocations:
            print("No allocation calculated yet.")
            return
        
        print(f"\n{'='*50}")
        print(f"Financial Gearbox - {self.current_stage} Stage")
        print(f"{'='*50}")
        print(f"Total Income: ₹{self.income:,.2f}")
        print(f"\nBudget Allocation:")
        print(f"  Savings:      ₹{self.allocations['Savings']:,.2f}")
        print(f"  Expenses:     ₹{self.allocations['Expenses']:,.2f}")
        print(f"  Investments:  ₹{self.allocations['Investments']:,.2f}")
        print(f"{'='*50}\n")
    
    def plot_pie_chart(self, save_path: str = None) -> None:
        """
        Create a pie chart visualization of the budget allocation.
        
        Args:
            save_path: Optional path to save the chart image
        """
        if not self.allocations:
            print("No allocation calculated yet. Cannot create chart.")
            return
        
        labels = list(self.allocations.keys())
        values = list(self.allocations.values())
        colors = ['#2ecc71', '#e74c3c', '#3498db']  # Green, Red, Blue
        
        plt.figure(figsize=(10, 8))
        plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
        plt.title(f'Budget Allocation - {self.current_stage} Stage\nTotal Income: ₹{self.income:,.2f}', 
                 fontsize=14, fontweight='bold')
        plt.axis('equal')
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Chart saved to {save_path}")
        
        plt.show()
    
    def plot_bar_chart(self, save_path: str = None) -> None:
        """
        Create a bar chart visualization of the budget allocation.
        
        Args:
            save_path: Optional path to save the chart image
        """
        if not self.allocations:
            print("No allocation calculated yet. Cannot create chart.")
            return
        
        labels = list(self.allocations.keys())
        values = list(self.allocations.values())
        colors = ['#2ecc71', '#e74c3c', '#3498db']  # Green, Red, Blue
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(labels, values, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
        
        # Add value labels on bars
        for bar, value in zip(bars, values):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'₹{value:,.2f}',
                    ha='center', va='bottom', fontweight='bold')
        
        plt.title(f'Budget Allocation - {self.current_stage} Stage\nTotal Income: ₹{self.income:,.2f}', 
                 fontsize=14, fontweight='bold')
        plt.ylabel('Amount (₹)', fontsize=12)
        plt.xlabel('Category', fontsize=12)
        plt.grid(axis='y', alpha=0.3, linestyle='--')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Chart saved to {save_path}")
        
        plt.show()


def main():
    """Main function to demonstrate the Financial Gearbox system."""
    print("⚙ The Financial Gearbox - Automated Budget Allocation System")
    print("=" * 60)
    
    # Initialize the system
    gearbox = FinancialGearbox()
    
    # Display available life stages
    print("\nAvailable Life Stages:")
    for i, stage in enumerate(gearbox.GEAR_RATIOS.keys(), 1):
        ratios = gearbox.GEAR_RATIOS[stage]
        print(f"  {i}. {stage}: Savings {ratios[0]*100:.0f}%, "
              f"Expenses {ratios[1]*100:.0f}%, Investments {ratios[2]*100:.0f}%")
    
    # Get user input
    print("\n" + "-" * 60)
    stage_input = input("\nEnter life stage (Student/First Job/Family/Retirement): ").strip()
    
    if not gearbox.set_life_stage(stage_input):
        print(f"Error: '{stage_input}' is not a valid life stage.")
        return
    
    try:
        income_input = float(input("Enter monthly income (₹): "))
        if income_input < 0:
            print("Error: Income cannot be negative.")
            return
    except ValueError:
        print("Error: Please enter a valid number for income.")
        return
    
    # Calculate and display allocation
    allocations = gearbox.calculate_allocation(income_input)
    gearbox.display_allocation()
    
    # Ask user if they want to see charts
    chart_choice = input("Would you like to see visualizations? (pie/bar/both/none): ").strip().lower()
    
    if chart_choice in ['pie', 'both']:
        gearbox.plot_pie_chart()
    
    if chart_choice in ['bar', 'both']:
        gearbox.plot_bar_chart()


if __name__ == "__main__":
    main()

