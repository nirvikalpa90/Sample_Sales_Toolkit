import csv


def find_companies_by_tech(csv_file_path, technology):
    """
    Find companies using specific technologies.

    Args:
        csv_file_path (str): Path to the CSV file
        technology (str): Technology to search for

    Returns:
        list: Companies using the specified technology
    """
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            companies = list(reader)
    except FileNotFoundError:
        print(f"Error: File {csv_file_path} not found.")
        return []

    matches = []
    for company in companies:
        if technology.lower() in company['tech_stack'].lower():
            matches.append(company)

    # Display results
    print(f"\n COMPANIES USING {technology.upper()}: {len(matches)} found")
    print("-" * 40)

    for company in matches:
        print(f"• {company['company']} ({company['industry']})")
        print(
            f"  Size: {company['size']} | Pain: {company['pain_points'][:60]}...")
        print()

    return matches


def find_companies_by_industry(csv_file_path, industry):
    """
    Find companies in specific industries.

    Args:
        csv_file_path (str): Path to the CSV file
        industry (str): Industry to filter by

    Returns:
        list: Companies in the specified industry
    """
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            companies = list(reader)
    except FileNotFoundError:
        print(f"Error: File {csv_file_path} not found.")
        return []

    matches = []
    for company in companies:
        if industry.lower() in company['industry'].lower():
            matches.append(company)

    print(f"\n COMPANIES IN {industry.upper()}: {len(matches)} found")
    print("-" * 40)

    for company in matches:
        print(f"• {company['company']}")
        print(f"  Tech: {company['tech_stack']}")
        print(f"  Contact: {company['contact_email']}")
        print()

    return matches


if __name__ == "__main__":
    # Example usage
    print("Testing Lead Filter...")
    aws_companies = find_companies_by_tech(
        '../sample_data/sample_companies.csv', 'AWS')
    saas_companies = find_companies_by_industry(
        '../sample_data/sample_companies.csv', 'SaaS')
