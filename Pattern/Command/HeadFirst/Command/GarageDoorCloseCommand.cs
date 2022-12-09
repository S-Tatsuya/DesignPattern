using Entities;

namespace Command
{
    public class GarageDoorCloseCommand : ICommand
    {
        GarageDoor _garageDoor;

        public GarageDoorCloseCommand(GarageDoor garageDoor)
        {
            _garageDoor = garageDoor;
        }

        public void execute()
        {
            _garageDoor.down();
        }
    }
}
