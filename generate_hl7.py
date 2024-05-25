
import hl7
import json

def create_hl7_message(patient_info):
    # Create HL7 message
    message = hl7.Message()
    
    # MSH Segment
    msh = hl7.Segment("MSH")
    msh.append(["MSH", "|", "^", "sending_app", "sending_facility", "receiving_app", "receiving_facility", "202401010101", "", "ADT^A01", "12345", "P", "2.3"])
    message.append(msh)
    
    # PID Segment
    pid = hl7.Segment("PID")
    pid.append(["PID", "1", patient_info["patient_id"], "", f"{patient_info['last_name']}^{patient_info['first_name']}", "", patient_info["dob"], patient_info["gender"], "", patient_info["address"], "", "", "", "", "", "", "", patient_info["marital_status"]])
    message.append(pid)
    
    return message

def save_hl7_message(message, filename):
    with open(filename, "w") as file:
        file.write(str(message))

def load_patient_info(filename):
    with open(filename, "r") as file:
        return json.load(file)

if __name__ == "__main__":
    patient_info_file = "patient_info.json"
    hl7_output_file = "output.hl7"
    
    # Load patient information from JSON file
    patient_info = load_patient_info(patient_info_file)
    
    # Create HL7 message
    hl7_message = create_hl7_message(patient_info)
    
    # Save HL7 message to a file
    save_hl7_message(hl7_message, hl7_output_file)
    
    print(f"HL7 message saved to {hl7_output_file}")
