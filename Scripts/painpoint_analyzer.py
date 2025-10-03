import csv


def analyze_pain_points(csv_file_path):
    """
    Analyze common pain points across companies in the dataset.

    Args:
        csv_file_path (str): Path to the CSV file

    Returns:
        dict: Pain point analysis results
    """
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            companies = list(reader)
    except FileNotFoundError:
        print(f"Error: File {csv_file_path} not found.")
        return {}

    pain_categories = {
        'Competition Pressure': 0,
        'Compliance & Regulations': 0,
        'Data Accuracy & Quality': 0,
        'Technical Complexity': 0,
        'Scalability & Performance': 0,
        'Customer/User Adoption': 0,
        'Integration Challenges': 0,
        'Privacy & Security': 0,
        'Sales Cycles': 0
    }

    for company in companies:
        pains = company['pain_points'].lower()

        # Categorize pain points
        if any(word in pains for word in ['competing', 'competition', 'market']):
            pain_categories['Competition Pressure'] += 1
        if any(word in pains for word in ['compliance', 'regulatory', 'legal']):
            pain_categories['Compliance & Regulations'] += 1
        if any(word in pains for word in ['accuracy', 'data quality', 'validation']):
            pain_categories['Data Accuracy & Quality'] += 1
        if any(word in pains for word in ['complexity', 'complicated', 'workflow']):
            pain_categories['Technical Complexity'] += 1
        if any(word in pains for word in ['scaling', 'scale', 'performance']):
            pain_categories['Scalability & Performance'] += 1
        if any(word in pains for word in ['adoption', 'onboarding', 'user retention']):
            pain_categories['Customer/User Adoption'] += 1
        if any(word in pains for word in ['integration', 'connecting', 'api']):
            pain_categories['Integration Challenges'] += 1
        if any(word in pains for word in ['privacy', 'security', 'compliance']):
            pain_categories['Privacy & Security'] += 1
        if any(word in pains for word in ['sales cycles', 'enterprise sales']):
            pain_categories['Sales Cycles'] += 1

    # Display results
    print("\n" + "="*50)
    print("PAIN POINT ANALYSIS RESULTS")
    print("="*50)

    total_companies = len(companies)
    for pain, count in sorted(pain_categories.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            percentage = (count / total_companies) * 100
            print(
                f"• {pain}: {count}/{total_companies} companies ({percentage:.1f}%)")

    return pain_categories


if __name__ == "__main__":
    # Example usage
    results = analyze_pain_points('../sample_data/sample_companies.csv')
