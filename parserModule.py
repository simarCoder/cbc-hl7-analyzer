
from datetime import datetime



def safe_get(lst, idx):
    """Helper to get list item safely without crashing."""
    return lst[idx] if idx < len(lst) else ""


def parse_hl7_date(dateStr):
    """Converts HL7 date string (YYYYMMDDHHMMSS) to YYYY-MM-DD HH:MM:SS"""
    if not dateStr or len(dateStr) < 8:
        return ""
    try:
        # HL7 format is usually YYYYMMDDHHMMSS...
        # We slice the first 14 chars
        clean_str = dateStr[:14].ljust(14, )
        # Pad with zeros if seconds/minutes missing
        clean_str = clean_str.ljust(14, '0') 
        dt = datetime.strptime(clean_str, "%Y%m%d%H%M")
        return dt.strftime("%Y-%m-%d / %H:%M")
    except ValueError:
        return dateStr
    


def normalize_results(results):
    normalized = {}
    for item in results:
        key = item["test"]
        if not key:
            continue
        normalized[key] = {
            "value": item["value"],
            "unit": item["unit"],
            "range": item["range"],
            "flag": item["flag"],
            "type": item.get("type", "NM")
        }
    return normalized

def build_section(data, params):
    section = {}
    for p in params:
        default_obj = {"value": "", "unit": "", "range": "", "flag": ""}
        section[p] = data.get(p, default_obj)
    return section

def parse_hl7_data(raw_data):
    segments = raw_data.strip().splitlines()
    pidID = ""
    obrID = ""


    parsed_data = {
        "patientName": "Unknown",
        "patientID": "",  # <--- Placeholder for ID
        "results": [],
        "images" : {}, #dictionary to store images data separatly

        "regDate": "",
        "sampleTestDate" : "",
        "reportPrintDate" : "",
        "sampleType" : "Whole Blood"
    }
    parsed_data["regDate"] = datetime.now().strftime("%Y-%m-%d/%H:%M")

    for segment in segments:
        if not segment.strip(): continue

        fields = segment.split("|")
        segment_id = fields[0]
        if segment_id == "MSH":
            mshDate = safe_get(fields, 6)
            parsed_data["reportPrintDate"] = parse_hl7_date(mshDate)

        elif segment_id == "PID":
            # --- 1. EXTRACT PATIENT NAME ---
            name_field = safe_get(fields, 5)
            parts = [p.strip() for p in name_field.split("^") if p.strip()]
            parsed_data["patientName"] = " ".join(parts)

            # --- 2. EXTRACT PATIENT ID (PID) ---
            # Standard HL7 puts the ID at index 3. 
            # Sometimes index 2 is used as an alternative ID.
            pid_val = safe_get(fields, 3).strip()
            if not pid_val:
                pid_val = safe_get(fields, 2).strip() # Fallback if index 3 is empty
            pidID = pid_val.split("^")[0]
            # Clean up caret symbols if they exist (e.g., 123^4^5 -> 123)
            # parsed_data["patientID"] = pid_val.split("^")[0]

        elif segment_id == "OBR":
            #filler order number (Index 3) first
            obrVal3 = safe_get(fields, 3).strip()
            obrVal2 = safe_get(fields, 2).strip()

            obrdate = safe_get(fields, 7)
            parsed_data["sampleTestDate"] = parse_hl7_date(obrdate)
            
            if parsed_data["sampleTestDate"]:
                parsed_data["regDate"] = parsed_data["sampleTestDate"]
            else:
                pass

            if obrVal3:
                obrID = obrVal3.split("^")[0]
            elif obrVal2:
                obrID = obrVal2.split("^")[0] 

        elif segment_id == "OBX":
            value_type = safe_get(fields, 2)
            test_id_full = safe_get(fields, 3)
            value = safe_get(fields, 5)
            unit = safe_get(fields, 6)
            ref_range = safe_get(fields, 7)
            flag = safe_get(fields, 8)

            id_parts = (test_id_full.split("^") + ["", "", ""])[:3]
            code, name, system = id_parts

            if value_type == "ED":
                components = value.split("^")
                if len(components) >= 5 and components[3] == "Base64" :
                    base64Data = components[4]
                    parsed_data["images"][name] = base64Data
                    value = "[Image Captured]" # Placeholder for text display
                else:
                    value = "[Invalid Image Data]"

            parsed_data["results"].append({
                "test": name, 
                "value": value,
                "unit": unit,
                "range": ref_range,
                "flag": flag
            })

    if obrID:
        parsed_data["patientID"] = obrID
    elif pidID:
        parsed_data["patientID"] = pidID
    else:
        parsed_data["patientID"] = "Unknown"

    # --- CONSTRUCT FINAL MODEL ---
    normalized = normalize_results(parsed_data["results"])

    wbc_params = ["WBC", "NEU%", "LYM%", "MON%", "EOS%", "BAS%"]
    wbc_abs_params = ["NEU#", "LYM#", "MON#", "EOS#", "BAS#", "ALY#", "LIC#", "NRBC#"]
    wbc_per_extra = ["ALY%", "LIC%", "NRBC%"]
    rbc_params = ["RBC", "HGB", "HCT", "MCV", "MCH", "MCHC", "RDW-CV", "RDW-SD"]
    plt_params = ["PLT", "MPV", "PDW-CV", "PDW-SD", "PCT", "P-LCR", "P-LCC"]

    # Extract Age
    age_obj = normalized.get("Age", {"value": "", "unit": ""})
    final_age_string = f"{age_obj['value']} {age_obj['unit']}".strip()

    final_model = {
        "PATIENT": parsed_data["patientName"],
        "PATIENT_ID": parsed_data["patientID"], # <--- NEW FIELD
        "AGE": final_age_string,

        "REG_DATE": parsed_data["regDate"],
        "SAMPLE_DATE": parsed_data["sampleTestDate"],
        "REPORT_DATE": parsed_data["reportPrintDate"],
        "SAMPLE_TYPE": parsed_data["sampleType"],

        "WBC": build_section(normalized, wbc_params),
        "WBC_ABSOLUTE": build_section(normalized, wbc_abs_params),
        "WBC_EXTRA": build_section(normalized, wbc_per_extra),
        "RBC": build_section(normalized, rbc_params),
        "PLATELET": build_section(normalized, plt_params),
        "IMAGES" : parsed_data["images"] #pass the images dictionary
    }

    return final_model


# print(parse_hl7_data(final_model))
