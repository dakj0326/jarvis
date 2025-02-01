

class Light:
    """
    Represents a lightbulb and its data. Does not cointain
    any functionality of the light itself.
    
    Attr:
    entity_id : str
        The id for the physical light represented by this Light
    color_comp : bool
        True if the lamp is compatible with different colors
    bright_comp : bool
        True if the lamp is compatible with different brightness levels
    """
    def __init__(self, entity_id: str, color_comp: bool, bright_comp: bool):
        """
        Constructor function for Light
        Will raise errors if poorly constructed
        """
        if not isinstance(entity_id, str):
            raise TypeError("entity_id must be of type String")
        self.entity_id = entity_id
        
        if not isinstance(color_comp, bool):
            raise TypeError("color_comp must be of type bool")
        self.color_comp = color_comp
        
        if not isinstance(bright_comp, bool):
            raise TypeError("bright_comp must be of type bool")
        self.bright_comp = bright_comp
        
    def get_id(self):
        """Getter for self.entity_id"""
        return self.entity_id

    def get_color_comp(self):
        """Getter for self.color_comp"""
        return self.color_comp
    
    def get_bright_comp(self):
        """Getter for self.bright_comp"""
        return self.bright_comp




class LightAction:
    """
    Used to preform actions on a Light.
    
    Attr:
    light : Light
        The selected Light to which the action will be preformed
    state : string
        What power state the Light should assume (on or off)
    color : tuple(int, int, int)
        A tuple of three values between 0-255 representing RGB
    brightness : int
        A value between 0-100 that represents the brightness
    """
    def __init__(self, light: Light, state: str, color: tuple, brightness: int):
        """
        Constructor function for LightAction
        Will raise errors if poorly contructed
        """
        if not isinstance(light, Light):
            raise TypeError("light must be of type Light")
        self.light = light
        
        if not isinstance(state, str):
            raise TypeError("state must be of type String")
        if not (state.lower() == "on" or state.lower() == "off"):
            raise ValueError("Invalid state format")
        self.state = state
        
        if color is not None:
            if not isinstance(color, tuple):
                raise TypeError("color must be of type Tuple")
            if not len(color) == 3:
                raise ValueError("Invalid number of values in color")
            for val in color:
                if not (0 <= val <= 255):
                    raise ValueError("Invalid color value")
        self.color = color
        
        if brightness is not None:
            if not isinstance(brightness, int):
                raise TypeError("brightness must be of type Integer")
            if not 0 <= brightness <= 100:
                raise ValueError("Invalid brightness value")
        self.brightness = brightness
        
    def get_light(self):
        """Getter for self.light"""
        return self.light
    
    def get_state(self):
        """Getter for self.state"""
        return self.state
    
    def get_color(self):
        """Getter for self.color"""
        return self.color

    def get_brightness(self):
        """Getter for self.brightness"""
        return self.brightness