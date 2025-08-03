STANDARD_COLUMNS = [
    "Relationship", 
    "Last Name", 
    "First Name", 
    "Birth Date", 
    "Hire Date", 
    "Gender", 
    "Employee Zip", 
    "Plan", 
    "Tier", 
    "Eligibility"
]

KEYWORD_MAP = { 
    "relationship": "Relationship", 
    "first name": "First Name", 
    "last name": "Last Name", 
    "last_name": "Last Name", 
    "first_name": "First Name", 
    "date_of_birth": "Birth Date",
    "zip_code": "Zip Code",
    "dob": "Birth Date", 
    "birth": "Birth Date", 
    "hire": "Hire Date", 
    "doh":"Hire Date",
    "gender": "Gender", 
    "sex": "Gender", 
    "zip": "Employee Zip", 
    "product": "Plan", 
    "medical plan": "Plan", 
    "medical tier": "Tier", 
    "medical coverage": "Tier",
    "plan": "Plan", 
    "coverage tier": "Tier", 
    "coveragetier" : "Tier", 
    "medical 1 coverage": "Tier", 
    "tier": "Tier", 
    "first": "First Name", 
    "last": "Last Name", 
    "coverage": "Tier"

}

RELATIONSHIP_MAP = {
    "ee": "Employee", 
    "es": "Spouse",  
    "sp": "Spouse",
    "ch": "Child", 
    "employee": "Employee", 
    "spouse": "Spouse", 
    "child": "Child", 
    "dep. child": "Child", 
    "dep child": "Child", 
    "dependent child": "Child", 
    "dependent spouse": "Spouse", 
    "full time": "Employee", 
    "emp": "Employee"
}

TIER_MAP = { 
    "eo" : "EE",
    "es": "ES", 
    "e+s": "ES", 
    "esp": "ES",
    "ec": "EC",
    "e+c": "EC",
    "ech": "EC", 
    "ef": "EF", 
    "fam": "EF", 
    "waived": "WAIVED", 
    "employee + children": "EC",
    "employee + child(ren)" : "EC",
    "employee + family": "EF", 
    "employee + spouse": "ES",
    "ee & sp": "ES", 
    "valid waiver": "WAIVED", 
    "waive": "WAIVED"

}