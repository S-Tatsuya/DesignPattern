using System;
using Entities;

namespace Command
{
    public class GarageDoorOpenCommand: ICommand
    {
        GarageDoor _garegeDoor;

        public GarageDoorOpenCommand(GarageDoor garageDoor)
        {
            _garegeDoor = garageDoor;
        }

        public void execute()
        {
            _garegeDoor.up();
        }
    }
    
}
