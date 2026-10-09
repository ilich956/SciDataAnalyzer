import os
from sci_analyzer import SciDataAnalyzer

def main():
    print("--- Scientific Data Analyzer ---")
    
    # 1. Define a realistic scientific dataset 
    # (e.g., an Enzyme Kinetics Experiment: Time vs. Concentration)
    experiment_data = {
        "time_minutes": [0, 5, 10, 15, 20, 25, 30],
        "product_concentration_mM": [0.0, 2.5, 4.8, 6.5, 8.0, 8.9, 9.5],
        "temperature_celsius": [37, 37, 37, 37, 37, 37, 37]
    }

    print("Initializing module with experiment data...\n")
    analyzer = SciDataAnalyzer(experiment_data)

    # 2. Calculate and display statistics for a specific metric
    target_metric = "product_concentration_mM"
    print(f"[*] Calculating statistical metrics for '{target_metric}':")
    
    try:
        # Fetching the stats
        stats = analyzer.calculate_statistics(target_metric)
        
        # Formatting the output to 3 decimal places for scientific precision
        print(f"    - Mean:       {stats['mean']:.3f} mM")
        print(f"    - Median:     {stats['median']:.3f} mM")
        print(f"    - Std Dev:    {stats['std_dev']:.3f} mM")
        
    except ValueError as e:
        print(f"[!] Error calculating statistics: {e}")

    # 3. Generate a visualization
    output_file = "kinetics_plot.png"
    print(f"\n[*] Generating visualization: Time vs. Concentration...")
    
    try:
        # Create the scatter plot
        analyzer.generate_plot(
            x_col="time_minutes",
            y_col=target_metric,
            output_filename=output_file
        )
        
        # Verify if the file was successfully created on the system
        if os.path.exists(output_file):
            print(f"    -> Success! Plot saved locally as '{output_file}'.")
        else:
            print("    -> Warning: Plot file was not created.")
            
    except KeyError as e:
        print(f"[!] Error generating plot. Missing data column: {e}")
        
    print("\n--- Analysis Complete ---")

if __name__ == "__main__":
    main()