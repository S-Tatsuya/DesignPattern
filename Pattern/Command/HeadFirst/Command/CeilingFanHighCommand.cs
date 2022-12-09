using Entities;

namespace Command
{
    public class CeilingFanHighCommnad : ICommand
    {
        CeilingFan _ceilingFan;

        public CeilingFanHighCommnad(CeilingFan ceilingFan)
        {
            _ceilingFan = ceilingFan;
        }

        public void execute()
        {
            _ceilingFan.high();
        }
    }
}
