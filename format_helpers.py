from config import RELATIONSHIP_MAP, TIER_MAP


def fix_relationship(extracted_cols):

    def correct_relationship_value(value):
        if not isinstance(value, str):
            return "Other"
        
        value = value.strip().lower()

        for keyword, label in RELATIONSHIP_MAP.items():
            if keyword in value: 
                return label
        
        return value
    
    extracted_cols["Relationship"] = extracted_cols["Relationship"].apply(correct_relationship_value)
    return extracted_cols


def fix_tier(extracted_cols):

    def correct_tier_value(value):
            if not isinstance(value, str):
                return ""
     
        
            value = value.strip().lower()

            for keyword, label in TIER_MAP.items():

                if value == "employee": 
                    return "EE"
                
                if keyword in value: 
                    return label
            
            return value
    
    extracted_cols["Tier"] = extracted_cols["Tier"].apply(correct_tier_value)
    return extracted_cols







