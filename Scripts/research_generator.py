import csv


def generate_research_report(csv_file_path, company_name):
    """
    Generate a pre-call research report for a specific company.

    Args:
        csv_file_path (str): Path to the CSV file
        company_name (str): Company to research

    Returns:
        dict: Company research data
    """
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            companies = list(reader)
    except FileNotFoundError:
        print(f"Error: File {csv_file_path} not found.")
        return {}

    for company in companies:
        if company_name.lower() in company['company'].lower():
            print("\n" + "="*60)
            print(f" PRE-CALL RESEARCH: {company['company'].upper()}")
            print("="*60)
            print(f" Industry: {company['industry']}")
            print(f" Company Size: {company['size']} employees")
            print(f"  Tech Stack: {company['tech_stack']}")
            print(f" Pain Points: {company['pain_points']}")
            print(
                f" Contact: {company['contact_name']} | {company['contact_email']}")
            print(f" Source: {company['source']}")
            print("="*60)
            return company

    print(f"Company '{company_name}' not found in database.")
    return {}


def list_all_companies(csv_file_path):
    """
    List all companies in the database.

    Args:
        csv_file_path (str): Path to the CSV file

    Returns:
        list: All companies
    """
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            companies = list(reader)
    except FileNotFoundError:
        print(f"Error: File {csv_file_path} not found.")
        return []

    print(f"\n ALL COMPANIES IN DATABASE ({len(companies)} total)")
    print("-" * 40)

    for i, company in enumerate(companies, 1):
        print(f"{i}. {company['company']} - {company['industry']}")

    return companies


if __name__ == "__main__":
    # Example usage
    print("Testing Research Generator...")
    list_all_companies('../sample_data/sample_companies.csv')
    print("\n")
    generate_research_report(
        '../sample_data/sample_companies.csv', 'CloudTech')
