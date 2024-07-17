
class Radio:
    def seek(self):
        pass

    def tune(self, frequency):
        pass

class TuneupRadio(Radio):

    def __init__(self) -> None:
        self.frequency = None

    def seek(self):
        self.frequency = self.frequency+1 if self.frequency else "100"
        print(f"now playing radio at {self.frequency}")
        print("playing radio")

    def tune(self, frequency):
        self.frequency = frequency
        print(f"now playing radio at {self.frequency}")

class CarAudio:
    def play_sound(self, radio: Radio):
        radio.seek()

class PhonePlayer():
    def play_music(self):
        print(f"Playing music library on {type(self).__name__}")

class PhonePlayerRadioAdapter(Radio):

    def __init__(self, phone: PhonePlayer) -> None:
        self.phone = phone
        self.transmit_frequency = None

    def seek(self):
        print(f"Streaming music on {self.transmit_frequency}")
        self.phone.play_music()

    def connect_to_radio(self, radio, frequency):
        self.transmit_frequency = frequency
        radio.tune(frequency)

if __name__ == "__main__":
    phone_adapter = PhonePlayerRadioAdapter(PhonePlayer())
    car_audio = CarAudio()
    tuneup_radio = TuneupRadio()
    car_audio.play_sound(tuneup_radio)

    phone_adapter.connect_to_radio(tuneup_radio, "101")
    car_audio.play_sound(phone_adapter)
    

