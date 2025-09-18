def convert_length(value, unit):
    """แปลงหน่วยความยาว - ไม่อนุญาตค่าติดลบ"""
    # ตรวจสอบค่าติดลบ
    if value < 0:
        raise ValueError("ความยาวไม่สามารถเป็นค่าติดลบได้")
    
    # แปลง input เป็น cm ก่อน
    if unit == "cm":
        cm = value
    elif unit == "m":
        cm = value * 100
    elif unit == "km":
        cm = value * 100000
    elif unit == "inch":
        cm = value * 2.54
    elif unit == "foot":
        cm = value * 30.48
    elif unit == "yard":
        cm = value * 91.44
    elif unit == "mile":
        cm = value * 160934
    else:
        cm = value  # fallback

    conversions = {
        "cm": cm,
        "m": cm / 100,
        "km": cm / 100000,
        "inch": cm / 2.54,
        "foot": cm / 30.48,
        "yard": cm / 91.44,
        "mile": cm / 160934
    }
    return conversions

def convert_weight(value, unit):
    """แปลงหน่วยน้ำหนัก - ไม่อนุญาตค่าติดลบ"""
    # ตรวจสอบค่าติดลบ
    if value < 0:
        raise ValueError("น้ำหนักไม่สามารถเป็นค่าติดลบได้")
    
    # แปลง input เป็นกรัมก่อน
    if unit == "g":
        grams = value
    elif unit == "kg":
        grams = value * 1000
    elif unit == "lb":
        grams = value * 453.592
    elif unit == "oz":
        grams = value * 28.3495
    else:
        grams = value

    conversions = {
        "g": grams,
        "kg": grams / 1000,
        "lb": grams / 453.592,
        "oz": grams / 28.3495
    }
    return conversions

def convert_temperature(value, unit):
    """แปลงหน่วยอุณหภูมิ - อนุญาตค่าติดลบ (เพราะอุณหภูมิสามารถติดลบได้)"""
    # ตรวจสอบค่าต่ำสุดของอุณหภูมิ (absolute zero)
    if unit == "K" and value < 0:
        raise ValueError("อุณหภูมิเคลวินไม่สามารถต่ำกว่า 0 K ได้")
    elif unit == "C" and value < -273.15:
        raise ValueError("อุณหภูมิเซลเซียสไม่สามารถต่ำกว่า -273.15°C ได้")
    elif unit == "F" and value < -459.67:
        raise ValueError("อุณหภูมิฟาเรนไฮต์ไม่สามารถต่ำกว่า -459.67°F ได้")
    
    if unit == "C":
        c = value
    elif unit == "F":
        c = (value - 32) * 5/9
    elif unit == "K":
        c = value - 273.15
    else:
        c = value

    conversions = {
        "C": c,
        "F": c * 9/5 + 32,
        "K": c + 273.15
    }
    return conversions