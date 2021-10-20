from pathlib import Path
""" Sound Loader houses the paths for all the sound files """

class Sound_Loader:
    def __init__(self):
        self.root = Path(__file__).parent
        self.map_path = self.root / "sounds" 
        self.attic_heart_beat_screams = self.root /"sounds"/"Attic_Heart_Beat_Screams.mp3"
        self.attic_screams_1 = self.root /"sounds"/"Attic_Scream_1.mp3"
        self.attic_screams_2 = self.root /"sounds"/"Attic_Scream_2.mp3"
        self.attic_screams_3 = self.root /"sounds"/"Attic_Scream_3.mp3"
        self.Backward_Souls = self.root /"sounds"/"Backwards_Souls-SoundBible.com-87826574.mp3"
        self.Ballroom_guests = self.root /"sounds"/"Ballroom_Guests.mp3"
        self.chains = self.root /"sounds"/"Chains_Rattling-SoundBible.com-1923614227.mp3"
        self.creaking_door = self.root /"sounds"/"Creaking_Door_Spooky-SoundBible.com-1909842345.mp3"
        self.evil_laugh = self.root /"sounds"/"Evil_Laugh_Cackle-SoundBible.com-957382653.mp3"
        self.footsteps_on_cement = self.root /"sounds"/"Footsteps_on_Cement-Tim_Fryer-870410055.mp3"
        self.footsteps_on_trail = self.root /"sounds"/"Hiking_A_Trail-SoundBible.com-589916437.mp3"
        self.hall_clock = self.root /"sounds"/"Hall_Clock.mp3"
        self.heart_beat = self.root /"sounds"/"Heart_Beat.mp3"
        self.scary = self.root /"sounds"/"Scary-Titus_Calen-1449371204.mp3"
        self.thunder = self.root /"sounds"/"Portrait_Hall_Thunder.mp3"
        self.witch = self.root /"sounds"/"Maniacal_Witches_Laugh-SoundBible.com-262127569.mp3"
        self.zombie = self.root /"sounds"/"Mummy_Zombie-SoundBible.com-1966938763.mp3"


    def get_map_name(self):
        return self.map_path

    def get_attic_heart_beat_path(self):
        return self.attic_heart_beat_screams

    def get_attic_screams_1_path(self): 
            return self.attic_screams_1

    def get_attic_screams_2_path(self): 
        return self.attic_screams_2

    def get_attic_screams_3_path(self): 
        return self.attic_screams_3

    def get_Backward_Souls_path(self):
        return self.Backward_Souls
    
    def get_ballroom_guests_path(self):
        return self.ballroom_guests

    def get_chains_path(self): 
            return self.chains

    def get_creaking_door_path(self): 
        return self.creaking_door

    def get_evil_laugh_path(self): 
        return self.evil_laugh

    def get_footsteps_on_cement_path(self):
        return self.footsteps_on_cement

    def get_footsteps_on_trail_path(self):
        return self.footsteps_on_trail

    def get_hall_clock_path(self): 
            return self.hall_clock

    def get_heart_beat_path(self):
        return self.heart_beat            

    def get_scary_path(self): 
        return self.scary

    def get_thunder_path(self): 
        return self.get_thunder

    def get_witch_path(self): 
            return self.witch

    def get_zombie_path(self): 
        return self.zombie
        
     
 
