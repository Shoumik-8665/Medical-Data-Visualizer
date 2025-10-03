# This entrypoint file to be used in development. Start by reading the instructions in README.md
import medical_data_visualizer

# Test your function by calling it here
print("Generating categorical plot...")
medical_data_visualizer.draw_cat_plot()
print("Categorical plot saved as 'catplot.png'")

print("\nGenerating heat map...")
medical_data_visualizer.draw_heat_map()
print("Heat map saved as 'heatmap.png'")

print("\nVisualization complete!")

# Uncomment the following lines to run unit tests if you have test_module.py
# import test_module
# test_module.run_tests()