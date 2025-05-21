from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Optional, Dict, Annotated

class Address(BaseModel):
    base: str
    city: str
    state: str
    pincode : int

class Patient(BaseModel):
    name : Annotated[str, Field(max_length=50, title="Name of the patient", description="Full name of the patient", examples=["Manasi Gunjal", "Bhushan Gunjal"])]
    email : EmailStr
    linkedin_url : AnyUrl
    address : Address
    age : int = Field(gt = 0) 
    height : Annotated[float, Field(gt = 0, strict=True)]
    married : Annotated[bool, Field(title="Marital Status", description="True if married, False otherwise", default=False)]
    allergies : Annotated[Optional[List[str]], Field(max_length=5)]
    contact : Dict[str, str]

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_list = ["hdfcbank.com", "kotakbank.com"]
        domain = value.split("@")[-1]
        if domain not in valid_list:
            raise ValueError("Email domain must be either hdfcbank.com or kotakbank.com")
        return value

    
    @field_validator("name")
    @classmethod
    def upper_case(cls, value):
        return value.upper()
    

    @model_validator(mode="after")
    def check_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact.keys():
            raise ValueError("Emergency contact is required for patients above 60 years of age.")
        else:
            return model


    @computed_field
    @property
    def name_check(self) -> str:
        if self.name == "BHUSHAN GUNJAL":
            return "bhu"
        else:
            return "not bhu"
    

address_dict = {
    "base": "Megh Malhar Society",
    "city": "Navi Mumbai",
    "state": "Maharashtra",
    "pincode": 400701
}


patient_info = {
    "name"          : "Bhushan Gunjal", 
    "email"         : "gunjalbhushan68@hdfcbank.com",
    "linkedin_url"  : "https://www.linkedin/in/bhushangunjal/",
    "address"       : address_dict,
    "age"           : 60,
    "height"        : 5.8,
    "married"       : True,
    "allergies"     : ["Peanuts", "Dust"],
    "contact"       : {
        "email"     : "gunjalbhushan68@gmail.com",
        "phone"     : "8104126120",
        "emergency" : "9820915277"
    }
}

patient1 = Patient(**patient_info)

def insert_patient_details_pydantic(patient: Patient):
    print()
    print("NAME:        ",patient.name)
    print("CHK:         ",patient.name_check)
    print("Pincode:     ",patient.address.pincode)
    print("EMAIL:       ",patient.email)
    print("LINKEDIN:    ",patient.linkedin_url)
    print("AGE:         ",patient.age)
    print("HEIGHT:      ",patient.height)
    print("MARRIED:     ",patient.married)
    print("ALLERGIES:   ",patient.allergies)
    print("CONTACT:     ",patient.contact)
    print("Patient details inserted successfully.")
    print()

insert_patient_details_pydantic(patient1)