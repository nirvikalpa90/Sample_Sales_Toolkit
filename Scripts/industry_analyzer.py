import csv
from collections import Counter


def analyze_industries(csv_file_path):
    """
    Analyze industry distribution in the dataset.

    Args:
        csv_file_path (str): Path to the CSV file

    Returns:
        dict: Industry analysis results
    """
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            companies = list(reader)
    except FileNotFoundError:
        print(f"Error: File {csv_file_path} not found.")
        return {}

    # Count industries
    industries = [company['industry'] for company in companies]
    industry_counts = Counter(industries)

    # Analyze tech stacks by industry
    industry_tech = {}
    for company in companies:
        industry = company['industry']
        if industry not in industry_tech:
            industry_tech[industry] = []

        techs = [tech.strip() for tech in company['tech_stack'].split(',')]
        industry_tech[industry].extend(techs)

    print("\n" + "="*50)
    print("INDUSTRY ANALYSIS")
    print("="*50)

    print(f"\n INDUSTRY DISTRIBUTION ({len(companies)} companies):")
    print("-" * 30)

    for industry, count in industry_counts.most_common():
        percentage = (count / len(companies)) * 100
        print(f"• {industry}: {count} companies ({percentage:.1f}%)")

    print(f"\n  TOP TECHNOLOGIES BY INDUSTRY:")
    print("-" * 30)

    for industry, techs in industry_tech.items():
        tech_counts = Counter(techs)
        top_techs = tech_counts.most_common(3)
        tech_list = ", ".join(
            [f"{tech} ({count})" for tech, count in top_techs])
        print(f"• {industry}: {tech_list}")

    return {
        'industry_counts': dict(industry_counts),
        'industry_tech': {k: dict(Counter(v)) for k, v in industry_tech.items()}
    }


if __name__ == "__main__":
    # Example usage
    results = analyze_industries('../sample_data/sample_companies.csv')
