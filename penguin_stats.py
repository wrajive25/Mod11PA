
# penguin_stats.py
# Rajive Williams
# 11/23/2026
# Functions for calculating and classifying penguin statistics

#Function to calcuate species percentages
def calculate_percentage(count, total):
    return (count/total) * 100

#Function to classify species
def classify_species(species_percentages):
    if species_percentages < 25:
       category = "small"
    elif (species_percentages >= 25) and (species_percentages < 40):
       category = "medium"
    else:
       category = "large"
    return category

#Function to determine position
def get_position_description(selected_species, largest_species,
                             smallest_species):
    if (selected_species == largest_species):
        size = "largest"
    elif (selected_species == smallest_species):
        size = "smallest"
    else:
        size = "middle-sized"
    return size

