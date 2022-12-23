using Entities;

namespace Command
{
    public class StereoOffCommand : ICommand
    {
        Stereo _stereo;
        public StereoOffCommand(Stereo stereo)
        {
            _stereo = stereo;
        }

        public void execute()
        {
            _stereo.off();
        }

        public void undo(){}
    }
}
