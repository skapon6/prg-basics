def time_string(hours, minutes, time_format):
    if time_format == "24":
        return f"{hours}:{minutes}"
    else:
        return f"{hours%12}:{minutes}am"
    
    
print(time_string(13,10,"12"))