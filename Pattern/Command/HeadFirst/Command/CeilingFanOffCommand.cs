using Entities;

namespace Command
{
    public class CeilingFanOffCommand : ICommand
    {
        CeilingFan _ceilingFan;
        int _prevSpeed;

        public CeilingFanOffCommand(CeilingFan ceilingFan)
        {
            _ceilingFan = ceilingFan;
        }

        public void execute()
        {
            _prevSpeed = _ceilingFan.Speed;
            _ceilingFan.off();
        }

        public void undo()
        {
            if (_prevSpeed == CeilingFan.HIGH)
            {
                _ceilingFan.high();
            }
            else if (_prevSpeed == CeilingFan.MEDIUM)
            {
                _ceilingFan.medium();
            }
            else if (_prevSpeed == CeilingFan.LOW)
            {
                _ceilingFan.low();
            }
            else if (_prevSpeed == CeilingFan.OFF)
            {
                _ceilingFan.off();
            }
        }
    }
}
