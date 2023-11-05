from pydantic import BaseModel, Field, validator


class HotkeyModel(BaseModel):
    hotkey: str = Field(..., alias="_ParseableHotkey")

    @validator("hotkey", pre=True, allow_reuse=True)
    def validate_hotkey(cls, value):
        # Define your hotkey validation logic here
        if not isinstance(value, str):
            raise ValueError("Hotkey must be a string")

        keys = value.split("+")
        if len(keys) < 2:
            raise ValueError("Invalid hotkey format. Must be like 'Ctrl+Alt+Del'")

        # Additional validation logic can be added
        return value
