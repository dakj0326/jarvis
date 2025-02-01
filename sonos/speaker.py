

class Speaker:
    """
    Represents a speaker and its data. Does not cointain
    any functionality of the speaker itself.
    
    Attr:
    entity_id : str
        The id for the physical speaker represented by this Speaker
    volume : float
        Between 0-1 this float is the volume level where 1 is maximum and 0 is muted
    """
    
    def __init__(self, entity_id: str):
        """
        Constructor function for Light
        Will raise errors if poorly constructed
        """
        if not isinstance(entity_id, str):
            raise TypeError("entity_id must be of type String")
        self.entity_id = entity_id
        
        self.volume = 0.2
        
    def get_id(self):
        """Getter for self.entity_id"""
        return self.entity_id
    
    def get_volume(self):
        """Getter for self.volume"""
        return self.volume
    
    def set_volume(self, volume: int):
        """Setter for self.volume"""
        self.volume = volume
        
class SpeakerAction:
    """
    Parent class for actions to be preformed. Used to destinguish 
    different types of actions.
    
    Attr:
    speaker : Speaker
        speaker is the Speaker that the actions is applied to
    action : str
        action is the type of action that is preformed
    """
    def __init__(self, speaker: Speaker, action: str):
        """
        Constructor function for SpeakerAction
        Will raise errors if poorly contructed
        """
        if not isinstance(speaker, Speaker):
            raise TypeError("speaker must be of type Speaker")
        self.speaker = speaker
        
        if not isinstance(action, str):
            raise TypeError("action must be of type String")
        self.action = action
        
    def get_speaker(self):
        """Getter for self.speaker"""
        return self.speaker
    
    def get_action(self):
        """Getter for self.action"""
        return self.action



class SpeakerToggle(SpeakerAction):
    """
    Specific Speaker action for toggling the speaker pause and play
    Child of SpeakerAction
    
    Attr:
    speaker : Speaker
        super for SpeakerAction 
    state : str
        Defines the state of the toggle
    """
    def __init__(self, speaker: Speaker, state: str):
        super().__init__(speaker, "toggle")
        if not isinstance(state, str):
            raise TypeError("state must be of type String")
        if not (state.lower() == "play" or state.lower() == "pause"):
            raise ValueError("Invalid state format")
        self.state = state
    
    def get_state(self):
        """Getter for self.state"""
        return self.state
        
        