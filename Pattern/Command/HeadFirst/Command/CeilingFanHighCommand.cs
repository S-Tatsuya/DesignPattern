using Entities;

namespace Command
{
    public class CeilingFanHighCommnad : ICommand
    {
        CeilingFan _ceilingFan;
        int _prevSpeed;

        public CeilingFanHighCommnad(CeilingFan ceilingFan)
        {
            _ceilingFan = ceilingFan;
        }

        public void execute()
        {
            _prevSpeed = _ceilingFan.Speed;
            _ceilingFan.high();
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
