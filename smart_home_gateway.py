from datetime import datetime


class SmartDevice:
    """Base device model for IoT sensors and actuators."""

    def __init__(self, device_id: str, device_type: str):
        self.device_id = device_id
        self.device_type = device_type
        self.is_active = False

    def toggle_power(self, state: bool):
        self.is_active = state


class SecurityDoorLock(SmartDevice):
    """Encapsulates biometric and keycode door lock hardware logic."""

    def __init__(self, device_id: str, master_code: str):
        super().__init__(device_id, "DOOR_LOCK")
        self._master_code = master_code
        self.is_locked = True

    def unlock(self, passcode: str) -> bool:
        """Unlocks the door mechanism if the provided code matches the master key."""
        if passcode == self._master_code:
            self.is_locked = False
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ACCESS GRANTED: Lock {self.device_id} opened.")
            return True
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ACCESS DENIED: Invalid keycode on {self.device_id}.")
        return False

    def lock(self):
        self.is_locked = True
        print(f"[{datetime.now().strftime('%H:%M:%S')}] LOCK ENGAGED: Lock {self.device_id} secured.")


# Demonstration Run
if __name__ == "__main__":
    print("=== SMART HOME GATEWAY DEMO ===")
    front_door = SecurityDoorLock("LOCK-MAIN-01", "8831")
    
    # Access Attempts
    front_door.unlock("0000")  # Invalid
    front_door.unlock("8831")  # Valid
    front_door.lock()
