using Entities;

namespace Command
{
    public class CeilingFanOffCommand : ICommand
    {
        CeilingFan _ceilingFan;

        public CeilingFanOffCommand(CeilingFan ceilingFan)
        {
            _ceilingFan = ceilingFan;
        }

        public void execute()
        {
            _ceilingFan.off();
        }
    }
}
