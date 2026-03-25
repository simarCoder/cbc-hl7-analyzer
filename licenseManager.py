import base64
from datetime import datetime
import os

class LicenseManager:
    def __init__(self, filepath = "license.dat"):
        self.filepath = filepath
        self.minValidDate = datetime(2025, 1, 1)

    def encode_(self, dateStr):
        """Obscures the date string so it isnt human readable, and it remains safe."""
        #simple Base64 encoding
        #for real security we will use encryption(Fernet/AES), but this stops casula editing and changing the date becomes tough
        return base64.b64encode(dateStr.encode()).decode()
    
    def decode_(self, encodedStr):
        """Decodes the obscured string back to a date"""
        try:
            return base64.b64decode(encodedStr.encode()).decode()
        except:
            return self.defaultDate
        

    def validate(self):
        """Checks the specific state of the license.
        Returns one of: "valid", "missing", "clock error", "expired", "corrupted"
        """
        #--- Check System Clock (Time Travel)
        if datetime.now()< self.minValidDate:
            return "CLOCK_ERROR"
        if not os.path.exists(self.filepath):
            return "MISSING"
        try:
            with open(self.filepath, "r") as f:
                encoded = f.read().strip()
                dateStr = self.decode_(encoded)
                
                if not dateStr:
                    return "CORRUPT"
                
                expiryDate = datetime.strptime(dateStr, "%Y-%m-%d")

                if datetime.now() > expiryDate:
                    return "EXPIRED"
                
                return "VALID"
        except Exception:
            return "CORRUPT"
        
    def getExpiryDate(self):
        """Reads the file and returns the datetime object."""
        if not os.path.exists(self.filepath):
            #creates a default file if missing(eg, 1 year trial or expired)
            #you might want to defualt to yesterday
            return "Not Found"
        try:
            with open(self.filepath, "r") as f:
                return self.decode_(f.read().strip())
        except:
            return "Error"
        
    def updateLicense(self, newDateStr):
        """ Saves a new date"""
        with open(self.filepath, "w") as f:
            encoded = self.encode_(newDateStr)
            f.write(encoded)

        print(f"LICENSE UPDATED TO {newDateStr}")
        
        