
# HL7 Message Generator

This project provides a simple Python script to generate HL7 messages. HL7 (Health Level 7) is a set of international standards for the exchange, integration, sharing, and retrieval of electronic health information.

## Files

1. **generate_hl7.py**: The main Python script to generate HL7 messages.
2. **patient_info.json**: A sample JSON file containing patient information.

## Requirements

- Python 3.x
- hl7 library (You can install it using `pip install hl7`)

## Usage

1. **Install the HL7 library**:
    ```bash
    pip install hl7
    ```

2. **Prepare the patient information**:
    Modify the `patient_info.json` file with the relevant patient information.

3. **Run the script**:
    Execute the `generate_hl7.py` script to generate the HL7 message.
    ```bash
    python generate_hl7.py
    ```

4. **Output**:
    The script will generate an HL7 message and save it to `output.hl7`.

## Example

### patient_info.json
```json
{
    "patient_id": "123456",
    "first_name": "John",
    "last_name": "Doe",
    "dob": "19800101",
    "gender": "M",
    "address": "123 Main St, Anytown, USA",
    "marital_status": "S"
}
```

### generate_hl7.py
```python
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
```

### Output
The script will generate the following HL7 message and save it to `output.hl7`:

```
MSH|^~\&|sending_app|sending_facility|receiving_app|receiving_facility|202401010101||ADT^A01|12345|P|2.3
PID|1|123456||Doe^John||19800101|M||123 Main St, Anytown, USA||||||||||S
```
