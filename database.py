import sqlite3
import json
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_name="cbc_records.db"):
        self.db_name = db_name
        self.init_db() # Ensure tables exist on startup

    def connect(self):
        return sqlite3.connect(self.db_name)

    def _get_table_name(self, date_obj):
        return f"records_{date_obj.strftime('%Y_%m')}"

    def _ensure_table_exists(self, table_name):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT,
                patient_pid TEXT,
                test_date TIMESTAMP,
                json_data TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def init_db(self):
        """Creates the doctors table if it doesn't exist."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS doctors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE
            )
        ''')
        # Insert 'SELF' if table is empty
        cursor.execute("SELECT count(*) FROM doctors")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO doctors (name) VALUES ('SELF')")
        
        conn.commit()
        conn.close()

    def get_all_doctors(self):
        """Returns a list of all doctor names sorted alphabetically."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM doctors ORDER BY name ASC")
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def add_doctor(self, name):
        """Adds a new doctor if they don't exist. Returns True if added."""
        name = name.strip().upper()
        if not name: return False
        
        conn = self.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO doctors (name) VALUES (?)", (name,))
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            conn.close()
            return False # Already exists

    def add_record(self, data_dict):
        """Saves new data. Returns (new_id, table_name, timestamp)"""
        now = datetime.now()
        table_name = self._get_table_name(now)
        self._ensure_table_exists(table_name)

        conn = self.connect()
        cursor = conn.cursor()
        
        p_name = data_dict.get("PATIENT", "Unknown")
        p_id = data_dict.get("PATIENT_ID", "")
        json_str = json.dumps(data_dict, default=str)
        
        cursor.execute(f'''
            INSERT INTO {table_name} (patient_name, patient_pid, test_date, json_data)
            VALUES (?, ?, ?, ?)
        ''', (p_name, p_id, now, json_str))
        
        new_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return new_id, table_name, now

    def update_record(self, record_id, table_name, data_dict):
        conn = self.connect()
        cursor = conn.cursor()
        
        p_name = data_dict.get("PATIENT", "Unknown")
        p_id = data_dict.get("PATIENT_ID", "")
        json_str = json.dumps(data_dict)
        
        try:
            cursor.execute(f'''
                UPDATE {table_name} 
                SET patient_name = ?, patient_pid = ?, json_data = ?
                WHERE id = ?
            ''', (p_name, p_id, json_str, record_id))
            conn.commit()
        except Exception as e:
            print(f"Update failed: {e}")
        finally:
            conn.close()

    def get_record(self, record_id, table_name):
        conn = self.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT json_data, test_date FROM {table_name} WHERE id = ?", (record_id,))
            row = cursor.fetchone()
        except sqlite3.OperationalError:
            return None, None
        finally:
            conn.close()
        
        if row:
            return json.loads(row[0]), row[1]
        return None, None

    def get_prev_id(self, current_id, table_name):
        conn = self.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT id FROM {table_name} WHERE id < ? ORDER BY id DESC LIMIT 1", (current_id,))
            row = cursor.fetchone()
            return row[0] if row else None
        except: return None
        finally: conn.close()

    def get_next_id(self, current_id, table_name):
        conn = self.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT id FROM {table_name} WHERE id > ? ORDER BY id ASC LIMIT 1", (current_id,))
            row = cursor.fetchone()
            return row[0] if row else None
        except: return None
        finally: conn.close()

    def get_last_id_in_month(self, date_obj):
        table_name = self._get_table_name(date_obj)
        conn = self.connect()
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT id FROM {table_name} ORDER BY id DESC LIMIT 1")
            row = cursor.fetchone()
            return row[0] if row else None, table_name
        except sqlite3.OperationalError:
            return None, table_name
        finally:
            conn.close()