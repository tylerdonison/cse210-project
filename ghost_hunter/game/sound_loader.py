""" Sound Loader houses the paths for all the sound files. Defines the path to the sound resources """
from pathlib import Path
import arcade

class Sound_Loader:
    """The Sound_Load class declares the path to the sounds folder also gives names to all the sound clips """
    def __init__(self):
        """class constructor """
        self.root = Path(__file__).parent
        self.map_path = self.root / "sounds"
        self.attic_heart_beat_screams = self.root / \
            "sounds"/"Attic_Heart_Beat_Screams.mp3"
        self.attic_screams_1 = self.root / "sounds"/"Attic_Scream_1.mp3"
        self.attic_screams_2 = self.root / "sounds"/"Attic_Scream_2.mp3"
        self.attic_screams_3 = self.root / "sounds"/"Attic_Scream_3.mp3"
        self.Backward_Souls = self.root / "sounds" / \
            "Backwards_Souls-SoundBible.com-87826574.mp3"
        self.Ballroom_guests = self.root / "sounds"/"Ballroom_Guests.mp3"
        self.chains = self.root / "sounds"/"Chains_Rattling-SoundBible.com-1923614227.mp3"
        self.creaking_door = self.root / "sounds" / \
            "Creaking_Door_Spooky-SoundBible.com-1909842345.mp3"
        self.evil_laugh = self.root / "sounds" / \
            "Evil_Laugh_Cackle-SoundBible.com-957382653.mp3"
        self.footsteps_on_cement = self.root / "sounds" / \
            "Footsteps_on_Cement-Tim_Fryer-870410055.mp3"
        self.footsteps_on_trail = self.root / "sounds" / \
            "Hiking_A_Trail-SoundBible.com-589916437.mp3"
        self.hall_clock = self.root / "sounds"/"Hall_Clock.mp3"
        self.heart_beat = self.root / "sounds"/"Heart_Beat.mp3"
        self.scary = self.root / "sounds"/"Scary-Titus_Calen-1449371204.mp3"
        self.thunder = self.root / "sounds"/"Portrait_Hall_Thunder.mp3"
        self.witch = self.root / "sounds" / \
            "Maniacal_Witches_Laugh-SoundBible.com-262127569.mp3"
        self.zombie = self.root / "sounds"/"Mummy_Zombie-SoundBible.com-1966938763.mp3"

    def get_map_name(self):
        """Gets the selected path for the sound clip.

        Returns:
            (self) map_path: The path to clips.
        """
        return self.map_path

############################################
    def play_attic_heart_beat_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) attic_heart_beat_screams: The sound clips.
        """
        sound = arcade.load_sound(self.attic_heart_beat_screams)
        arcade.play_sound(sound)
############################################

    def play_attic_screams_1_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) attic_screams_1: The sound clips.
        """
        return self.attic_screams_1

    def play_attic_screams_2_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) attic_screams_2: The sound clips.
        """
        return self.attic_screams_2

    def play_attic_screams_3_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) attic_screams_3: The sound clips.
        """
        return self.attic_screams_3

    def play_Backward_Souls_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) Backward_Souls: The sound clips.
        """
        return self.Backward_Souls

    def play_ballroom_guests_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) ballroom_guests: The sound clips.
        """
        return self.ballroom_guests

    def play_chains_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) chains: The sound clips.
        """
        return self.chains

    def play_creaking_door_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) creaking_door: The sound clips.
        """
        return self.creaking_door

    def play_evil_laugh_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) self.evil_laugh: The sound clips.
        """
        return self.evil_laugh

################################################
    def play_footsteps_on_cement_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) footsteps_on_cement: The sound clips.
        """
        sound = arcade.load_sound(self.footsteps_on_cement)
        arcade.play_sound(sound)
################################################

    def play_footsteps_on_trail_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) footsteps_on_trail: The sound clips.
        """
        return self.footsteps_on_trail

    def play_hall_clock_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) hall_clock: The sound clips.
        """
        return self.hall_clock

    def play_heart_beat_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) heart_beat: The sound clips.
        """
        return self.heart_beat

    def play_scary_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) scary: The sound clips.
        """
        return self.scary

    def play_thunder_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) thunder: The sound clips.
        """
        return self.thunder

    def play_witch_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) witch: The sound clips.
        """
        return self.witch

    def play_zombie_path(self):
        """Gets the selected sound clip.

        Returns:
            (self) zombie: The sound clips.
        """
        return self.zombie
