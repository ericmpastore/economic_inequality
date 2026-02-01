import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analyze_gini_trends(csv_file='GINIUSA.csv'):
    """
    Analyze GINI coefficient trends over time and create a visualization.

    EPastore 02/01/26, Analyze GINI coefficient trends over time and create a visualization.
    
    Parameters:
    csv_file: Path to the CSV file containing GINI coefficient data
    """
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Convert dates to datetime
    df['observation_date'] = pd.to_datetime(df['observation_date'])
    
    # Sort by date to ensure proper ordering
    df = df.sort_values('observation_date')
    
    # Extract data
    dates = df['observation_date']
    gini_values = df['SIPOVGINIUSA']
    
    # Calculate basic statistics
    start_year = dates.iloc[0].year
    end_year = dates.iloc[-1].year
    start_gini = gini_values.iloc[0]
    end_gini = gini_values.iloc[-1]
    min_gini = gini_values.min()
    max_gini = gini_values.max()
    avg_gini = gini_values.mean()
    change = end_gini - start_gini
    percent_change = (change / start_gini) * 100
    
    # Print analysis
    print("=" * 60)
    print("GINI COEFFICIENT TREND ANALYSIS")
    print("=" * 60)
    print(f"Data Period: {start_year} - {end_year}")
    print(f"Starting GINI: {start_gini:.1f}")
    print(f"Ending GINI: {end_gini:.1f}")
    print(f"Change: {change:+.1f} ({percent_change:+.1f}%)")
    print(f"Minimum GINI: {min_gini:.1f} (Year: {dates[gini_values == min_gini].iloc[0].year})")
    print(f"Maximum GINI: {max_gini:.1f} (Year: {dates[gini_values == max_gini].iloc[0].year})")
    print(f"Average GINI: {avg_gini:.1f}")
    print("=" * 60)
    
    # Create the plot
    plt.figure(figsize=(12, 7))
    plt.plot(dates, gini_values, linewidth=2, color='#2E86AB', marker='o', markersize=4)
    
    # Set y-axis to start at 0
    plt.ylim(bottom=0)
    
    # Label only the first and last data points
    # First point
    plt.annotate(f'{start_gini:.1f}', 
                xy=(dates.iloc[0], gini_values.iloc[0]), 
                xytext=(10, 10), 
                textcoords='offset points',
                fontsize=11,
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    
    # Last point
    plt.annotate(f'{end_gini:.1f}', 
                xy=(dates.iloc[-1], gini_values.iloc[-1]), 
                xytext=(10, 10), 
                textcoords='offset points',
                fontsize=11,
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    
    # Formatting
    plt.xlabel('Year', fontsize=12, fontweight='bold')
    plt.ylabel('GINI Coefficient', fontsize=12, fontweight='bold')
    plt.title('GINI Coefficient Trend in the United States (1963-2023)', 
              fontsize=14, fontweight='bold', pad=20)
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('gini_trend_analysis.png', dpi=300, bbox_inches='tight')
    print(f"\nPlot saved as 'gini_trend_analysis.png'")
    
    # Show the plot
    plt.show()
    
    # Economic interpretation
    print("\n" + "=" * 60)
    print("ECONOMIC INTERPRETATION")
    print("=" * 60)
    if change > 0:
        print(f"• The GINI coefficient increased by {change:.1f} points from {start_year} to {end_year}.")
        print("  This indicates rising income inequality over the period.")
    else:
        print(f"• The GINI coefficient decreased by {abs(change):.1f} points from {start_year} to {end_year}.")
        print("  This indicates declining income inequality over the period.")
    
    print(f"• The coefficient ranges from {min_gini:.1f} to {max_gini:.1f}, showing")
    print("  significant variation in income distribution over time.")
    print("• A GINI coefficient of 0 represents perfect equality, while 100 represents")
    print("  perfect inequality. The US values indicate moderate to high inequality.")
    print("=" * 60)

if __name__ == "__main__":
    analyze_gini_trends()
