using Entities;

namespace Command
{
    public class StereoOnWithCDCommand : ICommand
    {
        Stereo _stereo;
        
        public StereoOnWithCDCommand(Stereo stereo)
        {
            _stereo = stereo;
        }

        public void execute()
        {
            _stereo.on();
            _stereo.setCd();
            _stereo.setVolume();
        }
    }
    
}
