import pandas as pd
def show_dictionary(df):
    
    feature_descriptions = {
        'sex': "Sex of the respondent",
        'age1115': "Age group (11-15)",
        'ethnicgp5': "Ethnicity categorized into 5 groups",
        'region': "Region of residence (geographical context)",
        'cgpppar': "Whether parents/guardians of the respondent smoke",
        'cgppfrsa': "Whether friends of the respondent smoke",
        'cgfamn': "Family attitudes towards smoking (non-smokers)",
        'cgfams': "Family attitudes towards smoking (smokers)",
        'cgwhypre': "Belief that peers smoke due to peer pressure",
        'cgwhyadd': "Belief that peers smoke because of addiction",
        'cgwhyrel': "Belief that peers smoke to relax",
        'cgwhystr': "Belief that peers smoke to cope with stress",
        'cgwhygdf': "Belief that peers smoke because it gives them a good feeling",
        'cgwhycoo': "Belief that peers smoke to look cool",
        'okcg1': "Whether respondent thinks it is okay to try smoking to see what it is like",
        'okcgw': "Whether respondent thinks it is okay to smoke once a week",
        'cgshin': "Exposure to secondhand smoke in homes",
        'cgshcar': "Exposure to secondhand smoke in cars",
        'cgwhohme': "Whether people smoke inside the home of the respondent",
        'einfsmk': "Whether school provided enough information on smoking",
        'dlssmk': "Whether respondent had lessons on smoking in the last 12 months",
        'dcgevr': "Has ever smoked"
    }
    
    # Define your feature groups
    demographics_cols = ['sex', 'age1115', 'ethnicgp5']
    family_cols = ['cgpppar', 'cgppfrsa', 'cgfamn', 'cgfams']
    attitude_cols = ['dcgevr','cgwhypre', 'cgwhyadd', 'cgwhyrel', 'cgwhystr', 'cgwhygdf', 'cgwhycoo', 'okcg1', 'okcgw']
    exposure_cols = ['cgshin', 'cgshcar', 'cgwhohme']
    education_cols = ['einfsmk', 'dlssmk']
    
    # Map each feature to its subsection
    subsection_mapping = {col: 'Demographics' for col in demographics_cols}
    subsection_mapping.update({col: 'Family attitude' for col in family_cols})
    subsection_mapping.update({col: 'Personal attitudes' for col in attitude_cols})
    subsection_mapping.update({col: 'Exposure' for col in exposure_cols})
    subsection_mapping.update({col: 'Education' for col in education_cols})
    
    # Extract variable information
    variable_info = []
    for col in demographics_cols + family_cols + attitude_cols + exposure_cols + education_cols:
        dtype = str(df[col].dtype) 
        variable_info.append([subsection_mapping[col], col, feature_descriptions[col], dtype])
    
    # Create a DataFrame
    dictionary_table = pd.DataFrame(
        variable_info,
        columns=['Subsection', 'Variable Name', 'Description', 'Data Type']
    )
    
    dictionary_table.loc[dictionary_table['Subsection'].duplicated(), 'Subsection'] = ''
    dictionary_table = dictionary_table[['Subsection', 'Variable Name', 'Description', 'Data Type']]
    
    # Apply styling for left alignment
    styled_table = dictionary_table.style.set_properties(**{
        'text-align': 'left'  # Align text to the left
    }).set_table_styles([
        {'selector': 'th', 'props': [('text-align', 'left')]}  # Align headers to the left
    ])
    
    # Display the styled table
    display(styled_table)